---
title: Self-host MiroTalk
description: Deploy and operate MiroTalk on your own infrastructure with product-specific installation, configuration, networking, scaling, and update guides.
---

# Self-host MiroTalk

Run MiroTalk on infrastructure you control. Choose the product architecture first, then follow its deployment and configuration guides.

## Choose what to deploy

| Goal | Product | Deployment guide |
| --- | --- | --- |
| Scalable meetings, classes, and webinars | MiroTalk SFU | [Self-host SFU](../mirotalk-sfu/self-hosting.md) |
| Private calls and small group meetings | MiroTalk P2P | [Self-host P2P](../mirotalk-p2p/self-hosting.md) |
| Focused one-to-one video calls | MiroTalk C2C | [Self-host C2C](../mirotalk-c2c/self-hosting.md) |
| One-to-many broadcasting | MiroTalk BRO | [Self-host BRO](../mirotalk-bro/self-hosting.md) |
| Click-to-call support | MiroTalk CME | [Self-host CME](../mirotalk-cme/self-hosting.md) |
| Scheduling, invitations, and room management | MiroTalk WEB | [Self-host WEB](../mirotalk-web/self-hosting.md) |
| Server and configuration administration | MiroTalk Admin | [Self-host Admin](../mirotalk-admin/self-hosting.md) |

[Compare WebRTC architectures](../webrtc/architectures.md){ .md-button }
[Use automated installation scripts](../scripts/about.md){ .md-button }

## Prepare the infrastructure

- [Install and configure Coturn](../coturn/installation.md) for TURN connectivity where required.
- [Install Docker Compose](../utility/docker-compose.md) when using container-based deployment.
- [Manage Node.js with NVM](../utility/nvm.md).
- [Use ngrok for local development](../ngrok/ngrok.md).
- [Deploy with Cloudron](../cloudron/cloudron.md).

## Operate and scale

- Review each product's [configuration guides](#choose-what-to-deploy) after installation.
- Follow the [SFU scalability guide](../mirotalk-sfu/scalability.md) before planning larger deployments.
- Use the product-specific update guide or script and prepare backups before changing a deployment.
- Review host protection for [SFU](../mirotalk-sfu/host-protection.md) or [P2P](../mirotalk-p2p/host-protection.md) where applicable.

## Prefer a managed service?

MiroTalk Cloud is powered by MiroTalk WEB and removes the need to deploy, update, monitor, and scale the service yourself.

[Start MiroTalk Cloud](https://webrtc.mirotalk.com){ .md-button .md-button--primary }
[Compare Cloud and self-hosting](../cloud/index.md){ .md-button }