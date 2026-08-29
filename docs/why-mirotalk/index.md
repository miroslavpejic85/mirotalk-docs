---
title: Why MiroTalk
description: Compare building WebRTC from zero with adopting MiroTalk applications, integration surfaces, self-hosting guidance, and commercial options.
---

<header class="editorial-hero license-hero">
    <span class="editorial-kicker">Build the product, not every primitive</span>
    <h1>Why build with MiroTalk?</h1>
    <p>MiroTalk provides working communication applications and documented integration paths across several WebRTC architectures. Your team can start from an existing system while retaining a self-hosted path.</p>
    <div class="editorial-actions">
        <a class="md-button md-button--primary" href="#compare-the-engineering-surface">Compare the engineering surface</a>
        <a class="md-button" href="/projects/">Choose a product</a>
    </div>
</header>

## Compare the engineering surface

| Engineering area | Build from zero | Start with MiroTalk |
| --- | --- | --- |
| Browser media experience | Design and implement call controls, device handling, room states, and collaboration features | Begin with a working product interface and adapt supported behavior |
| Media topology | Select and implement mesh, SFU, or broadcasting architecture | Choose among focused P2P, SFU, one-to-one, and broadcast applications |
| Application workflows | Build meetings, direct calls, click-to-call, broadcasting, scheduling, and administration | Select the MiroTalk application designed for the workflow |
| Product integration | Create room APIs, embedding, direct joins, and event integration | Use documented REST APIs, iframes, direct links, widgets, and webhooks where supported |
| Deployment | Define runtime, proxy, TLS, process, and update procedures | Start with product-specific self-hosting and operations guides |
| Commercial delivery | Establish packaging, branding, and license terms | Evaluate published commercial licenses, white-label documentation, and the Ultimate bundle |

MiroTalk reduces the surface your team must create from an empty repository; it does not remove product engineering or operational responsibility.

## A suite of focused architectures

MiroTalk is not one universal meeting application presented as every solution. The suite separates distinct communication models:

- **SFU** for server-routed group meetings and webinars;
- **P2P** for private mesh calls and smaller groups;
- **C2C** for focused one-to-one video rooms;
- **BRO** for broadcaster-and-viewer workflows;
- **CME** for availability and click-to-call workflows;
- **WEB** for accounts, scheduling, rooms, and invitations;
- **Admin** for managing supported MiroTalk deployments.

[Compare all products and architectures](../overview/index.md){ .md-button .md-button--primary }
[Explore the complete suite](../about/index.md){ .md-button }

## Control the deployment model

Use [MiroTalk Cloud](../cloud/index.md) when the managed service fits the workflow, or follow the [self-hosting documentation](../self-host/index.md) when the organization needs infrastructure control. Self-hosting can support private operating models and source-level adaptation, but the operator remains responsible for security, monitoring, backups, updates, capacity, resilience, and third-party services.

## Integrate at the right depth

Start with a direct room link or iframe for a short integration path. Use product APIs and webhooks when the host application needs to create rooms or react to supported events. Work from the documentation for the selected application because capabilities and contracts are not interchangeable across the suite.

[Review developer paths](../build/index.md){ .md-button .md-button--primary }
[Try the iframe guide](../utility/quick-custom-integration.md){ .md-button }

## Make the decision with evidence

Before adopting any real-time communication stack:

1. Validate the required user journey in a representative browser and network environment.
2. Choose the topology based on roles, concurrency, interaction, and media flow.
3. Review authentication, authorization, privacy, recording, retention, and abuse controls.
4. Load-test the selected deployment with representative media settings.
5. Define ownership for infrastructure, updates, monitoring, incidents, and user support.
6. Review the applicable license before distributing, rebranding, closing source, or charging users.

## Where MiroTalk fits

MiroTalk is a strong candidate when a team wants working browser communication, multiple deployment architectures, source access, and a path from embedding to a broader self-hosted platform. A fully custom implementation may still be appropriate when the required media behavior, protocol, compliance controls, or operating model differs substantially from the available applications.

[Explore business solutions](../business/index.md){ .md-button .md-button--primary }
[Review licensing options](../license/index.md){ .md-button }