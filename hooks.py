from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
import xml.etree.ElementTree as ElementTree


SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"


def on_post_build(config, **kwargs):
    sitemap_path = Path(config["site_dir"]) / "sitemap.xml"
    if not sitemap_path.exists():
        return

    ElementTree.register_namespace("", SITEMAP_NAMESPACE)
    tree = ElementTree.parse(sitemap_path)
    root = tree.getroot()
    location_tag = f"{{{SITEMAP_NAMESPACE}}}loc"
    existing_urls = {
        location.text for location in root.iter(location_tag) if location.text
    }
    site_url = config["site_url"].rstrip("/") + "/"
    docs_dir = Path(config["docs_dir"])

    for source_path in sorted(docs_dir.rglob("*.html")):
        relative_path = source_path.relative_to(docs_dir)
        if relative_path.name == "index.html":
            route = relative_path.parent.as_posix().strip("/") + "/"
        else:
            route = relative_path.as_posix()

        page_url = urljoin(site_url, route)
        if page_url in existing_urls:
            continue

        url_element = ElementTree.SubElement(
            root, f"{{{SITEMAP_NAMESPACE}}}url"
        )
        ElementTree.SubElement(url_element, location_tag).text = page_url
        modified_at = datetime.fromtimestamp(
            source_path.stat().st_mtime, timezone.utc
        ).date()
        ElementTree.SubElement(
            url_element, f"{{{SITEMAP_NAMESPACE}}}lastmod"
        ).text = modified_at.isoformat()
        existing_urls.add(page_url)

    root[:] = sorted(root, key=lambda item: item.findtext(location_tag, ""))
    tree.write(sitemap_path, encoding="UTF-8", xml_declaration=True)