---
title: MiroTalk P2P - Private Small-Group Meetings
description: Explore MiroTalk P2P for self-hosted private calls and small-group meetings with direct WebRTC media, embedding, APIs, and host controls.
---

# MiroTalk P2P

Self-hosted WebRTC meetings for private calls and small groups. Participants exchange encrypted media directly when networks permit, keeping routine media forwarding off the application server.

[Try the live demo](https://p2p.mirotalk.com/newcall){ .md-button .md-button--primary }
[Self-host MiroTalk P2P](self-hosting.md){ .md-button }
[View product page](../sites/p2p.html){ .md-button }

![MiroTalk P2P small-group meeting interface](../images/mirotalk/p2p.png){ .product-shot }

## How P2P works

MiroTalk P2P uses a mesh: each participant sends media to every other participant. The application server coordinates signaling and rooms; a TURN server can relay encrypted packets when a direct path cannot be established.

| Responsibility | Participant device | Application infrastructure |
| --- | --- | --- |
| Media | Sends and receives peer streams | Does not normally forward media |
| Room growth | Uplink, downlink, CPU, and rendering increase | Signaling load grows more gradually |
| Restricted networks | Uses a direct path when possible | TURN relays media when required |
| Trust boundary | Participants are media endpoints | Signaling and optional relay remain server-side |

P2P is best when privacy, direct media paths, and modest infrastructure matter more than large-room scalability.

[Compare product architectures](../overview/index.md){ .md-button }
[Read about STUN and TURN](../coturn/stun-turn.md){ .md-button }

## Meeting capabilities

- Audio, webcam, and screen sharing
- Group and private chat, reactions, and file transfer
- Collaborative whiteboard and local recording
- Host protection and direct room links
- Responsive browser interface without a required plugin

Feature availability can depend on configuration and release. Follow the linked guides for current options.

## Build with P2P

| Goal | Documentation |
| --- | --- |
| Create rooms programmatically | [REST API](api.md) |
| Embed calls in a site | [Iframe and widget integration](integration.md) |
| Build direct room URLs | [Room join options](join-room.md) |
| Receive room lifecycle events | [Webhooks](webhook.md) |

## Self-host and operate

| Stage | Documentation |
| --- | --- |
| Install | [Self-hosting guide](self-hosting.md) |
| Configure | [Configuration reference](configurations.md) |
| Protect hosts | [Host protection](host-protection.md) |
| Update safely | [Update guide](updates.md) |
| Develop locally | [Ngrok guide](ngrok.md) |
| Customize branding | [Rebranding guide](rebranding.md) |

!!! note "TURN changes operating cost"

    Direct P2P media reduces routine server bandwidth, but restrictive networks may require TURN relay traffic. Test your expected browser, network, and room mix.

## Licensing and support

Use the official licensing page as the source of truth for commercial requirements.

[Compare licensing options](../license/index.md){ .md-button .md-button--primary }
[Review the P2P commercial package](https://codecanyon.net/item/mirotalk-p2p-webrtc-realtime-video-conferences/38376661){ .md-button }
[Contact MiroTalk Enterprise](../enterprise/index.md){ .md-button }