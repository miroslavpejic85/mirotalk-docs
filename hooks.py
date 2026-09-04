from datetime import datetime, timezone
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit, urlunsplit
import xml.etree.ElementTree as ElementTree


SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
SOCIAL_IMAGE_PATH = "images/mirotalk-preview.png"
URL_ATTRIBUTE_PATTERN = re.compile(
    r'(?P<prefix>\b(?:href|src)\s*=\s*["\'])(?P<url>[^"\']+)(?P<suffix>["\'])',
    re.IGNORECASE,
)
PRODUCT_LANDING_PAGES = {
    "admin": {
        "name": "MiroTalk Admin",
        "title": "MiroTalk Admin - Self-Hosted Infrastructure Management",
        "description": "Manage self-hosted MiroTalk services from one dashboard with centralized configuration, updates, monitoring, and process control.",
        "previous_url": "mirotalk-admin/",
    },
    "bro": {
        "name": "MiroTalk BRO",
        "title": "MiroTalk BRO - Self-Hosted WebRTC Live Broadcasting",
        "description": "Launch branded low-latency WebRTC broadcasts from your own server with P2P and SFU delivery modes, full source code, and REST API.",
        "previous_url": "mirotalk-bro/",
    },
    "c2c": {
        "name": "MiroTalk C2C",
        "title": "MiroTalk C2C - Self-Hosted One-to-One WebRTC Calls",
        "description": "Add private one-to-one WebRTC video calls to your product with full source code, REST API, iframe integration, and Docker deployment.",
        "previous_url": "mirotalk-c2c/",
    },
    "cme": {
        "name": "MiroTalk Call-Me",
        "title": "Call-Me - Self-Hosted WebRTC Click-to-Call",
        "description": "Add instant self-hosted one-to-one WebRTC calls to your website with shareable links, full source code, REST API, and no recurring platform fees.",
        "previous_url": "mirotalk-cme/",
    },
    "p2p": {
        "name": "MiroTalk P2P",
        "title": "MiroTalk P2P - Self-Hosted Peer-to-Peer Video Conferencing",
        "description": "Own a low-latency peer-to-peer WebRTC meeting platform with full source code, collaboration tools, REST API, and Docker support.",
        "previous_url": "mirotalk-p2p/",
    },
    "projects": {
        "name": "MiroTalk Projects",
        "title": "MiroTalk Projects - Which One Should I Choose?",
        "description": "Compare MiroTalk projects by purpose, audience size, running cost, and trade-offs.",
        "previous_url": "projects/",
    },
    "sfu": {
        "name": "MiroTalk SFU",
        "title": "MiroTalk SFU - Self-Hosted WebRTC Video Conferencing",
        "description": "Own and self-host a scalable WebRTC video conferencing platform with full source code, REST API, Docker deployment, and lifetime updates.",
        "previous_url": "mirotalk-sfu/",
    },
    "ultimate": {
        "name": "MiroTalk Ultimate",
        "title": "MiroTalk Ultimate - Complete Self-Hosted WebRTC Platform",
        "description": "Own seven production-ready MiroTalk WebRTC applications with full source code, self-hosted deployment, lifetime updates, and one-time licensing.",
        "previous_url": "mirotalk-ultimate/",
    },
    "web": {
        "name": "MiroTalk WEB",
        "title": "MiroTalk WEB - Self-Hosted Meeting Scheduler & Dashboard",
        "description": "Build a self-hosted video meeting workspace with user accounts, dashboards, scheduling, subscription plans, and multi-app integration.",
        "previous_url": "mirotalk-web/",
    },
}


def add_landing_page_metadata(site_dir, site_url):
    social_image = urljoin(site_url, SOCIAL_IMAGE_PATH)

    for slug, metadata in PRODUCT_LANDING_PAGES.items():
        page_path = site_dir / "sites" / f"{slug}.html"
        if not page_path.exists():
            continue

        page_url = urljoin(site_url, f"sites/{slug}/")
        previous_url = urljoin(site_url, metadata["previous_url"])
        contents = page_path.read_text(encoding="utf-8").replace(
            previous_url, page_url
        )

        structured_data = json.dumps(
            {
                "@context": "https://schema.org",
                "@type": "SoftwareApplication",
                "name": metadata["name"],
                "applicationCategory": "CommunicationApplication",
                "operatingSystem": "Web, Linux",
                "description": metadata["description"],
                "url": page_url,
                "image": social_image,
            },
            indent=2,
        )

        if 'property="og:title"' not in contents:
            title = escape(metadata["title"], quote=True)
            description = escape(metadata["description"], quote=True)
            tags = f"""
<meta property="og:type" content="website">
<meta property="og:site_name" content="MiroTalk">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{page_url}">
<meta property="og:image" content="{social_image}">
<meta property="og:image:alt" content="{escape(metadata['name'], quote=True)} product preview">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{social_image}">
"""
            contents = contents.replace("</head>", f"{tags}</head>", 1)

        if 'type="application/ld+json"' not in contents:
            structured_data_tag = f"""
<script type="application/ld+json">
{structured_data}
</script>
"""
            contents = contents.replace(
                "</head>", f"{structured_data_tag}</head>", 1
            )

        page_path.write_text(contents, encoding="utf-8")


def publish_clean_site_urls(site_dir, site_url):
    sites_dir = site_dir / "sites"
    standalone_pages = sorted(sites_dir.glob("*.html"))
    clean_routes = {
        page.stem: f"/sites/{page.stem}/" for page in standalone_pages
    }

    def clean_page_reference(match, source_url):
        reference = match.group("url")
        parsed = urlsplit(reference)
        if (
            reference.startswith(("#", "/"))
            or parsed.scheme
            or parsed.netloc
        ):
            return match.group(0)

        resolved = urlsplit(urljoin(source_url, reference))
        path = resolved.path
        if path.startswith("/sites/") and path.endswith(".html"):
            slug = Path(path).stem
            path = clean_routes.get(slug, path)

        clean_reference = urlunsplit(
            (resolved.scheme, resolved.netloc, path, resolved.query, resolved.fragment)
        )
        return (
            f'{match.group("prefix")}{clean_reference}'
            f'{match.group("suffix")}'
        )

    for page_path in standalone_pages:
        slug = page_path.stem
        page_url = urljoin(site_url, f"sites/{slug}/")
        contents = page_path.read_text(encoding="utf-8")
        contents = contents.replace(
            urljoin(site_url, f"sites/{slug}.html"), page_url
        )
        contents = URL_ATTRIBUTE_PATTERN.sub(
            lambda match: clean_page_reference(
                match, f"/sites/{page_path.name}"
            ),
            contents,
        )

        destination = sites_dir / slug / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(contents, encoding="utf-8")
        page_path.unlink()

    replacements = {
        f"/sites/{slug}.html": route for slug, route in clean_routes.items()
    }
    for page_path in site_dir.rglob("*.html"):
        contents = page_path.read_text(encoding="utf-8")
        updated = contents
        for old_path, new_path in replacements.items():
            updated = updated.replace(old_path, new_path)
            updated = updated.replace(old_path.lstrip("/"), new_path.lstrip("/"))
        if updated != contents:
            page_path.write_text(updated, encoding="utf-8")


def on_page_markdown(markdown, page, **kwargs):
    if not page.meta.get("description"):
        page.meta["description"] = (
            f"Learn how to use {page.title} with MiroTalk, including setup, "
            "configuration, examples, and operational guidance."
        )
    return markdown


def on_post_build(config, **kwargs):
    site_dir = Path(config["site_dir"])
    site_url = config["site_url"].rstrip("/") + "/"
    add_landing_page_metadata(site_dir, site_url)
    publish_clean_site_urls(site_dir, site_url)

    sitemap_path = site_dir / "sitemap.xml"
    if not sitemap_path.exists():
        return

    ElementTree.register_namespace("", SITEMAP_NAMESPACE)
    tree = ElementTree.parse(sitemap_path)
    root = tree.getroot()
    location_tag = f"{{{SITEMAP_NAMESPACE}}}loc"
    existing_urls = {
        location.text for location in root.iter(location_tag) if location.text
    }
    docs_dir = Path(config["docs_dir"])

    for source_path in sorted(docs_dir.rglob("*.html")):
        relative_path = source_path.relative_to(docs_dir)
        if relative_path.name == "index.html":
            route = relative_path.parent.as_posix().strip("/") + "/"
        elif relative_path.parent == Path("sites"):
            route = f"sites/{relative_path.stem}/"
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