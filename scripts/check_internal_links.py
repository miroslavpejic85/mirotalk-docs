#!/usr/bin/env python3

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


SITE_DIR = Path("site").resolve()
SITE_HOST = "docs.mirotalk.com"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        element_id = attributes.get("id")
        if element_id:
            self.ids.add(element_id)

        attribute = "href" if tag == "a" else "src" if tag in {"img", "script"} else None
        if attribute and attributes.get(attribute):
            self.references.append((tag, attributes[attribute] or ""))


def resolve_target(source: Path, reference: str) -> tuple[Path, str] | None:
    parsed = urlsplit(reference)
    if parsed.scheme in {"mailto", "tel", "javascript", "data"}:
        return None
    if parsed.scheme or parsed.netloc:
        if parsed.scheme not in {"http", "https"} or parsed.netloc != SITE_HOST:
            return None

    path = unquote(parsed.path)
    if not path:
        target = source
    elif path.startswith("/"):
        target = SITE_DIR / path.lstrip("/")
    else:
        target = source.parent / path

    target = target.resolve()
    if SITE_DIR not in target.parents and target != SITE_DIR:
        return target, parsed.fragment
    if target.is_dir() or path.endswith("/"):
        target /= "index.html"
    return target, unquote(parsed.fragment)


def main() -> int:
    if not SITE_DIR.is_dir():
        print("Generated site directory not found. Run the MkDocs build first.")
        return 1

    pages: dict[Path, PageParser] = {}
    for page in sorted(SITE_DIR.rglob("*.html")):
        parser = PageParser()
        parser.feed(page.read_text(encoding="utf-8"))
        pages[page.resolve()] = parser

    failures: set[str] = set()
    checked = 0
    for source, parser in pages.items():
        for tag, reference in parser.references:
            resolved = resolve_target(source, reference)
            if resolved is None:
                continue
            target, fragment = resolved
            checked += 1
            source_name = source.relative_to(SITE_DIR)

            if not target.exists():
                failures.add(f"{source_name}: {tag} target not found: {reference}")
                continue
            if fragment and target.suffix == ".html":
                target_parser = pages.get(target)
                if target_parser is None or fragment not in target_parser.ids:
                    failures.add(f"{source_name}: fragment not found: {reference}")

    if failures:
        print("Internal link validation failed:")
        for failure in sorted(failures):
            print(f"- {failure}")
        return 1

    print(f"Validated {checked} internal links and assets across {len(pages)} HTML pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())