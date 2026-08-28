# Redesign implementation status

Status date: 2026-08-27

## Completed

- Phase A: page inventory, IA, product positioning, SEO, conversion, accessibility, and release audit.
- Phase B: journey navigation, URL preservation, source coverage invariant, pinned dependencies, and CI.
- Phase C: shared MkDocs shell, responsive homepage and chooser, product/editorial Markdown migration, accessible contrast, and navigation landmarks.
- Phase D: Cloud, self-host, developer, commercial, licensing, demo, GitHub, and enterprise paths.
- Phase E repository scope: unique titles, descriptions, canonicals and H1s; OpenGraph/Twitter/schema metadata; sitemap coverage; redirect registry; internal and external link checks.
- Phase F repository scope: vendor-neutral CTA event taxonomy with approved non-personal fields and automated classification tests.
- Phase G local automation: strict build, navigation coverage, metadata uniqueness, internal links/assets, external links, responsive overflow, runtime errors, and axe serious/critical/moderate checks.
- API normalization: all six REST API guides retitled and linked to verified deployed Swagger contracts; default-looking secrets replaced with explicit placeholders.

## Production decisions required

These items cannot be completed safely from the documentation repository alone:

1. Approve the exact licensing language with the legal/commercial owner.
2. Select the analytics platform, consent behavior, privacy notice, retention period, and cross-domain attribution policy.
3. Identify the production edge/server repository and replace the legacy licensing HTML redirect with a real one-hop `301`.
4. Approve affiliate disclosure requirements for hosting and sponsored links.
5. Deploy to staging and production with owner approval and rollback access.

No analytics vendor, cookies, browser storage, or network transmission has been added. The site emits only the local `mirotalk:analytics` browser event; an approved adapter may consume it after the privacy decisions above.

## Validation commands

```bash
python scripts/check_nav_coverage.py
python -m mkdocs build --strict
python scripts/check_site_metadata.py
python scripts/check_internal_links.py
python scripts/check_external_links.py
node scripts/check_analytics_events.js
git diff --check
```

The external-link command treats confirmed HTTP `404` and `410` responses as failures and reports timeouts or access-controlled services separately.

## Latest results

- Navigation: 110 published sources exactly once; one legacy redirect allowlisted.
- Metadata: 86 content pages valid with unique title, description, canonical URL, and one H1; one legacy redirect exempt.
- Internal references: 12,052 links and assets validated across 88 generated HTML pages.
- External references: 128 checked; no confirmed `404` or `410`; two third-party timeouts (`icetest.info` and GNU licensing).
- Analytics: eight event classifications and the approved payload field allowlist validated.
- Browser QA: 52 route/viewport checks across 320, 390, 768, and 1440 px; zero overflow, runtime, H1, or HTTP failures.
- Accessibility: 26 axe runs across mobile and desktop; zero moderate, serious, or critical violations in the tested routes.
- Lighthouse SFU API mobile: accessibility `1.00`, best practices `1.00`, and SEO `1.00`; zero color-contrast failures.
- Lighthouse SFU API performance baseline: `0.41`. The main opportunities are unused theme CSS (`107 KiB`) and JavaScript (`55 KiB`) under mobile throttling; optimization is deferred because removing shared Material assets or splitting the API guide would change the site-wide theme or documentation structure.