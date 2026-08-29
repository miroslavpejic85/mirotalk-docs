---
title: MiroTalk Documentation
description: Use MiroTalk Cloud, integrate video with APIs, or self-host an open-source MiroTalk video communication product.
---

<header class="home-hero">
  <span class="home-kicker">Documentation</span>
  <h1>MiroTalk Documentation</h1>
  <p>Build, deploy, or simply use your own video communication platform.</p>
  <div class="home-hero-links">
    <a class="md-button md-button--primary" href="/projects/">Choose a product</a>
    <a class="md-button" href="/story/">What is MiroTalk?</a>
  </div>
</header>

## What are you trying to do?

<div class="journey-grid">
  <a class="journey-card journey-cloud" href="/cloud/">
    <span class="journey-label">Use it</span>
    <h3>Use MiroTalk Cloud</h3>
    <p>No server setup or maintenance. MiroTalk operates the infrastructure for you.</p>
    <span class="journey-action">Start MiroTalk Cloud</span>
  </a>
  <a class="journey-card journey-host" href="/self-host/">
    <span class="journey-label">Own it</span>
    <h3>Self-host MiroTalk</h3>
    <p>Deploy the open-source MiroTalk products on infrastructure you control.</p>
    <span class="journey-action">Explore self-hosting</span>
  </a>
  <a class="journey-card journey-build" href="/build/">
    <span class="journey-label">Integrate it</span>
    <h3>Build with MiroTalk</h3>
    <p>Use REST APIs, iframe embedding, direct links, webhooks, and developer examples.</p>
    <span class="journey-action">Open developer docs</span>
  </a>
  <a class="journey-card journey-commercial" href="/commercial/">
    <span class="journey-label">Build a business</span>
    <h3>Commercial &amp; Enterprise</h3>
    <p>Explore licensing, white-label requirements, dedicated services, and support.</p>
    <span class="journey-action">View commercial options</span>
  </a>
</div>

## See MiroTalk in action

MiroTalk is a suite of browser-based WebRTC applications for meetings, private calls, broadcasting, click-to-call, scheduling, and administration.

<div class="home-preview home-youtube" data-embed-src="https://www.youtube-nocookie.com/embed/_IVn2aINYww?autoplay=1&amp;rel=0" data-embed-title="MiroTalk product overview" data-embed-class="home-youtube-frame" data-embed-allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" aria-describedby="home-preview-description">
  <img src="https://i.ytimg.com/vi/_IVn2aINYww/hqdefault.jpg" alt="" width="480" height="360" loading="eager" fetchpriority="low" referrerpolicy="no-referrer">
  <button class="home-youtube-play" data-embed-button type="button" aria-label="Play the MiroTalk product overview" title="Play the MiroTalk product overview">
    <span class="home-youtube-play-icon" aria-hidden="true"></span>
  </button>
  <noscript><a href="https://www.youtube.com/watch?v=_IVn2aINYww">Watch the MiroTalk product overview on YouTube</a></noscript>
</div>

<p class="media-caption" id="home-preview-description">An overview of what MiroTalk is, its most-used features, architecture, usage statistics, and interfaces for meetings, calls, broadcasting, scheduling, and administration.<br>YouTube loads only after you press Play.</p>


## Which MiroTalk product should I use?

Choose by workflow rather than technical terminology. The [product chooser](./projects/index.md) explains architecture and trade-offs in detail.

| Your goal | Recommended product | Try it |
| :--- | :--- | :--- |
| Scalable meetings, classes, or webinars | [MiroTalk SFU](./mirotalk-sfu/index.md) | [Live demo](https://sfu.mirotalk.com) |
| Private calls and small group meetings | [MiroTalk P2P](./mirotalk-p2p/index.md) | [Live demo](https://p2p.mirotalk.com) |
| Focused one-to-one video calls | [MiroTalk C2C](./mirotalk-c2c/index.md) | [Live demo](https://c2c.mirotalk.com) |
| One-to-many broadcasting | [MiroTalk BRO](./mirotalk-bro/index.md) | [Live demo](https://bro.mirotalk.com) |
| Click-to-call customer support | [MiroTalk CME](./mirotalk-cme/index.md) | [Live demo](https://cme.mirotalk.com) |
| Scheduling, invitations, and room management | [MiroTalk WEB](./mirotalk-web/index.md) | [Live demo](https://webrtc.mirotalk.com) |
| Server and configuration management | [MiroTalk Admin](./mirotalk-admin/index.md) | [View on GitHub](https://github.com/miroslavpejic85/mirotalk-admin) |

[Compare every product](./projects/index.md){ .md-button .md-button--primary }
[Explore MiroTalk Ultimate](./mirotalk-ultimate/index.md){ .md-button }

## MiroTalk Cloud

MiroTalk Cloud is the managed service powered by MiroTalk WEB. Create and manage rooms while MiroTalk handles deployment, updates, monitoring, scaling, backups, and maintenance.

<div class="home-callout home-callout-cloud">
  <div>
    <span class="home-kicker">Managed service</span>
    <h3>You use MiroTalk. We run the infrastructure.</h3>
    <p>Start in the browser without configuring a VPS, Docker, Node.js, SSL, or WebRTC services.</p>
  </div>
  <a class="md-button md-button--primary" href="https://webrtc.mirotalk.com">Start MiroTalk Cloud</a>
</div>

[Learn how Cloud differs from self-hosting](./cloud/index.md)

## Build with MiroTalk

Embed a hosted or self-hosted MiroTalk instance with an iframe. This minimal SFU example grants the browser permissions required by a meeting:

```html
<iframe
  allow="camera; microphone; speaker-selection; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay; picture-in-picture"
  src="https://sfu.mirotalk.com/newroom"
  style="width: 100vw; height: 100vh; border: 0;"
></iframe>
```

[Quick iframe integration](./utility/quick-custom-integration.md){ .md-button .md-button--primary }
[Browse APIs and webhooks](./build/index.md){ .md-button }
[View the React example](https://codepen.io/Miroslav-Pejic/pen/QWzmGaZ){ .md-button }

## Self-host MiroTalk

Deploy MiroTalk for control over your infrastructure, domain, and configuration. Start with the architecture guide, then choose a product-specific installation path.

| Start with | Use it for |
| :--- | :--- |
| [Self-hosting overview](./self-host/index.md) | Product selection and deployment paths |
| [WebRTC architectures](./webrtc/architectures.md) | P2P, SFU, and media topology decisions |
| [Ubuntu installation scripts](./scripts/about.md) | Automated install, update, and uninstall workflows |
| [Coturn](./coturn/stun-turn.md) | STUN and TURN networking |
| [Cloudron](./cloudron/cloudron.md) | Managed self-hosting workflow |

## Open source, Cloud, or commercial

<div class="path-grid">
  <section class="path-option">
    <span class="journey-label">Open source</span>
    <h3>Run it yourself</h3>
    <p>Inspect, modify, and self-host the source under the applicable AGPLv3 terms.</p>
    <a href="/self-host/">Open self-hosting docs</a>
  </section>
  <section class="path-option">
    <span class="journey-label">MiroTalk Cloud</span>
    <h3>Use the managed service</h3>
    <p>Use MiroTalk without operating the application and WebRTC infrastructure.</p>
    <a href="https://webrtc.mirotalk.com">Start MiroTalk Cloud</a>
  </section>
  <section class="path-option">
    <span class="journey-label">Commercial</span>
    <h3>Build with MiroTalk</h3>
    <p>Review the official licensing options for commercial products and business requirements.</p>
    <a href="/license/">Compare licensing options</a>
  </section>
</div>

## Support and project links

- [Read the frequently asked questions](./faq/index.md).
- [Join the MiroTalk Discord community](https://discord.gg/rgGYfeYW3N).
- [View products, prices, and licensing options](./license/index.md).
- [Read the MiroTalk story](./story/index.md).
- [Contact MiroTalk](mailto:miroslav.pejic.85@gmail.com) about enterprise requirements.
