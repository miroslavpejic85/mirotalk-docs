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


def render_body(sections: list[dict]) -> tuple[str, str, str, int]:
    topics = [
        '<button class="topic active" type="button" data-section="all" aria-pressed="true">'
        '<i data-lucide="layout-grid"></i><span class="name">All topics</span>'
        '<span class="num"></span></button>'
    ]
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
        items = []
        for question in section["questions"]:
            question_id = slugify(question["question"])
            if question_id in ids.values():
                raise ValueError(f"Duplicate question id: {question_id}")
            ids[question["question"]] = question_id
            text = escape(question["question"])
            items.append(
                f'<details class="qa" id="{question_id}">\n'
                f'<summary><span class="q" data-text="{text}">{text}</span></summary>\n'
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

    return "\n".join(topics), "\n".join(blocks), "\n".join(popular), total


STYLE = """
    :root {
      color-scheme: light;
      --ink: #17231f; --muted: #52635b; --paper: #f5f8f5; --surface: #fff;
      --soft: #eaf1ed; --line: #d5e0da; --green: #087f5b; --green-dark: #056347;
      --mint: #dff5eb; --mark: #fff0a8; --shadow: 0 12px 32px rgba(23,35,31,.1);
      --blue: #1565c0; --blue-soft: #e3f0fb; --accent-bg: #1565c0; --accent-fg: #fff
    }
    [data-theme="dark"] {
      color-scheme: dark;
      --ink: #edf5f1; --muted: #a9b9b1; --paper: #101714; --surface: #17201c;
      --soft: #202b26; --line: #34443c; --green: #61d6aa; --green-dark: #8ce5c3;
      --mint: #173c2f; --mark: #5c4b12; --shadow: 0 12px 32px rgba(0,0,0,.35);
      --blue: #7dbcf0; --blue-soft: #173247; --accent-bg: #7dbcf0; --accent-fg: #0d1a24
    }
    * { box-sizing: border-box }
    html { scroll-behavior: smooth; scroll-padding-top: 88px }
    body { margin: 0; color: var(--ink); font: 16px/1.65 'DM Sans', sans-serif; background: var(--paper) }
    a { color: var(--blue) } button, input { color: inherit; font: inherit }
    :focus-visible { outline: 3px solid var(--blue); outline-offset: 2px }
    [hidden] { display: none !important }
    svg { flex: none }
    .shell { width: min(1120px, calc(100% - 40px)); margin-inline: auto }
    .site-header { position: sticky; top: 0; z-index: 20; border-bottom: 1px solid var(--line); background: color-mix(in srgb, var(--paper) 92%, transparent); backdrop-filter: blur(16px) }
    nav { display: flex; min-height: 64px; gap: 24px; align-items: center }
    .brand { display: flex; gap: 10px; align-items: center; color: var(--ink); font: 800 1rem Manrope, sans-serif; text-decoration: none }
    .mark { display: grid; width: 34px; height: 34px; place-items: center; border-radius: 50%; background: var(--green-dark); color: var(--paper) }
    .mark svg, .theme svg { width: 19px; height: 19px }
    .links { display: flex; gap: 22px; margin-left: auto }
    .links a { color: var(--muted); font-size: .9rem; font-weight: 600; text-decoration: none }
    .links a:hover { color: var(--ink) }
    .theme { display: grid; width: 40px; height: 40px; padding: 0; place-items: center; border: 1px solid var(--line); border-radius: 7px; background: var(--surface); cursor: pointer }
    h1, h2 { margin-top: 0; font-family: Manrope, sans-serif; letter-spacing: 0 }

    .hero { padding: 44px 0 28px; border-bottom: 1px solid var(--line); background: linear-gradient(180deg, var(--mint), transparent) }
    .hero .shell { max-width: 760px; text-align: center }
    .eyebrow { margin: 0 0 8px; color: var(--green); font-size: .8rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase }
    h1 { margin-bottom: 10px; font-size: clamp(2rem, 5vw, 2.75rem); line-height: 1.1 }
    .lead { margin: 0 auto 22px; max-width: 54ch; color: var(--muted); font-size: 1.05rem }
    .searchbox { position: relative }
    .searchbox > svg { position: absolute; top: 50%; left: 18px; width: 20px; height: 20px; color: var(--muted); transform: translateY(-50%); pointer-events: none }
    .search { width: 100%; padding: 16px 48px 16px 50px; border: 2px solid var(--line); border-radius: 14px; background: var(--surface); font-size: 1.05rem; box-shadow: var(--shadow) }
    .search:focus { border-color: var(--blue); outline: none }
    .search::-webkit-search-cancel-button { display: none }
    .clear { position: absolute; top: 50%; right: 10px; display: none; width: 34px; height: 34px; padding: 0; place-items: center; border: 0; border-radius: 50%; background: var(--soft); cursor: pointer; transform: translateY(-50%) }
    .clear.visible { display: grid }
    .clear svg { width: 16px; height: 16px }
    .popular { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; justify-content: center; margin-top: 16px; color: var(--muted); font-size: .88rem }
    .popular a { padding: 4px 12px; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); color: var(--ink); font-weight: 600; text-decoration: none }
    .popular a:hover { border-color: var(--blue); color: var(--blue) }

    .layout { display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 40px; align-items: start; padding: 32px 0 64px }
    .sidebar { position: sticky; top: 88px; max-height: calc(100vh - 108px); overflow-y: auto }
    .sidebar h2 { margin: 0 0 8px 10px; color: var(--muted); font: 700 .75rem 'DM Sans', sans-serif; letter-spacing: .08em; text-transform: uppercase }
    .topics { display: flex; flex-direction: column; gap: 2px }
    .topic { display: flex; gap: 10px; align-items: center; padding: 8px 10px; border: 0; border-radius: 8px; background: none; font-size: .92rem; font-weight: 500; text-align: left; cursor: pointer }
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
    .link-button:hover { border-color: var(--blue); color: var(--blue) }
    .faq-section { margin-top: 28px }
    .faq-section h2 { display: flex; gap: 12px; align-items: center; margin-bottom: 14px; font-size: 1.3rem }
    .faq-section h2 .icon { display: grid; width: 34px; height: 34px; place-items: center; border-radius: 9px; background: var(--blue-soft); color: var(--blue) }
    .faq-section h2 svg { width: 18px; height: 18px }
    .qa { margin-bottom: 10px; border: 1px solid var(--line); border-left: 4px solid var(--line); border-radius: 10px; background: var(--surface); transition: border-color .15s }
    .qa:hover { border-left-color: var(--blue) }
    .qa[open] { border-left-color: var(--blue); box-shadow: var(--shadow) }
    .qa summary { display: flex; gap: 16px; align-items: center; justify-content: space-between; padding: 16px 18px; font-size: 1.04rem; font-weight: 600; line-height: 1.4; cursor: pointer; list-style: none }
    .qa summary::-webkit-details-marker { display: none }
    .qa summary::after { flex: none; width: 24px; height: 24px; border-radius: 50%; background: var(--soft) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%231565c0' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M12 6v12M6 12h12'/%3E%3C/svg%3E") center/14px no-repeat; content: '' }
    .qa[open] summary::after { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%231565c0' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E") }
    [data-theme="dark"] .qa summary::after { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%237dbcf0' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M12 6v12M6 12h12'/%3E%3C/svg%3E") }
    [data-theme="dark"] .qa[open] summary::after { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%237dbcf0' stroke-width='3' stroke-linecap='round'%3E%3Cpath d='M6 12h12'/%3E%3C/svg%3E") }
    .qa:target { scroll-margin-top: 88px }
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
    .help { display: flex; flex-wrap: wrap; gap: 16px; align-items: center; justify-content: space-between; margin-top: 44px; padding: 24px; border-radius: 12px; background: var(--blue-soft) }
    .help h2 { margin-bottom: 4px; font-size: 1.2rem }
    .help p { margin: 0; color: var(--muted) }
    .button { display: inline-block; padding: 10px 18px; border-radius: 8px; background: var(--accent-bg); color: var(--accent-fg); font-weight: 700; text-decoration: none }
    .button:hover { opacity: .9 }
    .to-top { position: fixed; right: 20px; bottom: 20px; z-index: 15; display: none; width: 44px; height: 44px; padding: 0; place-items: center; border: 1px solid var(--line); border-radius: 50%; background: var(--surface); box-shadow: var(--shadow); cursor: pointer }
    .to-top.visible { display: grid }
    .to-top svg { width: 20px; height: 20px }
    footer { border-top: 1px solid var(--line); background: var(--surface) }
    .footer { display: flex; min-height: 110px; gap: 24px; align-items: center; justify-content: space-between; color: var(--muted); font-size: .82rem }
    .footer p { margin: 0 }
    .footer div { display: flex; flex-wrap: wrap; gap: 18px }
    .footer a { color: var(--muted) }
    kbd { padding: 1px 6px; border: 1px solid var(--line); border-bottom-width: 2px; border-radius: 4px; background: var(--surface); font: .8em monospace }

    @media (max-width: 900px) {
      .layout { grid-template-columns: 1fr; gap: 12px; padding-top: 20px }
      .sidebar { position: static; max-height: none; margin-inline: -14px; padding: 0 14px 6px; overflow-x: auto }
      .sidebar h2 { display: none }
      .sidebar { scrollbar-width: none }
      .topics { flex-direction: row; gap: 8px; width: max-content }
      .topic { padding: 6px 12px; border: 1px solid var(--line); border-radius: 999px; background: var(--surface); white-space: nowrap }
      .topic .num:empty { display: none }
    }
    @media (max-width: 680px) {
      .shell { width: calc(100% - 28px) }
      .links { display: none }
      .theme { margin-left: auto }
      .hero { padding: 28px 0 22px }
      .qa summary { padding: 14px; font-size: 1rem }
      .answer { padding-inline: 14px }
      .kbd-hint { display: none }
    }
    @media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto } .qa { transition: none } }
"""

SCRIPT = """
    document.addEventListener('DOMContentLoaded', () => {
      const refreshIcons = () => window.lucide && lucide.createIcons();
      refreshIcons();
      document.getElementById('theme').addEventListener('click', () => window.MiroTalkTheme.toggle());

      const input = document.getElementById('search');
      const clear = document.getElementById('clear');
      const sections = [...document.querySelectorAll('.faq-section')];
      const items = [...document.querySelectorAll('.qa')];
      const topics = [...document.querySelectorAll('.topic')];
      const status = document.getElementById('count');
      const empty = document.getElementById('empty');
      const emptyQuery = document.getElementById('empty-query');
      const toTop = document.getElementById('to-top');
      const index = new Map(items.map((item) => [item, item.textContent.toLowerCase()]));
      const escapeHtml = (text) => text.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
      const escapePattern = (text) => text.replace(/[.*+?^${}()|[\\]\\\\]/g, '\\\\$&');
      let activeSection = 'all';

      const highlight = (item, terms) => {
        const label = item.querySelector('.q');
        const text = label.dataset.text;
        const unescaped = new DOMParser().parseFromString(text, 'text/html').body.textContent;
        if (!terms.length) { label.textContent = unescaped; return; }
        const pattern = new RegExp(`(${terms.map(escapePattern).join('|')})`, 'gi');
        label.innerHTML = unescaped.split(pattern).map((part, i) => (i % 2 ? `<mark>${escapeHtml(part)}</mark>` : escapeHtml(part))).join('');
      };

      const apply = (searchChanged = false) => {
        const raw = input.value.trim();
        const terms = raw.toLowerCase().split(/\\s+/).filter(Boolean);
        const perSection = new Map(sections.map((section) => [section.dataset.section, 0]));
        let visible = 0;

        items.forEach((item) => {
          const section = item.closest('.faq-section').dataset.section;
          const matches = terms.every((term) => index.get(item).includes(term));
          if (matches) perSection.set(section, perSection.get(section) + 1);
          const shown = matches && (activeSection === 'all' || section === activeSection);
          item.hidden = !shown;
          if (shown) { visible += 1; highlight(item, terms); }
        });

        sections.forEach((section) => { section.hidden = !section.querySelector('.qa:not([hidden])'); });

        const matchTotal = [...perSection.values()].reduce((sum, n) => sum + n, 0);
        topics.forEach((topic) => {
          const count = topic.dataset.section === 'all' ? matchTotal : perSection.get(topic.dataset.section);
          topic.querySelector('.num').textContent = topic.dataset.section === 'all' ? '' : count;
          topic.classList.toggle('zero', count === 0);
        });

        if (searchChanged && terms.length && visible > 0 && visible <= 3) {
          items.forEach((item) => { if (!item.hidden) item.open = true; });
        }

        const noun = visible === 1 ? 'question' : 'questions';
        status.textContent = raw ? `${visible} ${noun} found for “${raw}”` : `Showing ${visible} ${noun}`;
        emptyQuery.textContent = raw ? `No answers match “${raw}”` : 'No questions in this topic';
        empty.classList.toggle('visible', visible === 0);
        clear.classList.toggle('visible', raw.length > 0);

        const url = new URL(window.location.href);
        if (raw) url.searchParams.set('q', raw); else url.searchParams.delete('q');
        history.replaceState(null, '', url);
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
        if (item.hidden) { input.value = ''; activeSection = 'all'; setSection('all'); }
        item.open = true;
        item.scrollIntoView();
      };

      input.addEventListener('input', () => apply(true));
      clear.addEventListener('click', () => { input.value = ''; apply(); input.focus(); });
      topics.forEach((topic) => topic.addEventListener('click', () => setSection(topic.dataset.section)));
      document.getElementById('expand').addEventListener('click', () => items.forEach((item) => { item.open = !item.hidden; }));
      document.getElementById('collapse').addEventListener('click', () => items.forEach((item) => { item.open = false; }));
      document.getElementById('reset').addEventListener('click', () => { input.value = ''; setSection('all'); input.focus(); });
      window.addEventListener('hashchange', openFromHash);

      document.querySelectorAll('.copy').forEach((button) => button.addEventListener('click', async () => {
        const url = `${location.origin}${location.pathname}#${button.dataset.id}`;
        const label = button.querySelector('span');
        try { await navigator.clipboard.writeText(url); label.textContent = 'Link copied'; } catch { label.textContent = 'Press Ctrl+C'; }
        setTimeout(() => { label.textContent = 'Copy link'; }, 1800);
      }));

      window.addEventListener('scroll', () => toTop.classList.toggle('visible', window.scrollY > 900), { passive: true });
      toTop.addEventListener('click', () => window.scrollTo({ top: 0 }));
      document.addEventListener('keydown', (event) => {
        const typing = ['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName);
        if (event.key === '/' && !typing && !event.metaKey && !event.ctrlKey) { event.preventDefault(); input.focus(); }
        if (event.key === 'Escape' && document.activeElement === input) { input.value = ''; apply(); }
      });

      input.value = new URLSearchParams(location.search).get('q') || '';
      apply(true);
      openFromHash();
    });
"""


def build_page(title: str, topics: str, body: str, popular: str, total: int) -> str:
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
</head>
<body>
  <header class="site-header">
    <nav class="shell" aria-label="Main navigation">
      <a class="brand" href="../"><span class="mark"><i data-lucide="video"></i></span>MiroTalk</a>
      <div class="links"><a href="../">Documentation</a><a href="../self-host/">Self-host</a><a href="../license/">Licensing</a><a href="../faq/">Classic FAQ</a></div>
      <button class="theme" id="theme" type="button" aria-label="Toggle color theme"><i data-lucide="sun-moon"></i></button>
    </nav>
  </header>
  <section class="hero">
    <div class="shell">
      <p class="eyebrow">Help center</p>
      <h1>{heading}</h1>
      <p class="lead">Quick answers about MiroTalk products, self-hosting, licensing, and troubleshooting.</p>
      <div class="searchbox">
        <i data-lucide="search"></i>
        <input class="search" id="search" type="search" placeholder="Search {total} questions..." aria-label="Search questions" autocomplete="off">
        <button class="clear" id="clear" type="button" aria-label="Clear search"><i data-lucide="x"></i></button>
      </div>
      <div class="popular"><span>Popular:</span>{popular}</div>
    </div>
  </section>
  <div class="shell layout">
    <aside class="sidebar" aria-label="Browse by topic">
      <h2>Browse by topic</h2>
      <div class="topics">{topics}</div>
    </aside>
    <main class="content">
      <div class="status">
        <span id="count" role="status" aria-live="polite">Showing {total} questions</span>
        <span class="actions"><button class="link-button" id="expand" type="button">Expand all</button><button class="link-button" id="collapse" type="button">Collapse all</button></span>
      </div>
{body}
      <div class="empty" id="empty"><strong id="empty-query">No answers found</strong>Try a shorter keyword or browse all topics.<br><button id="reset" type="button" class="link-button">Clear search and filters</button></div>
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
    title, sections = parse_faq(SOURCE.read_text(encoding="utf-8"))
    topics, body, popular, total = render_body(sections)
    return build_page(title, topics, body, popular, total)


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
