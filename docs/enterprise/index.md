---
title: MiroTalk Enterprise and Commercial Services
description: Evaluate MiroTalk commercial licensing, private infrastructure, white-label delivery, integration, support, security, scaling, and procurement.
---

<header class="editorial-hero license-hero">
	<span class="editorial-kicker">Private deployment and commercial delivery</span>
	<h1>MiroTalk for enterprise</h1>
	<p>Plan a licensed, branded, integrated, and self-hosted MiroTalk deployment with explicit ownership for infrastructure, security, scale, support, and operations.</p>
	<div class="editorial-actions">
		<a class="md-button md-button--primary" href="#define-the-requirement">Plan an evaluation</a>
		<a class="md-button" href="mailto:miroslav.pejic.85@gmail.com?subject=MiroTalk%20enterprise%20enquiry">Contact MiroTalk</a>
	</div>
</header>

## Define the requirement

Start with the outcome rather than a generic feature list.

| Requirement | Decision to make | Relevant documentation |
| --- | --- | --- |
| Commercial product | Whether users pay, source remains private, and one or more end products are involved | [Licensing options](../license/index.md) |
| Private infrastructure | Which applications, regions, networks, and operating model are required | [Self-hosting overview](../self-host/index.md) |
| White-label experience | Which supported product surfaces and brand assets must change | [SFU rebranding](../mirotalk-sfu/rebranding.md) and [P2P rebranding](../mirotalk-p2p/rebranding.md) |
| Product integration | Whether direct links, embedding, APIs, webhooks, or custom work is required | [Build with MiroTalk](../build/index.md) |
| Complete platform | Whether the organization needs the full application suite | [MiroTalk Ultimate](../mirotalk-ultimate/index.md) |
| Operational assistance | Where architecture, deployment, integration, or ongoing support is needed | [Prepare your request](#prepare-your-request) |

## Commercial licensing

MiroTalk publishes open-source, Regular, and Extended licensing paths. In broad terms, Regular is the starting point for an eligible closed-source end product where end users are not charged to access it; Extended is the starting point when eligible end users can be charged. Product structure, redistribution, services, the number of end products, and other factors can affect eligibility.

The [licensing page](../license/index.md), applicable license text, and marketplace listing are the sources of truth. This enterprise page is not legal advice and does not create additional license rights.

## Deployment models

### Managed service

Use [MiroTalk Cloud](../cloud/index.md) when its available managed workflow meets the organization's requirements and operating the underlying MiroTalk infrastructure is unnecessary.

### Self-hosted deployment

Deploy selected MiroTalk applications on infrastructure controlled by the organization or its provider. This path supports private operating models and deeper adaptation, while placing deployment and operational responsibilities with the operator.

### Assisted delivery

Discuss architecture, deployment, customization, integration, or support directly when the published documentation does not cover the requirement. Scope, availability, deliverables, pricing, acceptance criteria, and support terms must be confirmed in writing.

## Responsibility model

Unless a separate agreement assigns them elsewhere, the self-hosting organization is responsible for:

- cloud or on-premises infrastructure, domains, certificates, and network services;
- identity, access control, secrets, firewall policy, and administrative access;
- configuration, deployment, monitoring, logging, backups, updates, and incident response;
- capacity planning, load testing, availability, resilience, and disaster recovery;
- privacy notices, consent, recording policy, retention, data location, and regulatory evaluation;
- end-user support and the contracts, costs, limits, and availability of third-party services.

MiroTalk documentation and services do not by themselves make a deployment compliant with a particular law, standard, or internal policy.

## Security and privacy evaluation

An enterprise review should cover the complete system around MiroTalk, not only WebRTC media transport. Evaluate:

1. authentication and authorization for users, hosts, agents, viewers, and administrators;
2. room creation, invitation, admission, and link-sharing behavior;
3. secret storage, API access, server hardening, patching, and privileged operations;
4. media, signaling, chat, files, recordings, transcripts, logs, and backups;
5. retention, deletion, data residency, subprocessors, and incident handling;
6. abuse prevention, moderation, rate limits, monitoring, and audit requirements.

Security controls differ by product and configuration. Validate the exact version and deployment rather than assuming one product's behavior applies to the complete suite.

## Scaling and availability

Capacity depends on the selected architecture, participant roles, concurrency, bitrate, video resolution, screen sharing, recording, streaming, transcription, network quality, and infrastructure. No universal server size or participant count applies to every deployment.

Use the [architecture guide](../webrtc/architectures.md) and [SFU scaling documentation](../mirotalk-sfu/scalability.md) as starting points, then load-test representative sessions. Define availability targets, failure domains, recovery objectives, monitoring, and escalation before production launch.

## Integration and customization

Use the shallowest integration that satisfies the product workflow:

- direct links for launching a supported room or role;
- iframe or widget integration for an embedded experience;
- REST APIs for supported application automation;
- webhooks for supported lifecycle events;
- custom development when the documented surfaces do not provide the required behavior.

Custom work should define ownership of source changes, compatibility, testing, deployment, updates, and long-term maintenance.

## Costs beyond licensing

Plan separately for infrastructure, bandwidth, TURN traffic, storage, backups, observability, domains, certificates, email, identity, recording, transcription, streaming, support, implementation, maintenance, taxes, and other third-party services. Their pricing and terms are controlled by their respective providers.

## Procurement checklist

Before approval, record:

- the legal entity, billing contact, deployment owner, and technical owner;
- selected products, license path, end-product model, and permitted users;
- required environments, regions, integrations, customizations, and third-party services;
- security, privacy, compliance, data-handling, and vendor-review requirements;
- acceptance criteria, delivery milestones, support scope, response expectations, and exclusions;
- infrastructure budget, ongoing operating costs, update ownership, and exit plan.

## Prepare your request

Include the MiroTalk products being evaluated, intended user workflow, deployment model, expected concurrency, integration surfaces, customization needs, target timeline, and the business or technical outcome. State which responsibilities you expect MiroTalk to cover and which your organization or implementation partner will own.

Do not send credentials, API keys, private room links, production configuration, personal data, or other secrets by email.

[Contact Miroslav Pejic](mailto:miroslav.pejic.85@gmail.com?subject=MiroTalk%20enterprise%20enquiry){ .md-button .md-button--primary }
[Review licensing options](../license/index.md){ .md-button }