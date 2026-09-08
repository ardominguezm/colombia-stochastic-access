"""Download helpers with provenance and checksum recording."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


MACHINE_READABLE_SUFFIXES = (
    ".csv",
    ".zip",
    ".xlsx",
    ".xls",
    ".txt",
    ".json",
    ".geojson",
    ".shp",
)
RESOURCE_KEYS = {"downloadurl", "contenturl"}


def sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _is_machine_readable(url: str) -> bool:
    clean = url.lower().split("?", 1)[0]
    return clean.endswith(MACHINE_READABLE_SUFFIXES) or "/download/" in clean


def _walk_metadata(value):
    """Yield download-like URLs recursively from JSON metadata."""
    if isinstance(value, dict):
        for key, item in value.items():
            if key.lower() in RESOURCE_KEYS and isinstance(item, str):
                yield item
            yield from _walk_metadata(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_metadata(item)


def _decode_json_string(value: str) -> str:
    """Decode escaped slashes and unicode found in embedded JSON strings."""
    try:
        return json.loads(f'"{value}"')
    except (json.JSONDecodeError, TypeError):
        return value.replace("\\/", "/")


def discover_resources_from_html(html: str, catalog_url: str) -> list[str]:
    """Extract direct resources from anchors and embedded DCAT/JSON metadata."""
    soup = BeautifulSoup(html, "html.parser")
    candidates: list[str] = []

    for anchor in soup.select("a[href]"):
        candidates.append(anchor.get("href", ""))

    for script in soup.select('script[type="application/ld+json"], script[type="application/json"]'):
        payload = script.string or script.get_text()
        if not payload.strip():
            continue
        try:
            candidates.extend(_walk_metadata(json.loads(payload)))
        except json.JSONDecodeError:
            pass

    # AMVA embeds DCAT distributions in page state, sometimes outside script tags.
    for raw in re.findall(r'"(?:downloadURL|contentUrl)"\s*:\s*"([^"]+)"', html, flags=re.I):
        candidates.append(_decode_json_string(raw))

    urls = []
    for candidate in candidates:
        if not isinstance(candidate, str) or not candidate:
            continue
        url = urljoin(catalog_url, candidate)
        if _is_machine_readable(url):
            urls.append(url)
    return list(dict.fromkeys(urls))


def discover_resources(catalog_url: str, timeout: int = 60) -> list[str]:
    """Find direct machine-readable resources on an open-data catalog page."""
    response = requests.get(catalog_url, timeout=timeout)
    response.raise_for_status()
    return discover_resources_from_html(response.text, catalog_url)


def choose_resource(urls: list[str]) -> str | None:
    """Prefer CSV, then compressed/tabular alternatives, deterministically."""
    preference = {".csv": 0, ".zip": 1, ".xlsx": 2, ".xls": 3, ".txt": 4}
    candidates = [url for url in dict.fromkeys(urls) if _is_machine_readable(url)]
    if not candidates:
        return None

    def rank(url: str):
        suffix = Path(urlparse(url).path).suffix.lower()
        return preference.get(suffix, 99), url.lower()

    return min(candidates, key=rank)


def download(url: str, destination: str | Path, timeout: int = 180) -> dict:
    """Stream a URL to disk and return a provenance record."""
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=timeout) as response:
        response.raise_for_status()
        with destination.open("wb") as stream:
            for block in response.iter_content(1024 * 1024):
                if block:
                    stream.write(block)
    return {
        "url": url,
        "path": str(destination),
        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
    }


def write_manifest(records: list[dict], destination: str | Path) -> None:
    Path(destination).write_text(json.dumps(records, indent=2), encoding="utf-8")
