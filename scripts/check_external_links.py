#!/usr/bin/env python3

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urlsplit
from urllib.request import Request, urlopen


SITE_DIR = Path("site")
SITE_HOST = "docs.mirotalk.com"
EXAMPLE_HOSTS = {"localhost", "127.0.0.1", "your.domain.name"}
USER_AGENT = "MiroTalk-Docs-Link-Checker/1.0"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href:
            self.links.add(href)


def check_url(url: str, timeout: float) -> tuple[str, int | None, str | None]:
    request = Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=timeout) as response:
            return url, response.status, None
    except HTTPError as error:
        if error.code not in {405, 501}:
            return url, error.code, None
    except (TimeoutError, URLError) as error:
        return url, None, str(error)

    request = Request(
        url,
        headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"},
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            return url, response.status, None
    except HTTPError as error:
        return url, error.code, None
    except (TimeoutError, URLError) as error:
        return url, None, str(error)


def main() -> int:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--timeout", type=float, default=10)
    argument_parser.add_argument("--workers", type=int, default=16)
    arguments = argument_parser.parse_args()

    if not SITE_DIR.is_dir():
        print("Generated site directory not found. Run the MkDocs build first.")
        return 1

    links: set[str] = set()
    for page in SITE_DIR.rglob("*.html"):
        parser = LinkParser()
        parser.feed(page.read_text(encoding="utf-8"))
        for link in parser.links:
            url = urldefrag(link).url
            parsed = urlsplit(url)
            hostname = (parsed.hostname or "").lower()
            if (
                parsed.scheme in {"http", "https"}
                and parsed.netloc != SITE_HOST
                and hostname not in EXAMPLE_HOSTS
            ):
                links.add(url)

    hard_failures: list[tuple[str, int]] = []
    warnings: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=arguments.workers) as executor:
        futures = [executor.submit(check_url, url, arguments.timeout) for url in sorted(links)]
        for future in as_completed(futures):
            url, status, error = future.result()
            if status in {404, 410}:
                hard_failures.append((url, status))
            elif error:
                warnings.append((url, error))
            elif status is not None and status >= 500:
                warnings.append((url, f"HTTP {status}"))

    if warnings:
        print(f"External link warnings ({len(warnings)}):")
        for url, reason in sorted(warnings):
            print(f"- {url}: {reason}")

    if hard_failures:
        print(f"Broken external links ({len(hard_failures)}):")
        for url, status in sorted(hard_failures):
            print(f"- HTTP {status}: {url}")
        return 1

    print(f"Checked {len(links)} external links; no HTTP 404 or 410 responses found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())