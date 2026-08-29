#!/usr/bin/env python3

from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
ALLOWED_UNLISTED = {
    "license/licensing-options/index.html",
    "sites/bro.html",
    "sites/c2c.html",
    "sites/cme.html",
    "sites/p2p.html",
    "sites/sfu.html",
    "sites/ultimate.html",
    "sites/web.html",
}
PUBLISHED_SUFFIXES = {".html", ".md", ".sh"}


def collect_nav_targets(value):
    if isinstance(value, str):
        if not value.startswith(("http://", "https://")):
            yield value
        return

    if isinstance(value, list):
        for item in value:
            yield from collect_nav_targets(item)
        return

    if isinstance(value, dict):
        for item in value.values():
            yield from collect_nav_targets(item)


def main():
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
    nav_targets = list(collect_nav_targets(config["nav"]))
    nav_counts = Counter(nav_targets)

    source_targets = {
        path.relative_to(DOCS_DIR).as_posix()
        for path in DOCS_DIR.rglob("*")
        if path.is_file() and path.suffix in PUBLISHED_SUFFIXES
    }
    expected_targets = source_targets - ALLOWED_UNLISTED

    missing = sorted(expected_targets - nav_counts.keys())
    unknown = sorted(nav_counts.keys() - source_targets)
    duplicates = sorted(
        target for target, count in nav_counts.items() if count > 1
    )
    stale_allowlist = sorted(ALLOWED_UNLISTED - source_targets)

    problems = {
        "missing from navigation": missing,
        "unknown navigation target": unknown,
        "duplicate navigation target": duplicates,
        "stale allowlist entry": stale_allowlist,
    }
    failed = False
    for label, targets in problems.items():
        if not targets:
            continue
        failed = True
        print(f"{label}:")
        for target in targets:
            print(f"  - {target}")

    if failed:
        raise SystemExit(1)

    print(
        f"Navigation covers {len(expected_targets)} published sources "
        f"exactly once; {len(ALLOWED_UNLISTED)} standalone or legacy "
        "routes are intentionally unlisted."
    )


if __name__ == "__main__":
    main()