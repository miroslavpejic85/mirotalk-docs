---
title: MiroTalk Open-Source WebRTC Video Conferencing
description: Explore MiroTalk open-source WebRTC projects for video conferencing, peer-to-peer calls, live streaming, click-to-call, integration, and self-hosting.
---

# MiroTalk Open Source WebRTC Documentation

MiroTalk is an open-source, self-hosted WebRTC platform for browser-based video calls, conferencing, live streaming, screen sharing, and chat, with no plugins or downloads required.

<video class="home-preview" width="715" height="402" autoplay muted loop playsinline preload="metadata" poster="./images/mirotalk-poster.webp" aria-label="MiroTalk open-source WebRTC video conferencing projects">
  <source src="./images/mirotalk.webm" type="video/webm">
  <source src="./images/mirotalk.mp4" type="video/mp4">
</video>

Choose the right open-source, self-hosted WebRTC architecture: peer-to-peer (P2P) for private video calls, or a Selective Forwarding Unit (SFU) for scalable meetings and webinars. It also supports live streaming, broadcasting, click-to-call, scheduling, and management.

[Choose a project](#choose-a-mirotalk-webrtc-project){ .md-button .md-button--primary }
[Compare projects](overview/index.html){ .md-button }
[Get a license](./license/index.html){ .md-button }
[Read customer reviews](./license/index.html#reviews){ .md-button }

## What is MiroTalk?

Learn how MiroTalk grew from a peer-to-peer calling project into a suite of focused real-time communication applications.

[Read the MiroTalk story](./story/index.html){ .md-button }

## Start Here

| I want to… | Start with |
| :--- | :--- |
| **Choose the right product** | [Compare all MiroTalk projects](./overview/index.html) |
| **Embed video in an application** | [MiroTalk integration guides](#integrate-mirotalk) |
| **Deploy on my own server** | [MiroTalk self-hosting guides](#self-host-mirotalk) |
| **Find help** | [FAQ](./faq/index.md) or [Discord community](https://discord.gg/rgGYfeYW3N) |

## Choose a MiroTalk WebRTC Project

Each project has a distinct purpose and its own documentation. Choose by audience size and workflow rather than by feature count alone.

[Not sure which MiroTalk project to choose?](./projects/index.html){ .md-button .md-button--primary }

| Project | Best for | About | Live demo |
| :--- | :--- | :--- | :--- |
| **SFU** | Selective Forwarding Unit for scalable meetings, classes, and webinars | [About SFU](./mirotalk-sfu/index.html) | [sfu.mirotalk.com](https://sfu.mirotalk.com) |
| **P2P** | Private calls and small group meetings | [About P2P](./mirotalk-p2p/index.html) | [p2p.mirotalk.com](https://p2p.mirotalk.com) |
| **C2C** | Focused one-to-one cam-to-cam calls | [About C2C](./mirotalk-c2c/index.html) | [c2c.mirotalk.com](https://c2c.mirotalk.com) |
| **BRO** | One-to-many broadcasting and online events | [About BRO](./mirotalk-bro/index.html) | [bro.mirotalk.com](https://bro.mirotalk.com) |
| **CME** | Instant customer click-to-call | [About CME](./mirotalk-cme/index.html) | [cme.mirotalk.com](https://cme.mirotalk.com) |
| **WEB** | Scheduling, invitations, and room management | [About WEB](./mirotalk-web/index.html) | [webrtc.mirotalk.com](https://webrtc.mirotalk.com) |
| **ADMIN** | Managing MiroTalk servers and configurations | [About Admin](./mirotalk-admin/index.html) | — |

Need the complete suite? Explore the [MiroTalk Ultimate bundle](./mirotalk-ultimate/index.html). Prefer a managed service with no server maintenance? Subscribe to **[MiroTalk WEB](https://webrtc.mirotalk.com)**.

## Use MiroTalk WEB as a Managed Service

Want secure, browser-based video meetings without managing your own server? The hosted MiroTalk WEB service gives you one workspace to create an account, schedule and manage meeting rooms, and join meetings without downloads.

Hosting, maintenance, and updates are handled for you. Choose a flexible monthly subscription or make a one-time payment for lifetime access.

[Get started with MiroTalk WEB](https://webrtc.mirotalk.com){ .md-button .md-button--primary }
[Learn about MiroTalk WEB](./mirotalk-web/index.html){ .md-button }

## Integrate MiroTalk

Embed a hosted or self-hosted MiroTalk instance in a website with an iframe. This minimal SFU example grants the browser permissions needed for a meeting:

```html
<iframe
  allow="camera; microphone; speaker-selection; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay; picture-in-picture"
  src="https://sfu.mirotalk.com/newroom"
  style="width: 100vw; height: 100vh; border: 0px;"
></iframe>
```

Follow the generic walkthrough to add a launch button, open a dedicated meeting page, or toggle an inline MiroTalk iframe in any website or application.

[Quick custom integration](./utility/quick-custom-integration.md){ .md-button .md-button--primary }

For room parameters, REST APIs, and production embedding patterns, use the guide for your selected project:

| Project | Integration | Direct join | REST API | Example |
| :--- | :--- | :--- | :--- | :--- |
| **SFU** | [SFU integration](./mirotalk-sfu/integration.md) | [SFU direct join](./mirotalk-sfu/join-room.md) | [SFU REST API](./mirotalk-sfu/api.md) | [CodePen](https://codepen.io/Miroslav-Pejic/pen/LYXRbmE) |
| **P2P** | [P2P integration](./mirotalk-p2p/integration.md) | [P2P direct join](./mirotalk-p2p/join-room.md) | [P2P REST API](./mirotalk-p2p/api.md) | [CodePen](https://codepen.io/Miroslav-Pejic/pen/jOQMVzx) |
| **C2C** | [C2C integration](./mirotalk-c2c/integration.md) | [C2C direct join](./mirotalk-c2c/join-room.md) | [C2C REST API](./mirotalk-c2c/api.md) | [CodePen](https://codepen.io/Miroslav-Pejic/pen/ExOgNbJ) |
| **BRO** | [BRO integration](./mirotalk-bro/integration.md) | [BRO direct join](./mirotalk-bro/join-room.md) | [BRO REST API](./mirotalk-bro/api.md) | [CodePen](https://codepen.io/Miroslav-Pejic/pen/OJaRbZg) |
| **CME** | [CME integration](./mirotalk-cme/integration.md) | [CME direct join](./mirotalk-cme/join-room.md) | [CME REST API](./mirotalk-cme/api.md) | [CodePen](https://codepen.io/Miroslav-Pejic/pen/empeGYJ) |
| **WEB** | [WEB integration](./mirotalk-web/integration.md) | — | [WEB REST API](./mirotalk-web/api.md) | [CodePen](https://codepen.io/Miroslav-Pejic/pen/jOQMVxx) |

[View the React integration example](https://codepen.io/Miroslav-Pejic/pen/QWzmGaZ)

## Self-Host MiroTalk

Deploy MiroTalk on your own server for control over your data, domain, branding, and infrastructure. If you are unsure which architecture fits your audience size, [compare the projects](./overview/index.html) before deploying.

| Project | Self-Hosting Guide | Configurations |
| :--- | :--- | :--- |
| 🏆 **SFU** | [Self-host SFU](./mirotalk-sfu/self-hosting.md) | [SFU configuration](./mirotalk-sfu/configurations.md) |
| 🚀 **P2P** | [Self-host P2P](./mirotalk-p2p/self-hosting.md) | [P2P configuration](./mirotalk-p2p/configurations.md) |
| ✨ **C2C** | [Self-host C2C](./mirotalk-c2c/self-hosting.md) | [C2C configuration](./mirotalk-c2c/configurations.md) |
| 📡 **BRO** | [Self-host BRO](./mirotalk-bro/self-hosting.md) | [BRO configuration](./mirotalk-bro/configurations.md) |
| 🟢 **CME** | [Self-host CME](./mirotalk-cme/self-hosting.md) | [CME configuration](./mirotalk-cme/configurations.md) |
| 🛠 **WEB** | [Self-host WEB](./mirotalk-web/self-hosting.md) | [WEB configuration](./mirotalk-web/configurations.md) |
| ⚙️ **ADMIN** | [Self-host Admin](./mirotalk-admin/self-hosting.md) | — |

Choose a self-hosted installation method: [Ubuntu scripts](./scripts/about.md) or [Cloudron](./cloudron/cloudron.md). Prefer a managed service with no server maintenance? Explore [MiroTalk on EvoPlat](./evoplat/evoplat.md).

## MiroTalk Support and Licensing

<div class="home-license-callout">
  <div class="home-license-icon" aria-hidden="true">
    <img src="./images/license.png" alt="">
  </div>
  <div class="home-license-content">
    <span class="home-license-label">Open source or commercial</span>
    <h3>Choose the right license for your project</h3>
    <p>Use MiroTalk under AGPLv3 when your MiroTalk-based source remains public, or choose a commercial license for private and paid products.</p>
    <div class="home-license-actions">
      <a class="md-button md-button--primary" href="./license/index.html">Compare licensing options</a>
      <a class="home-license-link" href="./license/index.html#pricing">View product pricing &rarr;</a>
    </div>
  </div>
</div>

For help, check the [Frequently Asked Questions](./faq/index.md) or join the [MiroTalk Discord community](https://discord.gg/rgGYfeYW3N).

[Read the FAQ](./faq/index.md){ .md-button }
