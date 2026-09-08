"""Download helpers with provenance and checksum recording."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


MACHINE_READABLE_SUFFIXES = (".csv", ".zip", ".xlsx", ".xls", ".json", ".geojson", ".shp")


def sha256(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def discover_resources(catalog_url: str, timeout: int = 60) -> list[str]:
    """Find direct machine-readable resource links on an open-data page."""
    response = requests.get(catalog_url, timeout=timeout)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    urls = []
    for anchor in soup.select("a[href]"):
        url = urljoin(catalog_url, anchor.get("href"))
        clean = url.lower().split("?", 1)[0]
        if clean.endswith(MACHINE_READABLE_SUFFIXES) or "/download/" in clean:
            urls.append(url)
    return list(dict.fromkeys(urls))


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

