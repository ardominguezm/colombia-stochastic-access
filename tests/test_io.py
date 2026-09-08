from stochastic_access.io import choose_resource, discover_resources_from_html


def test_discovers_amva_dcat_download_url_with_escaped_slashes():
    html = r"""
    <div>JSON Metadata</div>
    {"data":{"@type":"dcat:Distribution",
    "downloadURL":"https:\/\/datosabiertos.metropol.gov.co\/sites\/default\/files\/uploaded_resources\/EOD_2017_DatosHogares.csv"}}
    """
    urls = discover_resources_from_html(
        html,
        "https://datosabiertos.metropol.gov.co/dataset/eod-hogares",
    )
    assert urls == [
        "https://datosabiertos.metropol.gov.co/sites/default/files/uploaded_resources/EOD_2017_DatosHogares.csv"
    ]


def test_discovers_json_ld_and_prefers_csv():
    html = """
    <script type="application/ld+json">
    {"distribution": [
      {"contentUrl": "/files/table.xlsx"},
      {"downloadURL": "/files/table.csv"}
    ]}
    </script>
    """
    urls = discover_resources_from_html(html, "https://example.org/catalog")
    assert choose_resource(urls) == "https://example.org/files/table.csv"


def test_ignores_non_machine_readable_links():
    html = '<a href="/about">About</a><a href="/files/data.txt">Data</a>'
    urls = discover_resources_from_html(html, "https://example.org/catalog")
    assert urls == ["https://example.org/files/data.txt"]
