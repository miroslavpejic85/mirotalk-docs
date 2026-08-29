---
title: MiroTalk CME - Click-to-Call Video
description: Explore MiroTalk CME for self-hosted click-to-call video, availability, private calls, embedding, APIs, webhooks, and host protection.
---

# MiroTalk CME

A self-hosted click-to-call experience for support, consultations, and direct communication. Participants can see who is available and start a private one-to-one WebRTC call.

[Try the live demo](https://cme.mirotalk.com){ .md-button .md-button--primary }
[Self-host MiroTalk CME](self-hosting.md){ .md-button }
[View product page](../sites/cme.html){ .md-button }

![MiroTalk CME click-to-call interface](../images/mirotalk/cme.png){ .product-shot }

## How CME works

CME separates availability and call initiation from the private media session. Application services coordinate users and signaling; callers establish an encrypted P2P media path directly when possible, with TURN relay fallback.

| Stage | Responsibility |
| --- | --- |
| Availability | Show users who can receive a call |
| Call initiation | Connect a caller to a selected user |
| Media | Exchange webcam, microphone, screen, chat, and files |
| Network fallback | Relay encrypted WebRTC packets through TURN when required |

[Compare product architectures](../overview/index.md){ .md-button }

## Call capabilities

- Private video and audio calls
- Screen sharing, real-time chat, and file sharing
- Device switching and browser notifications
- Host protection and JWT-based API workflows
- Iframe and widget embedding

## Build with CME

| Goal | Documentation |
| --- | --- |
| Work with users and calls programmatically | [REST API](api.md) |
| Embed click-to-call | [Iframe and widget integration](integration.md) |
| Construct direct call links | [Join options](join-room.md) |
| Receive call events | [Webhooks](webhook.md) |
| Localize the interface | [Internationalization](I18n.md) |

## Self-host and operate

| Stage | Documentation |
| --- | --- |
| Install | [Self-hosting guide](self-hosting.md) |
| Configure | [Configuration reference](configurations.md) |
| Develop locally | [Ngrok guide](ngrok.md) |

## Licensing and support

Use the official licensing page as the source of truth for commercial requirements.

[Compare licensing options](../license/index.md){ .md-button .md-button--primary }
[Review the CME commercial package](https://codecanyon.net/item/callme-easy-webrtc-video-call-app/55342915){ .md-button }
[Contact MiroTalk Enterprise](../enterprise/index.md){ .md-button }