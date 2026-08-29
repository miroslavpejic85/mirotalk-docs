---
title: MiroTalk SFU - Scalable Group Meetings
description: Explore MiroTalk SFU for self-hosted group meetings, classes, webinars, integrations, recording, streaming, and horizontal or vertical scaling.
---

# MiroTalk SFU

<div class="product-page-marker product-page-sfu" aria-hidden="true"></div>

Self-hosted WebRTC group meetings, classes, and webinars powered by [mediasoup](https://mediasoup.org/). An SFU forwards participant media through server infrastructure so rooms can grow beyond the practical limits of a peer-to-peer mesh.

[Try the live demo](https://sfu.mirotalk.com/newroom){ .md-button .md-button--primary }
[Self-host MiroTalk SFU](self-hosting.md){ .md-button }

![MiroTalk SFU group meeting interface](../images/mirotalk/sfu.png){ .product-shot }

## How MiroTalk SFU works

Each participant sends an upstream audio and video stream to the Selective Forwarding Unit. The server forwards selected streams to the other participants instead of mixing them into one composite feed.

![Participants sending media through an SFU server](../images/sfu.png)

| Responsibility | Participant device | SFU server |
| --- | --- | --- |
| Upload | Sends one primary media stream | Receives participant streams |
| Distribution | Receives selected remote streams | Routes and forwards streams |
| Capacity pressure | Decoding, rendering, and access-network bandwidth | CPU, memory, network throughput, and media quality |
| Media trust boundary | DTLS-SRTP protects transport to the server | The self-hosted SFU is inside the media path |

This architecture reduces distribution work on participant devices, but server capacity becomes part of room planning. Validate expected room sizes, codecs, resolution, recording, and concurrent workloads in your own environment.

[Compare MiroTalk architectures](../overview/index.md){ .md-button }
[Plan SFU scaling](scalability.md){ .md-button }

## Meeting capabilities

### Communication and collaboration

- Audio, webcam, and screen sharing
- Group and private chat
- File sharing and collaborative whiteboard
- Emoji, reactions, hand raising, and push-to-talk
- Collaborative editor and breakout rooms

### Hosting and moderation

- Lobby and room locking
- Host protection and moderation controls
- Polls, webinar roles, and presenter controls
- Direct room links with configurable join options
- Multiple rooms without a fixed meeting duration imposed by the application

### Media and extensions

- Local and server-side recording options
- RTMP streaming and broadcasting workflows
- Virtual backgrounds and noise suppression
- Speech recognition, AI assistants, and avatar integrations where configured
- Responsive browser interface without a required client download or plugin

Capabilities can require additional services or configuration. Use the linked guides as the source of truth for prerequisites and current behavior.

## Build with SFU

| Goal | Documentation | What it covers |
| --- | --- | --- |
| Create and inspect meetings programmatically | [REST API](api.md) | Meeting creation, active meetings, statistics, and room lifecycle operations |
| Embed a meeting experience | [Iframe and widget integration](integration.md) | Iframe API, configuration options, and widget setup |
| Construct direct meeting links | [Room join options](join-room.md) | Query parameters and room-entry behavior |
| React to meeting events | [Webhooks](webhook.md) | Configuration and meeting lifecycle events |
| Stream to RTMP services | [RTMP streaming](rtmp.md) | FFmpeg, Node Media Server, and Nginx RTMP options |

## Self-host and operate

| Stage | Start here | Outcome |
| --- | --- | --- |
| Install | [Self-hosting guide](self-hosting.md) | Deploy with Node.js, PM2, or Docker behind HTTPS |
| Configure | [Configuration reference](configurations.md) | Set server and client behavior |
| Protect hosts | [Host protection](host-protection.md) | Restrict host capabilities and room creation |
| Scale | [Scalability guide](scalability.md) | Plan vertical or multi-server deployment |
| Update | [Update guide](updates.md) | Maintain a customized installation |
| Develop locally | [Ngrok guide](ngrok.md) | Expose a development instance over HTTPS |

!!! warning "Capacity figures require testing"

    Participant capacity is workload-dependent. Browser mix, active cameras, selected video quality, frame rate, recording, AI features, RTMP output, TURN traffic, and concurrent rooms can materially change resource use.

## Security model

- WebRTC media transport between each participant and the SFU is protected with DTLS-SRTP.
- The SFU must process routing information and is inside the media trust boundary; deploy it on infrastructure you control and secure.
- OIDC, host protection, and JWT-based API controls are available for their documented workflows.
- Production deployments require HTTPS, restricted administration, maintained dependencies, and appropriate firewall rules.

[Configure host protection](host-protection.md){ .md-button }
[Review deployment requirements](self-hosting.md#requirements){ .md-button }

## Use managed or commercial options

Use MiroTalk Cloud when you want a managed service instead of operating SFU infrastructure. For private or commercial licensing requirements, use the official licensing page as the source of truth.

[Start MiroTalk Cloud](https://webrtc.mirotalk.com){ .md-button }
[Compare licensing options](../license/index.md){ .md-button .md-button--primary }
[Review the SFU commercial package](https://codecanyon.net/item/mirotalk-sfu-webrtc-realtime-video-conferences/40769970){ .md-button }

Need deployment assistance, customization, or dedicated infrastructure? [Contact MiroTalk Enterprise](../enterprise/index.md).
