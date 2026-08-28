# MiroTalk Documentation Phase A Audit

Audit date: 2026-08-27  
Source revision: `12f6f94` (`main`)  
Deployed site: <https://docs.mirotalk.com/>  
Framework: MkDocs 1.6.1 with Material for MkDocs 9.7.7

## Scope and method

This is an audit-only deliverable. No documentation content, navigation, URL, or production behavior was changed.

Evidence used:

- repository source, including `mkdocs.yml`, 67 Markdown pages, 14 standalone HTML pages, 24 published shell scripts, 72 image/media assets, hooks, theme override, and custom CSS;
- a strict local production build;
- generated HTML inspection across 82 pages, including the generated 404 page;
- live homepage inspection at desktop and 390 x 844 mobile viewport;
- live `robots.txt` and `sitemap.xml` inspection;
- source-wide searches for metadata, analytics, redirects, links, APIs, GitHub, CodeCanyon, and conversion paths.

The detailed page-level disposition and proposed URL ownership map are in [PAGE_INVENTORY.md](PAGE_INVENTORY.md).

## Executive summary

The documentation has broad and valuable technical coverage. The corpus includes all major products, API examples, integration and direct-join guides, webhooks, configuration, deployment, scaling, rebranding, updates, SaaS/Stripe, Coturn, Docker, Whisper, Cloudron, scripts, licensing, demos, GitHub links, and CodeCanyon links. This content should be preserved.

The main problem is discovery, not absence. Navigation is organized by internal product codes and repeated page labels (`about`, `api`, `configurations`, `self-hosting`) rather than user goals. The homepage partially addresses discovery, but the requested Cloud, developer, self-hosting, and commercial paths are not yet first-class navigation concepts.

The largest measurable SEO issue is metadata duplication. Ten page-title groups are duplicated across product guides, 67 generated pages share the global fallback description, 11 standalone pages have no description, and 12 content pages have no canonical URL. Existing URLs are short and established, so the safest redesign is to preserve them and change navigation ownership first.

MiroTalk WEB is presented as both a product and the managed service. The requested strategy introduces MiroTalk Cloud as the managed product name. That naming relationship must be approved before implementation to avoid implying that WEB and Cloud are separate products or silently renaming a paid service.

## Baseline inventory

| Surface | Count | Assessment |
| --- | ---: | --- |
| Markdown pages | 67 | Core technical corpus; preserve and improve incrementally |
| Standalone HTML pages | 14 | Valuable product/commercial content, but inconsistent with the docs shell |
| Generated HTML pages | 82 | Includes 404; strict build passes |
| Published shell scripts | 24 | Important installation/update endpoints; preserve exact URLs |
| Image/media assets | 72 | Reuse after alt text, size, and format review |
| API guides | 6 | Existing endpoints and examples; normalize structure against product source |
| Named API endpoint sections | 19 | Across BRO, C2C, CME, P2P, and SFU; WEB delegates to Swagger only |
| Integration guides | 7 | Strong embedding base; consolidate developer discovery |
| Webhook guides | 3 | P2P, SFU, and CME only; do not imply support elsewhere |
| Product landing pages | 7 | Admin, BRO, C2C, CME, P2P, SFU, WEB |
| Analytics implementations | 0 | No tracking library or event system found |
| Redirect mechanisms | 1 | One HTML redirect from `/license/licensing-options/` to `/license/` |

## What works today

### Technical breadth

- Each primary product has an overview and most have API, configuration, integration, direct-join, ngrok, and self-hosting coverage.
- SFU additionally covers RTMP, scalability, host protection, rebranding, updates, and webhooks.
- P2P additionally covers host protection, rebranding, updates, and webhooks.
- CME includes internationalization and webhooks.
- WEB includes SaaS billing with Stripe.
- Shared infrastructure topics include Coturn, Docker Compose, NVM, FTP, update workflows, Whisper, Cloudron, and Ubuntu automation scripts.
- API pages link to deployed Swagger interfaces and include language examples.

Current prose API coverage is uneven: BRO has 1 named endpoint section, C2C has 2, CME has 5, P2P has 5, and SFU has 6. WEB contains only a Swagger link. These counts describe documentation sections, not a verified endpoint inventory; product repositories and OpenAPI documents remain the authority.

### Existing discovery and conversion foundations

- The homepage includes product selection, integration, self-hosting, licensing, live demos, and a managed WEB section.
- Product overview and project chooser pages already contain substantial comparison content.
- GitHub, CodePen, live demo, Stripe, CodeCanyon, Discord, hosting, and commercial links are present throughout the corpus.
- CodeCanyon is an active commercial distribution channel and should remain visible.

### SEO and platform foundations

- The homepage has a unique title, description, H1, canonical URL, OpenGraph/Twitter metadata, and organization/site/item-list schema.
- MkDocs pages receive canonical URLs and social metadata from the Material override.
- `robots.txt` allows crawling and points to the sitemap.
- A post-build hook adds standalone HTML pages to the sitemap.
- `use_directory_urls` gives stable, readable paths.

### UX, mobile, and accessibility foundations

- Material search is present and has an accessible label.
- Code-copy controls are enabled.
- The live homepage had no page-level horizontal overflow at 390 px.
- Homepage tables and code blocks remain contained at the tested mobile width.
- Theme switching, focusable controls, semantic main content, and back-to-top behavior are present.

## Findings and risks

### P0: source-of-truth and legal approval

1. Licensing language is inconsistent across surfaces. The homepage says AGPLv3 applies when source remains public; the standalone About page uses broader phrases such as "public, non-commercial use" and "without AGPL obligations." Legal meaning must come from the approved licensing page and counsel-approved copy, not a redesign interpretation.
2. The Cloud naming model is undefined in source. Current copy calls hosted WEB a managed service; the brief calls for MiroTalk Cloud. Approve whether Cloud is the commercial name for hosted WEB, a suite, or a separate offer before changing user-facing terminology.
3. API accuracy cannot be certified from this repository alone. Endpoint documentation must be checked against each product repository and deployed Swagger specification before examples are rewritten.

### P1: information architecture and discovery

1. Top-level navigation is implementation-centric and long. Users must understand SFU, P2P, C2C, BRO, CME, WEB, and ADMIN before choosing a task.
2. Repeated labels such as `about`, `api`, `configurations`, and `self-hosting` are ambiguous in navigation and search results.
3. The requested four journeys are not navigation owners: Use MiroTalk, Build with MiroTalk, Self-host MiroTalk, and Commercial & Enterprise.
4. MiroTalk Cloud has no dedicated documentation section for accounts, workspaces, meetings, rooms, scheduling, recording, or administration.
5. Enterprise, dedicated infrastructure, support, custom development, and deployment services do not have a coherent lead-generation destination.
6. Product discovery is split among the homepage, `/overview/`, `/projects/`, and `/about/`, with overlapping goals and separate visual systems.

### P1: SEO

1. Duplicate generated titles affect 10 groups: self-hosting, API, configurations, integration, join-room, ngrok, webhook, host-protection, rebranding, and updates.
2. Sixty-seven generated pages use the same fallback meta description.
3. Eleven standalone pages lack a meta description.
4. Twelve content pages lack a canonical link because standalone HTML bypasses the MkDocs override.
5. Standalone HTML pages have uneven OpenGraph and Twitter metadata.
6. Sitemap `lastmod` values derive from local file modification time/build context, not Git history or verified content updates; on the deployed audit date all entries appeared current, reducing signal quality.
7. No breadcrumb schema or documentation-specific structured data was found.
8. No redirect map exists for future IA changes. Preserving current URLs avoids this risk in Phase B.

### P1: conversion and analytics

1. No analytics implementation was found. Current commercial intent cannot be attributed to source page or journey.
2. CTA wording and destination are inconsistent: WEB managed service, license page, CodeCanyon user page, individual CodeCanyon items, Stripe checkout, and product demos all compete.
3. There is no stable event taxonomy or campaign parameter convention.
4. Self-hosting and deployment guides do not consistently offer a managed alternative.
5. API and integration guides do not consistently offer commercial licensing or developer contact paths.
6. Enterprise contact is not a first-class conversion endpoint.

### P1: content quality and API documentation

1. Technical guides do not consistently follow Goal, Prerequisites, Installation, Configuration, Example, Expected result, Troubleshooting, and Related documentation.
2. API guides often link to Swagger and provide several language examples, but do not consistently state method, endpoint, auth, parameters, request schema, response schema, status codes, and errors together.
3. API examples use default-looking secrets. Even when documented as examples, use explicit placeholders to reduce accidental insecure deployments.
4. A malformed CME Swagger target appears in source: `https:/cme.mirotalk.com/api/v1/docs`.
5. The Admin quick-start page links to the obsolete-looking `/html/overview/` route.
6. The README self-hosting link points to `docs/docs/self-hosting.md`, which does not exist.
7. Affiliate hosting links are mixed into prerequisites. They should be disclosed and separated from minimum technical requirements.
8. A full built-site crawl confirms `/html/overview/` returns 404. Placeholder domains and localhost examples also register as unreachable and need an explicit checker allowlist rather than being silently ignored.

### P2: search

1. Search uses the standard Material client-side index with no explicit search configuration, synonyms, ranking controls, or result categories.
2. Generic page titles weaken result quality because many hits display as only `api`, `integration`, or `self-hosting`.
3. Standalone HTML content may not have the same search indexing behavior as Markdown pages and should be tested page by page after consolidation.
4. Search intent terms from the brief should be represented naturally in titles and introductions: WebRTC, Docker, authentication, Stripe, recording, scaling, integrations, and troubleshooting.

### P2: design, accessibility, performance, and maintainability

1. Fourteen standalone HTML pages bypass the shared MkDocs shell and several embed large inline CSS/JS payloads. This creates inconsistent navigation, search, metadata, theme behavior, and maintenance.
2. Standalone pages independently load Google Fonts and Font Awesome; this increases requests and visual inconsistency.
3. The docs theme uses Roboto while standalone surfaces use Inter, DM Sans, Manrope, and IBM Plex Mono.
4. Raw product pages need keyboard, focus, landmark, heading, alt-text, reduced-motion, and contrast audits. Source inspection alone is insufficient.
5. The homepage contains 184 internal links in the rendered DOM, largely because the full navigation tree is repeated; this raises scanning cost.
6. No automated accessibility, broken-link, metadata, Lighthouse, or visual-regression workflow exists in the repository.
7. Dependencies are unpinned and there is no CI workflow. Reproducibility currently depends on ambient tool versions.
8. The source contains 181 Markdown/HTML image references. Many Markdown alt labels are implementation names such as `api`, `settings`, `ngrok`, and `nodejs`, which do not communicate image purpose. Decorative images should remain empty; informative images need contextual alternatives.
9. Several standalone commercial images are hosted on third-party image infrastructure. Availability, privacy, caching, intrinsic dimensions, and ownership should be reviewed before relying on them for primary product evidence.

## Proposed information architecture

Keep current URLs in Phase B. Reassign them under four task-oriented navigation groups and add only the missing overview pages.

### Use MiroTalk

- Cloud overview: new canonical page explaining the managed product and its relationship to WEB.
- Getting started: accounts, workspace, meetings, rooms, scheduling, recording, and administration.
- Product chooser: retain `/projects/` as the task-based chooser.
- Demos and FAQ: retain existing demos and `/faq/`.
- Primary CTA: Start MiroTalk Cloud.

### Build with MiroTalk

- Developer overview: new index that routes by integration goal and product.
- REST APIs: retain all six current API URLs.
- Embedding and iframe: retain all integration URLs and `/utility/quick-custom-integration/`.
- Direct join: retain all current join-room URLs.
- Webhooks: retain P2P, SFU, and CME webhook URLs.
- Authentication and examples: organize existing product-specific material without inventing shared behavior.
- Primary CTA: Build with MiroTalk. Secondary CTA: Commercial License.

### Self-host MiroTalk

- Self-hosting overview: new index linking architecture choice to each existing product guide.
- Deployment: retain product guides, Ubuntu scripts, Cloudron, Docker Compose, Nginx, SSL, Node.js, MongoDB, Coturn, and ngrok content.
- Operate: configuration, updates, scalability, monitoring, backups, and troubleshooting.
- Primary CTA: Self-host MiroTalk. Secondary CTA: Try MiroTalk Cloud.

### Commercial & Enterprise

- Licensing: retain `/license/` as the approved legal/commercial source.
- Ultimate: retain `/mirotalk-ultimate/` and CodeCanyon as an additional channel.
- Enterprise: new page for white-label, dedicated infrastructure, support, custom development, and deployment services using verified claims only.
- Primary CTA: Contact MiroTalk.

## Product naming recommendation

Use three user-facing choices consistently after approval:

| Choice | Meaning | Supporting product detail |
| --- | --- | --- |
| Use it | MiroTalk Cloud: managed service operated by MiroTalk | State whether this is powered by MiroTalk WEB |
| Own it | MiroTalk Open Source: self-host under applicable AGPLv3 terms | Route to product chooser and deployment |
| Build with it | Commercial / Enterprise | Route to APIs, commercial license, and contact |

Do not use "MiroTalk Cloud" and "hosted WEB" as interchangeable labels. Define each offer and its owner explicitly.

## URL strategy

1. Preserve all current documentation and script URLs during the IA/navigation change.
2. Treat current product paths as durable leaf URLs even when grouped under new navigation labels.
3. Add journey indexes at new descriptive URLs; do not move leaf content merely to make folders match navigation.
4. Keep `/license/licensing-options/` redirecting to `/license/`, but replace the client-side redirect with an edge/server 301 when deployment control permits.
5. Create a version-controlled redirect map before any later URL migration.
6. Never redirect a detailed guide to a generic category page when an equivalent destination exists.
7. Preserve the 24 shell-script URLs exactly because they may be used by automation outside the docs site.

## Contextual CTA model

Use one contextual callout near the end of an eligible page, before related documentation. Do not place all commercial options on every page.

| Page context | Primary CTA | Secondary/context |
| --- | --- | --- |
| Deployment, configuration, operations | Try MiroTalk Cloud | Skip infrastructure management |
| API, iframe, webhook, direct join | Build with MiroTalk | Explore Commercial Licensing |
| WEB SaaS and Stripe | Talk to MiroTalk | Commercial / Enterprise |
| Product overview | Live demo or relevant getting started | GitHub and managed option |
| Rebranding | Commercial License | Contact for enterprise requirements |
| Licensing and Ultimate | Purchase/contact path | Documentation and demos |

All CTA links should carry stable event names and page context when analytics is approved.

## Analytics recommendation

No analytics infrastructure exists, so this is a product/privacy decision rather than an extension task. Prefer a privacy-conscious, consent-appropriate platform with no unnecessary personal data.

Event taxonomy:

- `cta_cloud_start`
- `cta_cloud_from_self_host`
- `cta_commercial_license`
- `cta_enterprise_contact`
- `cta_github_view`
- `cta_codecanyon`
- `cta_demo_open`
- `developer_api_to_cloud`
- `developer_api_to_license`

Attach only non-personal context such as `page_path`, `product`, `journey`, `cta_location`, and `destination_type`. Cloud signup completion must be measured in the Cloud application and attributed with an approved cross-domain strategy.

## SEO landing and comparison policy

Do not create all proposed SEO pages at once. Validate search intent, factual differentiation, and maintenance ownership first. Prioritize pages closest to demonstrated product capability:

1. Self-Hosted Video Conferencing
2. Open Source Video Conferencing
3. Video Conferencing API / WebRTC API
4. White Label Video Conferencing
5. Click-to-Call
6. Live Streaming and Self-Hosted Webinar Platform
7. Video SaaS Platform

Competitor pages should cite dated public sources, state the comparison date, distinguish complete applications from SDK/infrastructure products, and include a "choose the other product when" section. Start with one pilot comparison after the core documentation is correct. Do not publish unverified feature, price, scale, lock-in, or production-readiness claims.

## Implementation plan

### Phase B: information architecture and navigation

1. Pin dependencies and add CI for strict build, links, and metadata.
2. Add the four journey indexes while preserving all current leaf URLs.
3. Rewrite `nav` labels to be descriptive and group existing pages by journey.
4. Make `/projects/` the single task-based product chooser; define the roles of `/overview/` and `/about/` to remove overlap.
5. Establish a version-controlled URL registry and redirect map.

Exit criteria: every inventory row appears exactly once in navigation or is explicitly marked utility/redirect; current URLs still resolve; strict build and internal-link checks pass.

### Phase C: visual and UX redesign

1. Bring product landing pages into the shared documentation shell or shared templates.
2. Implement the four-path homepage with documentation-first hierarchy.
3. Standardize typography, tokens, code presentation, admonitions, tabs, tables, and related links.
4. Verify desktop and mobile navigation, search, code, tables, media, focus, contrast, and reduced motion.

Exit criteria: no horizontal page overflow at 320, 390, 768, and desktop widths; WCAG 2.2 AA automated checks pass with manual keyboard review.

### Phase D: product discovery and conversion

1. Publish the approved Cloud/WEB naming model.
2. Implement the goal-based chooser and three-choice product framing.
3. Add contextual CTA components with controlled destinations.
4. Add consistent GitHub, demo, Cloud, commercial, and enterprise paths where relevant.

Exit criteria: each major journey reaches its intended action within two decisions; CTAs are contextual and uniquely identifiable.

### Phase E: SEO and redirects

1. Add unique front matter titles and descriptions to every Markdown page.
2. Add canonical, OpenGraph, Twitter, and structured metadata to all shared and standalone pages.
3. Resolve duplicate titles and normalize H1/H2 structure.
4. Correct broken/stale routes and validate all internal and external links.
5. Implement real 301 redirects where URLs change and verify sitemap last-modified semantics.
6. Pilot one high-value search-intent page after technical pages are complete.

Exit criteria: no missing/duplicate titles or descriptions, no missing canonicals, no broken internal links, and all redirects are one-hop 301s.

### Phase F: analytics

1. Approve platform, privacy policy, consent model, and retention.
2. Implement the event taxonomy through one reusable CTA/link mechanism.
3. Configure cross-domain attribution only if required and approved.
4. Validate events without collecting free text, secrets, room names, user names, or meeting identifiers.

Exit criteria: test events contain only approved fields and each commercial journey is attributable.

### Phase G: validation and release

1. Run strict build, internal/remote link checks, metadata checks, HTML validation, accessibility, Lighthouse, and visual regression.
2. Verify all API examples against product source and Swagger.
3. Verify GitHub, CodeCanyon, Stripe, demos, Cloud, contact, and affiliate links.
4. Crawl staging and compare URL inventory against production.
5. Deploy to staging, obtain product/legal approval, then deploy production with rollback instructions.

Exit criteria: inventory parity, approved content, green automated checks, verified redirects, and successful production smoke test.

## Product decisions

Confirmed on 2026-08-27:

1. MiroTalk Cloud is the approved name for the managed service powered by MiroTalk WEB.
2. The canonical MiroTalk Cloud CTA is <https://webrtc.mirotalk.com>.
3. Enterprise enquiries route to the author, Miroslav Pejic, at <miroslav.pejic.85@gmail.com>.

Still required for later phases:

1. Which licensing page and exact statements are legally approved as source of truth?
2. Which analytics platform, consent model, and retention policy are approved?
3. Which repository/deployment system controls production 301 redirects?
4. Are affiliate relationships to hosting providers disclosed elsewhere, or should the docs add disclosure?

## Validation record

- `python -m mkdocs build --strict`: passed in 3.35 seconds.
- Live homepage title, description, canonical, OG title, H1, search label, and landmarks: present.
- Live homepage at 390 x 844: no page-level horizontal overflow; sampled code and tables remained contained.
- `robots.txt`: allows all and declares the sitemap.
- Analytics source scan: no implementation found.
- Generated metadata scan: 82 HTML pages, no missing titles; duplicate and missing metadata issues recorded above.
- Built-site link crawl: 585 targets scanned in 21.4 seconds; one confirmed public internal 404 at `/html/overview/`. Reported placeholder/localhost failures and access-controlled external responses require a maintained allowlist and manual review.
- API prose scan: 19 named endpoint sections across five guides; WEB is Swagger-only.
- Image source scan: 181 image references across 58 files; descriptive-alt-text review required.

Strict MkDocs success does not prove remote links, standalone HTML semantics, API correctness, accessibility, or performance. Those remain explicit Phase G checks.