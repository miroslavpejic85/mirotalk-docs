#!/usr/bin/env python3

from __future__ import annotations

from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path


SITE_DIR = Path("site")
EXEMPT_PAGES = {Path("license/licensing-options/index.html")}


class MetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.canonical: list[str] = []
        self.descriptions: list[str] = []
        self.h1_count = 0
        self.in_title = False
        self.title_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta" and attributes.get("name", "").lower() == "description":
            self.descriptions.append(attributes.get("content", ""))
        elif tag == "link" and "canonical" in attributes.get("rel", "").split():
            href = attributes.get("href")
            if href:
                self.canonical.append(href)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_parts).split())


def main() -> int:
    if not SITE_DIR.is_dir():
        print("Generated site directory not found. Run the MkDocs build first.")
        return 1

    failures: list[str] = []
    values: dict[str, dict[str, list[Path]]] = {
        "title": defaultdict(list),
        "description": defaultdict(list),
        "canonical": defaultdict(list),
    }
    checked = 0

    for page in sorted(SITE_DIR.rglob("index.html")):
        relative_path = page.relative_to(SITE_DIR)
        if relative_path in EXEMPT_PAGES:
            continue

        parser = MetadataParser()
        parser.feed(page.read_text(encoding="utf-8"))
        checked += 1

        if not parser.title:
            failures.append(f"{relative_path}: missing title")
        else:
            values["title"][parser.title].append(relative_path)
        if len(parser.descriptions) != 1:
            failures.append(
                f"{relative_path}: expected 1 meta description, found {len(parser.descriptions)}"
            )
        elif not parser.descriptions[0].strip():
            failures.append(f"{relative_path}: empty meta description")
        else:
            values["description"][parser.descriptions[0]].append(relative_path)
        if len(parser.canonical) != 1:
            failures.append(
                f"{relative_path}: expected 1 canonical URL, found {len(parser.canonical)}"
            )
        else:
            values["canonical"][parser.canonical[0]].append(relative_path)
        if parser.h1_count != 1:
            failures.append(f"{relative_path}: expected 1 H1, found {parser.h1_count}")

    for field, grouped_values in values.items():
        for value, pages in grouped_values.items():
            if len(pages) > 1:
                paths = ", ".join(str(page) for page in pages)
                failures.append(f'duplicate {field} "{value}": {paths}')

    if failures:
        print("Generated site metadata validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"Metadata valid for {checked} generated pages; "
        f"{len(EXEMPT_PAGES)} legacy redirect is exempt."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())