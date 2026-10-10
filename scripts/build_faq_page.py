#!/usr/bin/env python3
"""Generate docs/sites/faq.html, the interactive FAQ, from docs/faq/index.md.

MkDocs runs this automatically before every build (see hooks.py). Manual use:
    python scripts/build_faq_page.py           # write docs/sites/faq.html
    python scripts/build_faq_page.py --check   # fail if the page is out of date
"""

from __future__ import annotations

import argparse
import posixpath
import re
import sys
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import markdown


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "faq" / "index.md"
OUTPUT = ROOT / "docs" / "sites" / "faq.html"
SOURCE_ROUTE = "/faq/"
PAGE_URL = "https://docs.mirotalk.com/sites/faq/"
TITLE = "MiroTalk FAQ - Searchable Questions and Answers"
DESCRIPTION = (
    "Search answers about MiroTalk products, self-hosting, STUN/TURN, licensing, "
    "scaling, security, and troubleshooting in one interactive FAQ."
)

QUESTION_PATTERN = re.compile(r'^\?\?\? question "(?P<question>.+)"\s*$')
LINK_PATTERN = re.compile(r'(?P<prefix>\bhref=")(?P<url>[^"]+)(?P<suffix>")')


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def parse_faq(text: str) -> tuple[str, list[dict]]:
    title = "Frequently Asked Questions"
    sections: list[dict] = []
    question: dict | None = None

    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
        elif line.startswith("## "):
            sections.append({"title": line[3:].strip(), "questions": []})
            question = None
        elif QUESTION_PATTERN.match(line):
            if not sections:
                raise ValueError("Question found before the first section heading.")
            question = {"question": QUESTION_PATTERN.match(line)["question"], "lines": []}
            sections[-1]["questions"].append(question)
        elif question is not None:
            if line.startswith("    "):
                question["lines"].append(line[4:])
            elif not line.strip():
                question["lines"].append("")
            elif line.strip() != "---":
                raise ValueError(f"Unexpected content after a question: {line!r}")

    return title, [section for section in sections if section["questions"]]


def site_route(reference: str) -> str:
    """Convert a relative Markdown link to the published route."""
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "/")):
        return reference

    path = posixpath.normpath(posixpath.join(SOURCE_ROUTE, parsed.path))
    if parsed.path.endswith("/") and not path.endswith("/"):
        path += "/"
    if path.endswith(".md"):
        path = path[: -len("index.md")] if path.endswith("/index.md") else path[:-3] + "/"
    elif path.endswith(".html") and path.startswith("/sites/"):
        path = path[: -len(".html")] + "/"
    return urlunsplit(("", "", path, parsed.query, parsed.fragment))


def render_answer(lines: list[str]) -> str:
    html = markdown.markdown("\n".join(lines), extensions=["tables", "fenced_code"])
    html = LINK_PATTERN.sub(
        lambda m: f'{m["prefix"]}{site_route(m["url"])}{m["suffix"]}', html
    )
    external = re.compile(r'<a href="(https?://[^"]+)"')
    html = external.sub(r'<a href="\1" target="_blank" rel="noopener noreferrer"', html)
    return html.replace("<table>", '<div class="table-wrap"><table>').replace(
        "</table>", "</table></div>"
    )


SECTION_ICONS = {
    "general": "info",
    "products": "layers",
    "self-hosting-deployment": "server",
    "stun-turn-servers": "network",
    "configuration": "settings",
    "api-integration": "plug",
    "features": "sparkles",
    "licensing": "key-round",
    "room-customization": "sliders-horizontal",
    "scaling-architecture": "trending-up",
    "updates-maintenance": "refresh-cw",
    "internationalization": "languages",
    "database-email": "database",
    "security": "shield-check",
    "troubleshooting": "life-buoy",
}
POPULAR_QUESTIONS = [
    ("Which MiroTalk product should I choose?", "Choose a product"),
    ("How can I self-host MiroTalk?", "Self-host"),
    ("What are the server requirements?", "Server requirements"),
    ("What are STUN and TURN servers, and why do I need them?", "STUN & TURN"),
    ("What are the licensing options for MiroTalk?", "Licensing"),
    ("My video/audio is not working. What should I check?", "Video or audio not working"),
]


TONES = ("green", "blue", "coral", "gold")
DEEPER_SECTION = re.compile(r"^## Go deeper\s*$(?P<body>.*?)(?=^## |\Z)", re.MULTILINE | re.DOTALL)
DEEPER_CARD = re.compile(
    r'<a class="chooser-choice[^"]*" href="(?P<href>[^"]+)">\s*'
    r'<span class="chooser-code">(?P<code>[^<]+)</span>\s*'
    r'<span class="chooser-copy"><strong>(?P<title>[^<]+)</strong><small>(?P<text>[^<]+)</small></span>'
)


def parse_deeper(text: str) -> list[dict]:
    """Read the "Go deeper" cards from the Markdown page, skipping links to this page."""
    section = DEEPER_SECTION.search(text)
    cards = []
    for match in DEEPER_CARD.finditer(section["body"] if section else ""):
        href = site_route(match["href"])
        if href != urlsplit(PAGE_URL).path:
            cards.append({**match.groupdict(), "href": href})
    return cards


def render_squares(sections: list[dict]) -> str:
    squares = [
        '<button class="need active" type="button" data-section="all" aria-pressed="true">'
        '<i data-lucide="layout-grid"></i><span class="name">All topics</span>'
        '<span class="num"></span></button>'
    ]
    for index, section in enumerate(sections):
        section_id = slugify(section["title"])
        squares.append(
            f'<button class="need tone-{TONES[index % len(TONES)]}" type="button" '
            f'data-section="{section_id}" aria-pressed="false">'
            f'<i data-lucide="{SECTION_ICONS.get(section_id, "circle-help")}"></i>'
            f'<span class="name">{escape(section["title"])}</span>'
            f'<span class="num">{len(section["questions"])}</span></button>'
        )
    return "\n".join(squares)


def render_deeper(cards: list[dict]) -> str:
    if not cards:
        return ""
    items = "\n".join(
        f'<a href="{escape(card["href"], quote=True)}"><span class="code">{escape(card["code"])}</span>'
        f'<span><strong>{escape(card["title"])}</strong><small>{escape(card["text"])}</small></span></a>'
        for card in cards
    )
    return (
        '<section class="deeper" aria-labelledby="deeper-title">\n'
        '<h2 id="deeper-title">Go deeper</h2>\n<p>Need more than a quick answer? These guides cover the details.</p>\n'
        f'<div class="quick">\n{items}\n</div>\n</section>'
    )


def render_body(sections: list[dict]) -> tuple[str, str, str, str, int]:
    topics = [
        '<button class="topic active" type="button" data-section="all" aria-pressed="true">'
        '<i data-lucide="layout-grid"></i><span class="name">All topics</span>'
        '<span class="num"></span></button>'
    ]
    options = ['<option value="all">All topics</option>']
    blocks = []
    total = 0
    ids: dict[str, str] = {}

    for section in sections:
        section_id = slugify(section["title"])
        icon = SECTION_ICONS.get(section_id, "circle-help")
        count = len(section["questions"])
        total += count
        topics.append(
            f'<button class="topic" type="button" data-section="{section_id}" aria-pressed="false">'
            f'<i data-lucide="{icon}"></i><span class="name">{escape(section["title"])}</span>'
            f'<span class="num">{count}</span></button>'
        )
        options.append(
            f'<option value="{section_id}" data-name="{escape(section["title"], quote=True)}">'
            f'{escape(section["title"])} ({count})</option>'
        )
        items = []
        for question in section["questions"]:
            question_id = slugify(question["question"])
            if question_id in ids.values():
                raise ValueError(f"Duplicate question id: {question_id}")
            ids[question["question"]] = question_id
            text = escape(question["question"])
            items.append(
                f'<details class="qa" id="{question_id}">\n'
                f'<summary><span class="qwrap"><span class="q" data-text="{text}">{text}</span>'
                '<span class="snippet" hidden></span></span></summary>\n'
                f'<div class="answer">\n{render_answer(question["lines"])}\n'
                f'<div class="answer-foot"><button class="copy" type="button" data-id="{question_id}">'
                '<i data-lucide="link"></i><span>Copy link</span></button></div></div>\n'
                "</details>"
            )
        blocks.append(
            f'<section class="faq-section" id="{section_id}" data-section="{section_id}">\n'
            f'<h2><span class="icon"><i data-lucide="{icon}"></i></span>{escape(section["title"])}</h2>\n'
            + "\n".join(items)
            + "\n</section>"
        )

    popular = []
    for question, label in POPULAR_QUESTIONS:
        if question not in ids:
            raise ValueError(f"Popular question not found in the FAQ: {question}")
        popular.append(f'<a href="#{ids[question]}">{escape(label)}</a>')

    return "\n".join(topics), "\n".join(blocks), "\n".join(popular), "\n".join(options), total


STYLE = """
    :root {
      color-scheme: light;
      --ink: #18231f; --muted: #607069; --paper: #f7f9f7; --surface: #fff;
      --soft: #edf2ef; --line: #d8e2dc; --green: #087f5b; --green2: #056347;
      --mint: #dff5eb; --blue: #1769aa; --bluebg: #e5f2fb; --coral: #d9503f;
      --coralbg: #fbe9e5; --gold: #a76808; --goldbg: #fff1d4; --mark: #fff0a8;
      --shadow: 0 18px 50px #18231f17; --accent-bg: var(--green2); --accent-fg: #fff;
      --tone-green: #64d8ad; --tone-blue: #79b9e8; --tone-coral: #ff8b7c; --tone-gold: #efbd67
    }
    [data-theme="dark"] {
      color-scheme: dark;
      --ink: #edf5f1; --muted: #a7b7af; --paper: #101714; --surface: #17201c;
      --soft: #202b26; --line: #33423b; --green: #61d6aa; --green2: #8ce5c3;
      --mint: #173c2f; --blue: #79b9e8; --bluebg: #173247; --coral: #ff8b7c;
      --coralbg: #45251f; --gold: #efbd67; --goldbg: #3d311d; --mark: #5c4b12;
      --shadow: 0 18px 50px #0004; --accent-fg: #102119;
      --tone-green: #087f5b; --tone-blue: #1769aa; --tone-coral: #d9503f; --tone-gold: #a76808
    }
    * { box-sizing: border-box }
    html { scroll-behavior: smooth; scroll-padding-top: 140px }
    body { margin: 0; color: var(--ink); font: 16px/1.65 'DM Sans', sans-serif; background: linear-gradient(90deg, color-mix(in srgb, var(--line) 38%, transparent) 1px, transparent 1px) 0 0/42px 42px, linear-gradient(color-mix(in srgb, var(--line) 38%, transparent) 1px, transparent 1px) 0 0/42px 42px, var(--paper) }
    body:before { content: ''; position: fixed; inset: 0; z-index: -1; background: linear-gradient(180deg, transparent, var(--paper) 65rem); pointer-events: none }
    a { color: var(--blue) } button, input { color: inherit; font: inherit }
    :focus-visible { outline: 3px solid var(--green); outline-offset: 3px }
    [hidden] { display: none !important }
    svg { flex: none }
    .shell { width: min(1160px, calc(100% - 40px)); margin-inline: auto }
    .site-header { position: sticky; top: 0; z-index: 20; border-bottom: 1px solid var(--line); background: color-mix(in srgb, var(--paper) 88%, transparent); backdrop-filter: blur(16px) }
    nav { display: flex; min-height: 68px; gap: 28px; align-items: center }
    .brand { display: flex; gap: 10px; align-items: center; color: var(--ink); font: 800 1rem Manrope, sans-serif; text-decoration: none }
    .mark { display: grid; width: 34px; height: 34px; place-items: center; border-radius: 50%; background: var(--green2); color: #fff }
    [data-theme="dark"] .mark { color: #102119 }
    .mark svg, .theme svg { width: 19px; height: 19px }
    .links { display: flex; gap: 24px; margin-left: auto }
    .links a { color: var(--muted); font-size: .9rem; font-weight: 600; text-decoration: none }
    .links a:hover { color: var(--ink) }
    .theme { display: grid; width: 40px; height: 40px; padding: 0; place-items: center; border: 1px solid var(--line); border-radius: 7px; background: var(--surface); color: var(--ink); cursor: pointer }
    .theme .sun { display: none }
    [data-theme="dark"] .theme .moon { display: none }
    [data-theme="dark"] .theme .sun { display: block }
    h1, h2, h3 { margin-top: 0; font-family: Manrope, sans-serif; line-height: 1.12; letter-spacing: 0 }

    .hero { padding: 64px 0 48px; border-bottom: 1px solid var(--line); background: linear-gradient(180deg, var(--mint), transparent) }
    .hero .shell { max-width: 800px; text-align: center }
    .eyebrow { display: inline-flex; gap: 8px; align-items: center; margin: 0; color: var(--green); font-size: .77rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase }
    .eyebrow:before { content: ''; width: 28px; height: 2px; background: currentColor }
    h1 { margin: 16px 0 14px; font-size: clamp(2.4rem, 5.5vw, 4rem) }
    .lead { margin: 0 auto 26px; max-width: 54ch; color: var(--muted); font-size: 1.16rem }
    .searchbox { position: relative }
    .searchbox > svg { position: absolute; top: 50%; left: 18px; width: 20px; height: 20px; color: var(--muted); transform: translateY(-50%); pointer-events: none }
    .search { width: 100%; padding: 16px 48px 16px 50px; border: 2px solid var(--line); border-radius: 8px; background: var(--surface); font-size: 1.05rem; box-shadow: var(--shadow) }
    .search:focus { border-color: var(--green); outline: none }
    .search::-webkit-search-cancel-button { display: none }
    .clear { position: absolute; top: 50%; right: 10px; display: none; width: 34px; height: 34px; padding: 0; place-items: center; border: 0; border-radius: 50%; background: var(--soft); cursor: pointer; transform: translateY(-50%) }
    .clear.visible { display: grid }
    .clear svg { width: 16px; height: 16px }
    .popular { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; justify-content: center; margin-top: 18px; color: var(--muted); font-size: .88rem }
    .popular a { padding: 4px 12px; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); color: var(--ink); font-weight: 600; text-decoration: none }
    .popular a:hover { border-color: var(--green); color: var(--green) }

    .chooser { padding: 64px 0; background: var(--ink); color: var(--paper) }
    [data-theme="dark"] .chooser { background: #eaf2ee; color: #16211c }
    .chooser .eyebrow { color: var(--tone-green) }
    .chooser h2 { margin: 12px 0 10px; font-size: clamp(1.8rem, 3.5vw, 2.6rem) }
    .chooser .intro { max-width: 700px; margin-bottom: 30px }
    .chooser .intro p { margin: 0; color: color-mix(in srgb, currentColor 70%, transparent); font-size: 1.05rem }
    .needs { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px }
    .need { --tone: var(--tone-green); position: relative; display: flex; min-height: 112px; flex-direction: column; gap: 4px; padding: 16px; border: 1px solid color-mix(in srgb, currentColor 24%, transparent); border-radius: 7px; background: transparent; color: inherit; text-align: left; cursor: pointer }
    .need.tone-blue { --tone: var(--tone-blue) }
    .need.tone-coral { --tone: var(--tone-coral) }
    .need.tone-gold { --tone: var(--tone-gold) }
    .need svg { width: 22px; height: 22px; margin-bottom: 6px; color: var(--tone) }
    .need .name { font-weight: 700; line-height: 1.35 }
    .need .num { position: absolute; top: 12px; right: 12px; min-width: 24px; padding: 0 7px; border-radius: 999px; background: color-mix(in srgb, currentColor 14%, transparent); font-size: .75rem; font-weight: 700; text-align: center }
    .need:hover, .need.active { border-color: var(--tone); background: color-mix(in srgb, var(--tone) 14%, transparent) }
    .need.zero:not(.active) { opacity: .45 }

    .layout { display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 40px; align-items: start; padding: 48px 0 72px }
    .sidebar { position: sticky; top: 140px; max-height: calc(100vh - 160px); overflow-y: auto }
    .sidebar h2 { margin: 0 0 8px 10px; color: var(--muted); font: 700 .75rem 'DM Sans', sans-serif; letter-spacing: .08em; text-transform: uppercase }
    .topics { display: flex; flex-direction: column; gap: 2px }
    .topic { display: flex; gap: 10px; align-items: center; padding: 6px 10px; border: 0; border-radius: 7px; background: none; font-size: .92rem; font-weight: 500; text-align: left; cursor: pointer }
    .topic svg { width: 17px; height: 17px; color: var(--muted) }
    .topic .name { flex: 1 }
    .topic .num { min-width: 22px; padding: 0 6px; border-radius: 999px; background: var(--soft); color: var(--muted); font-size: .75rem; text-align: center }
    .topic:hover { background: var(--soft) }
    .topic.active { background: var(--accent-bg); color: var(--accent-fg); font-weight: 700 }
    .topic.active svg { color: inherit }
    .topic.active .num { background: color-mix(in srgb, var(--accent-fg) 22%, transparent); color: inherit }
    .topic.zero:not(.active) { opacity: .45 }

    .content { min-width: 0 }
    .status { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; justify-content: space-between; margin-bottom: 4px; color: var(--muted); font-size: .88rem }
    .status .actions { display: flex; gap: 6px }
    .link-button { padding: 4px 10px; border: 1px solid var(--line); border-radius: 6px; background: var(--surface); font-size: .82rem; font-weight: 600; cursor: pointer }
    .link-button:hover { border-color: var(--green); color: var(--green) }
    .sections { display: flex; flex-direction: column }
    .faq-section { display: flex; flex-direction: column; margin-top: 28px }
    .faq-section h2 { order: -1; display: flex; gap: 12px; align-items: center; margin-bottom: 14px; font-size: 1.3rem }
    .faq-section h2 .icon { display: grid; width: 38px; height: 38px; place-items: center; border-radius: 7px; background: var(--soft); color: var(--green) }
    .faq-section h2 svg { width: 18px; height: 18px }
    .qa { margin-bottom: 10px; border: 1px solid var(--line); border-left: 4px solid var(--line); border-radius: 8px; background: var(--surface); transition: border-color .15s }
    .qa:hover { border-left-color: var(--green) }
    .qa[open] { border-left-color: var(--green); box-shadow: var(--shadow) }
    .qa summary { display: flex; gap: 16px; align-items: center; justify-content: space-between; padding: 16px 18px; font-size: 1.04rem; font-weight: 600; line-height: 1.4; cursor: pointer; list-style: none }
    .qa summary::-webkit-details-marker { display: none }
    .qa summary::after { flex: none; width: 24px; height: 24px; border-radius: 50%; background: var(--soft) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23056347' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M12 6v12M6 12h12'/%3E%3C/svg%3E") center/14px no-repeat; content: '' }
    .qa[open] summary::after { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23056347' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E") }
    [data-theme="dark"] .qa summary::after { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%238ce5c3' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M12 6v12M6 12h12'/%3E%3C/svg%3E") }
    [data-theme="dark"] .qa[open] summary::after { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%238ce5c3' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E") }
    .qwrap { display: flex; flex-direction: column; gap: 4px; min-width: 0 }
    .snippet { color: var(--muted); font-size: .86rem; font-weight: 400; line-height: 1.5 }
    .qa[open] .snippet { display: none }
    .stickybar { position: fixed; top: 68px; right: 0; left: 0; z-index: 19; padding: 8px 0; border-bottom: 1px solid var(--line); background: color-mix(in srgb, var(--paper) 94%, transparent); backdrop-filter: blur(14px) }
    .stickybar .search { padding: 9px 90px 9px 44px; border-width: 1px; border-radius: 10px; font-size: .95rem; box-shadow: none }
    .stickybar .searchbox > svg { left: 15px; width: 18px; height: 18px }
    .sticky-count { position: absolute; top: 50%; right: 14px; color: var(--muted); font-size: .8rem; transform: translateY(-50%); pointer-events: none }
    .topic-select { display: none; gap: 10px; align-items: center; font-size: .88rem; font-weight: 600 }
    .topic-select select { flex: 1; min-width: 0; padding: 10px 12px; border: 1px solid var(--line); border-radius: 10px; background: var(--surface); font: inherit; font-size: 1rem }
    mark { padding: 0 2px; border-radius: 3px; background: var(--mark); color: inherit }
    .answer { padding: 4px 20px 18px; border-top: 1px solid var(--line); line-height: 1.75 }
    .answer > :first-child { margin-top: 16px }
    .answer p, .answer ul, .answer ol { max-width: 70ch; margin: 0 0 12px }
    .answer li { margin-bottom: 4px }
    .answer table { width: 100%; border-collapse: collapse; font-size: .9rem; line-height: 1.5 }
    .answer th, .answer td { padding: 9px 12px; border: 1px solid var(--line); text-align: left; vertical-align: top }
    .answer th { background: var(--soft) }
    .table-wrap { overflow-x: auto; margin-bottom: 12px }
    .answer code { padding: 1px 5px; border-radius: 4px; background: var(--soft); font-size: .88em }
    .answer pre { overflow-x: auto; margin: 0 0 14px; padding: 14px 16px; border: 1px solid var(--line); border-radius: 8px; background: var(--soft); line-height: 1.5 }
    .answer pre code { padding: 0; background: none }
    .answer-foot { display: flex; justify-content: flex-end; margin-top: 6px }
    .copy { display: inline-flex; gap: 6px; align-items: center; padding: 4px 8px; border: 0; border-radius: 6px; background: none; color: var(--muted); font-size: .8rem; cursor: pointer }
    .copy:hover { background: var(--soft); color: var(--ink) }
    .copy svg { width: 14px; height: 14px }
    .empty { display: none; margin-top: 28px; padding: 36px 24px; border: 1px dashed var(--line); border-radius: 12px; color: var(--muted); text-align: center }
    .empty.visible { display: block }
    .empty strong { display: block; margin-bottom: 6px; color: var(--ink); font-size: 1.1rem }
    .empty .link-button { margin-top: 12px }
    .help { display: flex; flex-wrap: wrap; gap: 16px; align-items: center; justify-content: space-between; margin-top: 28px; padding: 24px; border: 1px solid var(--line); border-radius: 8px; background: var(--mint) }
    .help h2 { margin-bottom: 4px; font-size: 1.2rem }
    .help p { margin: 0; color: var(--muted) }
    .button { display: inline-flex; min-height: 46px; gap: 8px; align-items: center; justify-content: center; padding: 0 18px; border-radius: 7px; background: var(--accent-bg); color: var(--accent-fg); font-weight: 700; text-decoration: none; transition: transform .16s }
    .button:hover { transform: translateY(-2px) }
    .to-top { position: fixed; right: 20px; bottom: 20px; z-index: 15; display: none; width: 44px; height: 44px; padding: 0; place-items: center; border: 1px solid var(--line); border-radius: 50%; background: var(--surface); box-shadow: var(--shadow); cursor: pointer }
    .to-top.visible { display: grid }
    .to-top svg { width: 20px; height: 20px }
    footer { border-top: 1px solid var(--line); background: var(--surface) }
    .footer { display: flex; min-height: 110px; gap: 24px; align-items: center; justify-content: space-between; color: var(--muted); font-size: .82rem }
    .footer p { margin: 0 }
    .footer div { display: flex; flex-wrap: wrap; gap: 18px }
    .footer a { color: var(--muted) }
    .deeper { margin-top: 44px }
    .deeper h2 { margin-bottom: 6px; font-size: 1.3rem }
    .deeper > p { margin: 0 0 16px; color: var(--muted) }
    .quick { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1px; overflow: hidden; border: 1px solid var(--line); border-radius: 8px; background: var(--line) }
    .quick a { display: grid; min-height: 96px; grid-template-columns: 52px 1fr; gap: 15px; align-items: center; padding: 16px 20px; background: var(--surface); color: var(--ink); text-decoration: none }
    .quick a:last-child:nth-child(odd) { grid-column: 1 / -1 }
    .quick a:hover { background: var(--soft) }
    .quick .code { display: grid; width: 52px; height: 44px; place-items: center; border-radius: 7px; background: var(--mint); color: var(--green2); font: 800 .7rem Manrope, sans-serif }
    .quick strong { display: block; font-family: Manrope, sans-serif }
    .quick small { display: block; color: var(--muted); font-size: .86rem; line-height: 1.45 }
    kbd { padding: 1px 6px; border: 1px solid var(--line); border-bottom-width: 2px; border-radius: 4px; background: var(--surface); font: .8em monospace }

    @media (max-width: 900px) {
      .needs { grid-template-columns: repeat(3, minmax(0, 1fr)) }
      .layout { grid-template-columns: 1fr; gap: 12px; padding-top: 20px }
      .sidebar { position: static; max-height: none; overflow: visible }
      .sidebar h2, .topics { display: none }
      .topic-select { display: flex }
    }
    @media (max-width: 680px) {
      .shell { width: calc(100% - 28px) }
      .links { display: none }
      .theme { margin-left: auto }
      .hero { padding: 36px 0 28px }
      .needs { grid-template-columns: repeat(2, minmax(0, 1fr)) }
      .need { min-height: 96px; padding: 14px }
      .quick { grid-template-columns: 1fr }
      .qa summary { padding: 14px; font-size: 1rem }
      .answer { padding-inline: 14px }
      .kbd-hint { display: none }
    }
    @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto } .qa { transition: none } }
"""

SCRIPT = """
    document.addEventListener('DOMContentLoaded', () => {
      if (window.lucide) lucide.createIcons();
      document.getElementById('theme').addEventListener('click', () => window.MiroTalkTheme.toggle());

      const heroInput = document.getElementById('search');
      const stickyInput = document.getElementById('search-sticky');
      const stickyBar = document.getElementById('stickybar');
      const stickyCount = document.getElementById('sticky-count');
      const clear = document.getElementById('clear');
      const sectionsBox = document.getElementById('sections');
      const sections = [...document.querySelectorAll('.faq-section')];
      const items = [...document.querySelectorAll('.qa')];
      const topics = [...document.querySelectorAll('.topic, .need')];
      const topicSelect = document.getElementById('topic-select');
      const status = document.getElementById('count');
      const empty = document.getElementById('empty');
      const emptyQuery = document.getElementById('empty-query');
      const toTop = document.getElementById('to-top');
      let activeSection = 'all';

      const escapeHtml = (text) => text.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
      const escapePattern = (text) => text.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
      const highlightHtml = (text, terms) => {
        if (!terms.length) return escapeHtml(text);
        const pattern = new RegExp(`(${terms.map(escapePattern).join('|')})`, 'gi');
        return text.split(pattern).map((part, i) => (i % 2 ? `<mark>${escapeHtml(part)}</mark>` : escapeHtml(part))).join('');
      };

      const data = new Map(items.map((item, position) => {
        const title = item.querySelector('.q').dataset.text;
        const body = [...item.querySelector('.answer').children]
          .filter((element) => !element.classList.contains('answer-foot'))
          .map((element) => element.textContent).join(' ').replace(/\\s+/g, ' ').trim();
        return [item, { title, titleLower: title.toLowerCase(), body, bodyLower: body.toLowerCase(), position }];
      }));

      const snippetFor = (entry, terms) => {
        const hit = terms.map((term) => entry.bodyLower.indexOf(term)).filter((i) => i >= 0).sort((a, b) => a - b)[0];
        if (hit === undefined) return '';
        let start = Math.max(0, hit - 50);
        let end = Math.min(entry.body.length, hit + 110);
        // Snap to word boundaries so the excerpt does not start or end mid-word.
        if (start > 0) start = Math.min(entry.body.indexOf(' ', start) + 1 || start, hit);
        if (end < entry.body.length) end = Math.max(entry.body.lastIndexOf(' ', end) || end, hit + 1);
        return `${start > 0 ? '… ' : ''}${highlightHtml(entry.body.slice(start, end), terms)}${end < entry.body.length ? ' …' : ''}`;
      };

      const apply = (searchChanged = false) => {
        const raw = heroInput.value.trim();
        const terms = raw.toLowerCase().split(/\\s+/).filter(Boolean);
        const perSection = new Map(sections.map((section) => [section.dataset.section, 0]));
        const scores = new Map();
        let visible = 0;

        items.forEach((item) => {
          const entry = data.get(item);
          const section = item.closest('.faq-section').dataset.section;
          const matches = terms.every((term) => entry.titleLower.includes(term) || entry.bodyLower.includes(term));
          if (matches) {
            perSection.set(section, perSection.get(section) + 1);
            scores.set(item, terms.reduce((sum, term) => sum + (entry.titleLower.includes(term) ? 10 : 0) + (entry.bodyLower.includes(term) ? 1 : 0), 0));
          }
          const shown = matches && (activeSection === 'all' || section === activeSection);
          item.hidden = !shown;
          if (!shown) return;
          visible += 1;
          item.querySelector('.q').innerHTML = highlightHtml(entry.title, terms);
          const snippet = item.querySelector('.snippet');
          const bodyOnly = terms.length && !terms.every((term) => entry.titleLower.includes(term));
          snippet.innerHTML = bodyOnly ? snippetFor(entry, terms) : '';
          snippet.hidden = !snippet.innerHTML;
        });

        // Best matches first, without moving DOM nodes (CSS order on flex columns).
        const ranked = items.filter((item) => !item.hidden).sort((a, b) => (scores.get(b) || 0) - (scores.get(a) || 0) || data.get(a).position - data.get(b).position);
        items.forEach((item) => { item.style.order = terms.length ? String(ranked.indexOf(item)) : ''; });
        sections.forEach((section) => {
          const visibleItems = [...section.querySelectorAll('.qa:not([hidden])')];
          section.hidden = visibleItems.length === 0;
          section.style.order = terms.length && visibleItems.length ? String(Math.min(...visibleItems.map((item) => ranked.indexOf(item)))) : '';
        });

        const matchTotal = [...perSection.values()].reduce((sum, n) => sum + n, 0);
        topics.forEach((topic) => {
          const count = topic.dataset.section === 'all' ? matchTotal : perSection.get(topic.dataset.section);
          topic.querySelector('.num').textContent = topic.dataset.section === 'all' ? '' : count;
          topic.classList.toggle('zero', count === 0);
        });
        [...topicSelect.options].forEach((option) => {
          option.textContent = option.value === 'all' ? `All topics (${matchTotal})` : `${option.dataset.name} (${perSection.get(option.value)})`;
        });
        topicSelect.value = activeSection;

        if (searchChanged && terms.length && visible > 0 && visible <= 3) {
          items.forEach((item) => { if (!item.hidden) item.open = true; });
        }

        const noun = visible === 1 ? 'question' : 'questions';
        status.textContent = raw ? `${visible} ${noun} found for “${raw}”` : `Showing ${visible} ${noun}`;
        stickyCount.textContent = raw ? `${visible} found` : '';
        emptyQuery.textContent = raw ? `No answers match “${raw}”` : 'No questions in this topic';
        empty.classList.toggle('visible', visible === 0);
        clear.classList.toggle('visible', raw.length > 0);

        const url = new URL(window.location.href);
        if (raw) url.searchParams.set('q', raw); else url.searchParams.delete('q');
        history.replaceState(null, '', url);
      };

      const setQuery = (value, searchChanged = true) => {
        heroInput.value = value;
        stickyInput.value = value;
        apply(searchChanged);
      };

      const setSection = (name) => {
        activeSection = name;
        topics.forEach((topic) => {
          const active = topic.dataset.section === name;
          topic.classList.toggle('active', active);
          topic.setAttribute('aria-pressed', String(active));
        });
        apply();
      };

      const openFromHash = () => {
        const id = decodeURIComponent(location.hash.slice(1));
        const item = id && document.getElementById(id);
        if (!item || !item.classList.contains('qa')) return;
        if (item.hidden) { setQuery('', false); setSection('all'); }
        item.open = true;
        item.scrollIntoView();
      };

      [heroInput, stickyInput].forEach((input) => {
        input.addEventListener('input', () => setQuery(input.value));
        input.addEventListener('keydown', (event) => { if (event.key === 'Escape') setQuery(''); });
      });
      clear.addEventListener('click', () => { setQuery('', false); heroInput.focus(); });
      topics.forEach((topic) => topic.addEventListener('click', () => {
        setSection(topic.dataset.section);
        if (topic.classList.contains('need')) document.getElementById('results').scrollIntoView();
      }));
      topicSelect.addEventListener('change', () => setSection(topicSelect.value));
      document.getElementById('expand').addEventListener('click', () => items.forEach((item) => { item.open = !item.hidden; }));
      document.getElementById('collapse').addEventListener('click', () => items.forEach((item) => { item.open = false; }));
      document.getElementById('reset').addEventListener('click', () => { setQuery('', false); setSection('all'); heroInput.focus(); });
      window.addEventListener('hashchange', openFromHash);

      document.querySelectorAll('.copy').forEach((button) => button.addEventListener('click', async () => {
        const url = `${location.origin}${location.pathname}#${button.dataset.id}`;
        const label = button.querySelector('span');
        try { await navigator.clipboard.writeText(url); label.textContent = 'Link copied'; } catch { label.textContent = 'Press Ctrl+C'; }
        setTimeout(() => { label.textContent = 'Copy link'; }, 1800);
      }));

      // Show a compact search bar once the main search box has scrolled out of view.
      new IntersectionObserver(([entry]) => { stickyBar.hidden = entry.isIntersecting; }, { rootMargin: '-68px 0px 0px 0px' })
        .observe(document.querySelector('.hero .searchbox'));

      window.addEventListener('scroll', () => toTop.classList.toggle('visible', window.scrollY > 900), { passive: true });
      toTop.addEventListener('click', () => window.scrollTo({ top: 0 }));
      document.addEventListener('keydown', (event) => {
        const typing = ['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName);
        if (event.key === '/' && !typing && !event.metaKey && !event.ctrlKey) {
          event.preventDefault();
          (stickyBar.hidden ? heroInput : stickyInput).focus();
        }
      });

      setQuery(new URLSearchParams(location.search).get('q') || '');
      openFromHash();
    });
"""


def build_page(
    title: str, topics: str, body: str, popular: str, options: str, total: int, squares: str, deeper: str
) -> str:
    safe_title = escape(TITLE, quote=True)
    safe_description = escape(DESCRIPTION, quote=True)
    heading = escape(title)
    return f"""<!doctype html>
<!-- Generated by scripts/build_faq_page.py from docs/faq/index.md. Do not edit by hand. -->
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{safe_description}">
  <meta name="robots" content="noindex, follow">
  <meta name="theme-color" content="#f5f8f5">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="MiroTalk">
  <meta property="og:title" content="{safe_title}">
  <meta property="og:description" content="{safe_description}">
  <meta property="og:url" content="{PAGE_URL}">
  <meta property="og:image" content="https://docs.mirotalk.com/images/mirotalk-preview.png">
  <meta property="og:image:alt" content="MiroTalk video communication products">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{safe_title}">
  <meta name="twitter:description" content="{safe_description}">
  <meta name="twitter:image" content="https://docs.mirotalk.com/images/mirotalk-preview.png">
  <link rel="canonical" href="{PAGE_URL}">
  <link rel="icon" href="../images/icon/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js" defer></script>
  <script src="../javascripts/product-theme.js"></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{safe_title}",
    "description": "{safe_description}",
    "url": "{PAGE_URL}",
    "image": "https://docs.mirotalk.com/images/mirotalk-preview.png",
    "isPartOf": {{ "@type": "WebSite", "name": "MiroTalk Documentation", "url": "https://docs.mirotalk.com/" }}
  }}
  </script>
  <title>{safe_title}</title>
  <style>{STYLE}  </style>
  <noscript><style>.searchbox, .popular, .chooser, .sidebar, .status .actions, .copy, .to-top, .theme {{ display: none }} .layout {{ grid-template-columns: 1fr }}</style></noscript>
</head>
<body>
  <header class="site-header">
    <nav class="shell" aria-label="Main navigation">
      <a class="brand" href="../"><span class="mark"><i data-lucide="video"></i></span>MiroTalk</a>
      <div class="links"><a href="../">Documentation</a><a href="../self-host/">Self-host</a><a href="../license/">Licensing</a><a href="../faq/">Classic FAQ</a></div>
      <button class="theme" id="theme" type="button" aria-label="Switch color theme" title="Switch color theme"><i class="moon" data-lucide="moon"></i><i class="sun" data-lucide="sun"></i></button>
    </nav>
  </header>
  <div class="stickybar" id="stickybar" role="search" aria-label="Search the FAQ" hidden>
    <div class="shell">
      <div class="searchbox">
        <i data-lucide="search"></i>
        <input class="search" id="search-sticky" type="search" placeholder="Search questions..." aria-label="Search questions" autocomplete="off">
        <span class="sticky-count" aria-hidden="true" id="sticky-count"></span>
      </div>
    </div>
  </div>
  <section class="hero" aria-labelledby="faq-title">
    <div class="shell">
      <span class="eyebrow">Help center</span>
      <h1 id="faq-title">{heading}</h1>
      <p class="lead">Quick answers about MiroTalk products, self-hosting, licensing, and troubleshooting.</p>
      <div class="searchbox">
        <i data-lucide="search"></i>
        <input class="search" id="search" type="search" placeholder="Search {total} questions..." aria-label="Search questions" autocomplete="off">
        <button class="clear" id="clear" type="button" aria-label="Clear search"><i data-lucide="x"></i></button>
      </div>
      <div class="popular"><span>Popular:</span>{popular}</div>
    </div>
  </section>
  <section class="chooser" aria-labelledby="topics-title">
    <div class="shell">
      <div class="intro"><span class="eyebrow">Browse by topic</span>
        <h2 id="topics-title">What do you need help with?</h2>
        <p>Pick a topic to filter the answers below, or search across everything.</p>
      </div>
      <div class="needs" role="group" aria-label="Filter questions by topic">
{squares}
      </div>
    </div>
  </section>
  <div class="shell layout" id="results">
    <aside class="sidebar" aria-label="Browse by topic">
      <h2>Browse by topic</h2>
      <div class="topics">{topics}</div>
      <label class="topic-select"><span>Topic</span><select id="topic-select" aria-label="Filter by topic">{options}</select></label>
    </aside>
    <main class="content">
      <div class="status">
        <span id="count" role="status" aria-live="polite">Showing {total} questions</span>
        <span class="actions"><button class="link-button" id="expand" type="button">Expand all</button><button class="link-button" id="collapse" type="button">Collapse all</button></span>
      </div>
<div class="sections" id="sections">
{body}
      </div>
      <div class="empty" id="empty"><strong id="empty-query">No answers found</strong>Try a shorter keyword or browse all topics.<br><button id="reset" type="button" class="link-button">Clear search and filters</button></div>
{deeper}
      <aside class="help">
        <div><h2>Can't find your answer?</h2><p>Ask the MiroTalk community or browse the full documentation.</p></div>
        <a class="button" href="{{{{ links.discord }}}}" target="_blank" rel="noopener noreferrer">Ask on Discord</a>
      </aside>
    </main>
  </div>
  <button class="to-top" id="to-top" type="button" aria-label="Back to top"><i data-lucide="arrow-up"></i></button>
  <footer><div class="shell footer"><p><strong>MiroTalk</strong><br>Open video communication, on your terms.</p><div><a href="../">Documentation</a><a href="../faq/">Classic FAQ</a><a href="../license/">Licensing</a></div></div></footer>
  <script>{SCRIPT}  </script>
</body>
</html>
"""


def generate() -> str:
    text = SOURCE.read_text(encoding="utf-8")
    title, sections = parse_faq(text)
    topics, body, popular, options, total = render_body(sections)
    return build_page(
        title, topics, body, popular, options, total, render_squares(sections),
        render_deeper(parse_deeper(text)),
    )


def write_page() -> bool:
    """Write the page if its content changed; return whether it was written."""
    page = generate()
    if OUTPUT.exists() and OUTPUT.read_text(encoding="utf-8") == page:
        return False
    OUTPUT.write_text(page, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="fail if the page is stale")
    args = parser.parse_args()

    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != generate():
            print(f"{OUTPUT.relative_to(ROOT)} is out of date. Run: python scripts/build_faq_page.py")
            return 1
        print(f"{OUTPUT.relative_to(ROOT)} is up to date.")
        return 0

    status = "Wrote" if write_page() else "Already up to date:"
    print(f"{status} {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
