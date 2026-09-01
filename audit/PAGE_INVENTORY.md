# MiroTalk Documentation Page Inventory and URL Map

Audit date: 2026-08-27  
Source revision: `12f6f94`

## Legend

- SEO: **H** = high-intent or high-authority potential; **M** = useful long-tail/supporting value; **L** = utility, duplicate, or little standalone search value.
- **Keep** means preserve both content and URL.
- **Move nav** means change information-architecture ownership without changing the URL.
- **Improve** means add metadata, structure, links, examples, or verified positioning.
- **Merge** means consolidate overlapping content while retaining the old URL through a redirect or useful compatibility page.
- No content page is approved for deletion in Phase A.

Generated titles for many Markdown pages currently use generic navigation labels such as `api`, `integration`, and `self-hosting`. The title shown below records that current behavior where applicable; the improved title should include the product name.

## Core discovery, support, and commercial pages

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/` | MiroTalk: Open-Source WebRTC Video Conferencing; global discovery homepage | All visitors / H | Keep; redesign around four paths; retain technical entry points | Cross-journey home |
| `/story/` | The Story Behind MiroTalk; project history and credibility | Evaluators, community / M | Migrated to shared shell; unsupported metrics removed; URL preserved | Commercial & Enterprise > About |
| `/about/` | MiroTalk WebRTC Suite; suite, demos, integrations, and pathways | Evaluators, developers / H | Migrated to shared shell; overlap removed; URL preserved | Use > Product overview |
| `/overview/` | Compare MiroTalk Products and Architectures; technical comparison | Product evaluators / H | Migrated to shared shell; architecture/capability reference; URL preserved | Use > Compare architectures |
| `/projects/` | Which MiroTalk Product Should I Choose?; goal-based chooser | All evaluators / H | Migrated to shared shell; canonical task-based chooser; URL preserved | Use > Choose a product |
| `/changelogs/changelogs/` | changelogs; links to product commit histories | Existing users / L | Keep; improve label and update model | Support > Changelogs |
| `/faq/` | faq; broad troubleshooting and product questions | All users / H | Keep; retitle; split/link answers to owning guides over time | Support > FAQ |
| `/license/` | MiroTalk Licensing Options; licensing paths, pricing, and CodeCanyon terms | Commercial evaluators / H | Migrated to shared shell; marketplace links and URL preserved | Commercial & Enterprise > Licensing |
| `/license/licensing-options/` | Redirecting to MiroTalk Licensing Options | Legacy traffic / L | Keep redirect; implement HTTP 301; no index | Redirect to `/license/` |
| `/mirotalk-ultimate/` | MiroTalk Ultimate; seven-application bundle, deployment, integration, and pricing | Commercial buyers / H | Migrated to shared shell; claims normalized; URL and checkout paths preserved | Commercial & Enterprise > Ultimate |
| `/cloudron/cloudron/` | cloudron; Cloudron deployment option | Self-hosters / M | Keep; retitle and add prerequisites/result/troubleshooting | Self-host > Deployment options |

## Shared infrastructure and utility pages

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/coturn/stun-turn/` | stun-turn; explains STUN/TURN and Coturn | Infrastructure teams / H | Keep; retitle; cross-link architecture and deployment | Self-host > Networking |
| `/coturn/installation/` | installation; installs and secures Coturn | Infrastructure teams / H | Keep; retitle; verify commands and affiliate disclosure | Self-host > Networking |
| `/ngrok/ngrok/` | ngrok; shared local tunnel guide | Developers / M | Keep; make canonical shared guide; product pages link here | Build > Local development |
| `/scripts/about/` | about; Ubuntu automation script index | Self-hosters / H | Keep; retitle; preserve script endpoints exactly | Self-host > Automated install |
| `/utility/quick-custom-integration/` | Quick Custom Integration; generic iframe integration | Developers / H | Keep; improve expected result/security/accessibility | Build > Embedding |
| `/utility/docker-compose/` | docker-compose; install/update Docker Compose | Infrastructure teams / H | Keep; retitle and connect to product deployment | Self-host > Docker |
| `/utility/ftp/` | ftp; FTP setup/use | Operators / L | Keep but reassess necessity/security guidance | Self-host > Utilities |
| `/utility/nvm/` | nvm; Node.js version management | Developers, operators / M | Keep; retitle; verify supported Node versions | Self-host > Prerequisites |
| `/utility/update/` | update; shared Git update procedure | Operators / M | Keep; clarify product scope and rollback | Self-host > Operations |
| `/utility/whisper/` | whisper; self-host speech-to-text service | Operators, integrators / H | Keep; structure and connect to supported products | Self-host > Integrations |
| `/webrtc/architectures/` | architectures; WebRTC architecture concepts | Technical evaluators / H | Keep; retitle; link chooser and scaling | Self-host > Architecture |
| `/mirotalk-docs/self-hosting/` | self-hosting; deploy this documentation site | Docs maintainers / L | Keep; move out of product-facing hierarchy | Contribute > Documentation |

## MiroTalk Admin

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/mirotalk-admin/` | MiroTalk Admin - Infrastructure Management; product overview | Administrators / M | Migrated to shared shell; privileged control-plane role clarified; URL preserved | Self-host > Admin |
| `/mirotalk-admin/quick-start/` | quick-start; local Admin setup | Administrators / M | Keep; retitle; obsolete `/html/overview/` link corrected | Self-host > Admin |
| `/mirotalk-admin/self-hosting/` | self-hosting; production Admin deployment | Administrators, DevOps / M | Keep; retitle and normalize guide structure | Self-host > Admin |

## MiroTalk BRO

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/mirotalk-bro/` | MiroTalk BRO - One-to-Many Live Broadcasting; product overview | Broadcasters, evaluators / H | Migrated to shared shell; P2P/SFU modes clarified; URL preserved | Use > Products > BRO |
| `/mirotalk-bro/api/` | MiroTalk BRO REST API; authenticated direct-join endpoint and examples | Developers / H | Normalized against deployed Swagger 1.0.0; safe secret placeholders added | Build > APIs > BRO |
| `/mirotalk-bro/configurations/` | configurations; BRO runtime settings | Operators / M | Keep; retitle; organize by outcome and environment | Self-host > Configure > BRO |
| `/mirotalk-bro/integration/` | integration; BRO iframe embedding | Developers / H | Keep; retitle; add security and expected result | Build > Embedding > BRO |
| `/mirotalk-bro/join-room/` | join-room; broadcast/viewer URL parameters | Developers, users / M | Keep; retitle; document parameter contracts | Build > Direct join > BRO |
| `/mirotalk-bro/ngrok/` | ngrok; local BRO tunnel | Developers / L | Keep URL; merge content toward shared ngrok guide | Build > Local development |
| `/mirotalk-bro/rtmp/` | rtmp; RTMP upstream source for SFU rooms | Broadcasters, operators / H | New; documents MediaMTX ingest, publish URLs, RTMPS, and tuning | Self-host > Streaming > BRO |
| `/mirotalk-bro/self-hosting/` | self-hosting; BRO production deployment | DevOps, broadcasters / H | Keep; retitle; normalize and add managed CTA | Self-host > BRO |

## MiroTalk C2C

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/mirotalk-c2c/` | MiroTalk C2C - One-to-One Video Calls; product overview | Product evaluators / H | Migrated to shared shell; one-to-one role clarified; URL preserved | Use > Products > C2C |
| `/mirotalk-c2c/api/` | MiroTalk C2C REST API; meeting and direct-join endpoints | Developers / H | Normalized against deployed Swagger 1.0.0; safe secret placeholders added | Build > APIs > C2C |
| `/mirotalk-c2c/configurations/` | configurations; C2C environment settings | Operators / M | Keep; retitle; organize by outcome | Self-host > Configure > C2C |
| `/mirotalk-c2c/integration/` | integration; C2C iframe embedding | Developers / H | Keep; retitle; add expected result/security | Build > Embedding > C2C |
| `/mirotalk-c2c/join-room/` | join-room; C2C direct-join parameters | Developers, users / M | Keep; retitle; document parameter contracts | Build > Direct join > C2C |
| `/mirotalk-c2c/ngrok/` | ngrok; local C2C tunnel | Developers / L | Keep URL; merge content toward shared ngrok guide | Build > Local development |
| `/mirotalk-c2c/self-hosting/` | self-hosting; C2C production deployment | DevOps / H | Keep; retitle; normalize and add managed CTA | Self-host > C2C |

## MiroTalk CME

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/mirotalk-cme/` | MiroTalk CME - Click-to-Call Video; product overview | Support/sales teams / H | Migrated to shared shell; click-to-call journey clarified; URL preserved | Use > Products > CME |
| `/mirotalk-cme/api/` | MiroTalk CME REST API; six endpoint contracts and examples | Developers / H | Pilot normalized against deployed Swagger 1.1.0; malformed URL and secret literals fixed | Build > APIs > CME |
| `/mirotalk-cme/configurations/` | configurations; CME runtime settings | Operators / M | Keep; retitle; organize by outcome | Self-host > Configure > CME |
| `/mirotalk-cme/I18n/` | I18n; CME localization | Developers / M | Keep; normalize lowercase title/URL only if redirected | Build > Customize > CME |
| `/mirotalk-cme/integration/` | integration; CME widget/iframe embedding | Developers / H | Keep; retitle; preserve widget assets/examples | Build > Embedding > CME |
| `/mirotalk-cme/join-room/` | join-room; CME caller/agent parameters | Developers, support teams / M | Keep; retitle; document role and parameter contracts | Build > Direct join > CME |
| `/mirotalk-cme/ngrok/` | ngrok; local CME tunnel | Developers / L | Keep URL; merge content toward shared ngrok guide | Build > Local development |
| `/mirotalk-cme/self-hosting/` | self-hosting; CME production deployment | DevOps, support teams / H | Keep; retitle; normalize and add managed CTA | Self-host > CME |
| `/mirotalk-cme/webhook/` | webhook; signed call lifecycle events | Developers / H | Keep; retitle; verify events/signature/errors | Build > Webhooks > CME |

## MiroTalk P2P

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/mirotalk-p2p/` | MiroTalk P2P - Private Small-Group Meetings; product overview | Small-team evaluators / H | Migrated to shared shell; mesh and TURN trade-offs stated; URL preserved | Use > Products > P2P |
| `/mirotalk-p2p/api/` | MiroTalk P2P REST API; stats, meetings, join, and token endpoints | Developers / H | Normalized against deployed Swagger 1.0.1; safe secret placeholders added | Build > APIs > P2P |
| `/mirotalk-p2p/configurations/` | configurations; P2P server/client settings | Operators / M | Keep; retitle; organize by outcome | Self-host > Configure > P2P |
| `/mirotalk-p2p/host-protection/` | host-protection; room host authorization | Developers, operators / M | Keep; retitle; explain threat model and expected result | Self-host > Security > P2P |
| `/mirotalk-p2p/integration/` | integration; P2P iframe/widget embedding | Developers / H | Keep; retitle; preserve examples; add security | Build > Embedding > P2P |
| `/mirotalk-p2p/join-room/` | join-room; P2P direct-join query parameters | Developers / H | Keep; retitle; tabulate and validate parameters | Build > Direct join > P2P |
| `/mirotalk-p2p/ngrok/` | ngrok; local P2P tunnel | Developers / L | Keep URL; merge content toward shared ngrok guide | Build > Local development |
| `/mirotalk-p2p/rebranding/` | rebranding; P2P white-label changes and license CTA | Commercial developers / H | Keep; legal review; connect commercial licensing | Commercial > White-label |
| `/mirotalk-p2p/self-hosting/` | self-hosting; P2P production deployment | DevOps / H | Keep; retitle; normalize and add managed CTA | Self-host > P2P |
| `/mirotalk-p2p/updates/` | updates; update P2P deployment | Operators / M | Keep; retitle; add backup/rollback/version notes | Self-host > Operate > P2P |
| `/mirotalk-p2p/webhook/` | webhook; P2P meeting lifecycle events | Developers / H | Keep; retitle; verify events/payload/errors | Build > Webhooks > P2P |

## MiroTalk SFU

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/mirotalk-sfu/` | MiroTalk SFU - Scalable Group Meetings; product overview | Group/webinar evaluators / H | Migrated to shared shell; unsupported capacity promises removed; URL preserved | Use > Products > SFU |
| `/mirotalk-sfu/api/` | MiroTalk SFU REST API; stats, meetings, lifecycle, join, and token endpoints | Developers / H | Normalized against deployed Swagger 1.0.1; safe secret placeholders added | Build > APIs > SFU |
| `/mirotalk-sfu/configurations/` | configurations; SFU server/client settings | Operators / H | Keep; retitle; organize by outcome | Self-host > Configure > SFU |
| `/mirotalk-sfu/host-protection/` | host-protection; room host authorization | Developers, operators / M | Keep; retitle; explain threat model | Self-host > Security > SFU |
| `/mirotalk-sfu/integration/` | integration; SFU iframe/widget embedding | Developers / H | Keep; retitle; preserve examples; add security | Build > Embedding > SFU |
| `/mirotalk-sfu/join-room/` | join-room; SFU direct-join query parameters | Developers / H | Keep; retitle; tabulate and validate parameters | Build > Direct join > SFU |
| `/mirotalk-sfu/ngrok/` | ngrok; local SFU tunnel | Developers / L | Keep URL; merge content toward shared ngrok guide | Build > Local development |
| `/mirotalk-sfu/rebranding/` | rebranding; SFU white-label changes and license CTA | Commercial developers / H | Keep; legal review; connect commercial licensing | Commercial > White-label |
| `/mirotalk-sfu/rtmp/` | rtmp; live-streaming integration | Broadcasters, operators / H | Keep; retitle; clarify supported topology/result | Self-host > Streaming > SFU |
| `/mirotalk-sfu/scalability/` | scalability; architecture, capacity, and provider examples | Infrastructure teams / H | Keep; verify benchmarks/prices; add dated methodology | Self-host > Scale > SFU |
| `/mirotalk-sfu/self-hosting/` | self-hosting; SFU production deployment | DevOps / H | Keep; retitle; normalize and add managed CTA | Self-host > SFU |
| `/mirotalk-sfu/updates/` | updates; update SFU deployment | Operators / M | Keep; retitle; add backup/rollback/version notes | Self-host > Operate > SFU |
| `/mirotalk-sfu/webhook/` | webhook; SFU meeting lifecycle events | Developers / H | Keep; retitle; verify events/payload/errors | Build > Webhooks > SFU |

## MiroTalk WEB and current managed service

| Current URL | Current title and purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/mirotalk-web/` | MiroTalk WEB - Meeting Workspace and Scheduler; product overview | SaaS/workspace evaluators / H | Migrated to shared shell; relationship to Cloud and media products defined; URL preserved | Use > Products > WEB |
| `/mirotalk-web/api/` | MiroTalk WEB REST API; user, room, booking, and integration API entry guide | Developers / H | Normalized against deployed OpenAPI 3.0 v1.0.0; Swagger remains contract authority | Build > APIs > WEB |
| `/mirotalk-web/configurations/` | configurations; WEB backend settings | Operators / H | Keep; retitle; organize by outcome | Self-host > Configure > WEB |
| `/mirotalk-web/integration/` | integration; WEB iframe embedding | Developers / H | Keep; retitle; add expected result/security | Build > Embedding > WEB |
| `/mirotalk-web/ngrok/` | ngrok; local WEB tunnel | Developers / L | Keep URL; merge content toward shared ngrok guide | Build > Local development |
| `/mirotalk-web/self-hosting/` | self-hosting; WEB production deployment | DevOps, SaaS teams / H | Keep; retitle; distinguish self-hosted WEB from Cloud | Self-host > WEB |
| `/mirotalk-web/stripe/` | stripe; SaaS subscriptions and billing behavior | SaaS developers / H | Keep; verify against source and current Stripe flow | Build > SaaS > Billing |

## Published automation script URLs

These are downloadable/executable resources rather than prose pages. All have high operational importance even when low SEO value. Preserve exact paths, content types, executable formatting, and backward compatibility.

| Current URL | Purpose | Audience / SEO | Disposition | Proposed owner |
| --- | --- | --- | --- | --- |
| `/scripts/sfu/sfu-install.sh` | Install SFU | Operators / L | Keep exact URL; security/version test | Self-host > Scripts > SFU |
| `/scripts/sfu/sfu-uninstall.sh` | Uninstall SFU | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > SFU |
| `/scripts/sfu/sfu-update.sh` | Update SFU | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > SFU |
| `/scripts/p2p/p2p-install.sh` | Install P2P | Operators / L | Keep exact URL; security/version test | Self-host > Scripts > P2P |
| `/scripts/p2p/p2p-uninstall.sh` | Uninstall P2P | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > P2P |
| `/scripts/p2p/p2p-update.sh` | Update P2P | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > P2P |
| `/scripts/c2c/c2c-install.sh` | Install C2C | Operators / L | Keep exact URL; security/version test | Self-host > Scripts > C2C |
| `/scripts/c2c/c2c-uninstall.sh` | Uninstall C2C | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > C2C |
| `/scripts/c2c/c2c-update.sh` | Update C2C | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > C2C |
| `/scripts/bro/bro-install.sh` | Install BRO | Operators / L | Keep exact URL; security/version test | Self-host > Scripts > BRO |
| `/scripts/bro/bro-uninstall.sh` | Uninstall BRO | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > BRO |
| `/scripts/bro/bro-update.sh` | Update BRO | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > BRO |
| `/scripts/cme/cme-install.sh` | Install CME | Operators / L | Keep exact URL; security/version test | Self-host > Scripts > CME |
| `/scripts/cme/cme-uninstall.sh` | Uninstall CME | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > CME |
| `/scripts/cme/cme-update.sh` | Update CME | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > CME |
| `/scripts/web/web-install.sh` | Install WEB | Operators / L | Keep exact URL; security/version test | Self-host > Scripts > WEB |
| `/scripts/web/web-uninstall.sh` | Uninstall WEB | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > WEB |
| `/scripts/web/web-update.sh` | Update WEB | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > WEB |
| `/scripts/coturn/coturn-install.sh` | Install Coturn | Operators / L | Keep exact URL; firewall/security test | Self-host > Scripts > Coturn |
| `/scripts/coturn/coturn-uninstall.sh` | Uninstall Coturn | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > Coturn |
| `/scripts/coturn/coturn-update.sh` | Update Coturn | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > Coturn |
| `/scripts/whisper/whisper-install.sh` | Install Whisper service | Operators / L | Keep exact URL; GPU/CPU requirements test | Self-host > Scripts > Whisper |
| `/scripts/whisper/whisper-uninstall.sh` | Uninstall Whisper service | Operators / L | Keep exact URL; destructive-action warning | Self-host > Scripts > Whisper |
| `/scripts/whisper/whisper-update.sh` | Update Whisper service | Operators / L | Keep exact URL; backup/rollback test | Self-host > Scripts > Whisper |

## Phase B journey pages

These additions were implemented in Phase B. They fill navigation and product-positioning gaps without replacing current leaf URLs.

| Current URL | Title | Purpose | Links to existing content |
| --- | --- | --- | --- |
| `/use/` | Use MiroTalk | Journey index for Cloud, product choice, meetings, and support | `/projects/`, product overviews, `/faq/` |
| `/cloud/` | MiroTalk Cloud | Approved managed-product positioning and getting started | WEB/Cloud user guides once supplied |
| `/build/` | Build with MiroTalk | Developer index by API, embed, direct join, webhook, and SaaS goal | All existing API/integration/join/webhook pages |
| `/self-host/` | Self-host MiroTalk | Deployment index by goal, architecture, and product | All existing self-host/config/script/infrastructure pages |
| `/commercial/` | Commercial & Enterprise | Business route for licensing, white-label, services, and contact | `/license/`, `/mirotalk-ultimate/`, rebranding pages |
| `/enterprise/` | MiroTalk Enterprise | Verified enterprise offer and lead route | Approved contact endpoint |

## URL preservation rules for Phase B

1. All URLs in this inventory remain unchanged.
2. Navigation movement does not imply filesystem movement.
3. Every content URL must be linked from exactly one primary journey or explicitly classified as support, contribute, utility, or redirect.
4. Shared guides replace duplicated prose only after product URLs provide a useful product-specific summary and canonical next step.
5. Script paths are immutable unless a versioned compatibility strategy is approved.
6. Any future changed URL requires an old URL, new URL, reason, redirect status, test, and removal date recorded in a redirect registry.