---
title: MiroTalk RND - Random One-to-One Video Chat
description: Explore MiroTalk RND for self-hosted random peer matching with one-to-one WebRTC video chat.
---

# MiroTalk RND

Random 1-on-1 video chat built with Node.js, Socket.IO, and WebRTC.

[View on GitHub](https://github.com/miroslavpejic85/mirotalkrnd){ .md-button .md-button--primary }
[Self-host MiroTalk RND](self-hosting.md){ .md-button }
[Review runtime sizing](metrics.md){ .md-button }

## How RND works

MiroTalk RND matches participants in a random one-to-one flow. The application server handles signaling, matching queue, and protections. Media is sent over WebRTC between peers when possible, with TURN fallback for restrictive networks.

| Concern | RND behavior |
| --- | --- |
| Participation | Two matched participants per session |
| Matching | Random queue-based pairing |
| Media | Direct peer-to-peer when possible |
| Network fallback | TURN relay when required |
| Server role | Signaling, queueing, rate limiting, and capacity guards |

[Compare product architectures](../overview/index.md){ .md-button }
[Read about STUN and TURN](../coturn/stun-turn.md){ .md-button }

## Chat capabilities

- Random peer matching
- Video and audio chat over WebRTC
- Skip/next match and end session controls
- Mic/camera toggle and self-preview controls
- Device selection and mobile-friendly UI
- Optional virtual background (blur or image)

## Self-host and operate

| Stage | Documentation |
| --- | --- |
| Install with Node.js or Docker | [Self-hosting guide](self-hosting.md) |
| Configure runtime and limits | [Configuration reference](configurations.md) |
| Expose local development securely | [Ngrok guide](ngrok.md) |
| Plan infrastructure sizing | [Metrics and capacity notes](metrics.md) |

## Current scope

MiroTalk RND does not currently provide the same REST API and webhook surfaces documented for other MiroTalk products.

