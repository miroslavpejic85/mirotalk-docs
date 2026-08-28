---
title: MiroTalk WEB REST API
description: Explore the MiroTalk WEB API for users, rooms, bookings, invitations, and application integrations through its OpenAPI documentation.
---

# MiroTalk WEB REST API

![MiroTalk WEB REST API documentation](../images/api.png)

MiroTalk WEB publishes an OpenAPI contract for account, room, booking, invitation, and integration workflows. Use the interactive documentation to inspect the request schema, authentication requirement, response model, and status codes for a specific operation.

[Open the WEB Swagger documentation](https://webrtc.mirotalk.com/api/v1/docs){ .md-button .md-button--primary }
[Review WEB integration options](integration.md){ .md-button }

The deployed specification currently identifies itself as **MiroTalk WebRTC admin API 1.0.0** using OpenAPI 3.0. A self-hosted instance exposes its contract at:

```text
https://YOUR-DOMAIN-NAME/api/v1/docs
```

## API areas

| Area | Typical operations |
| --- | --- |
| **User** | Create and confirm accounts, sign in, change passwords, invite users, and manage user records. |
| **Room** | Create, retrieve, update, and delete rooms; manage invitations and attendee responses. |
| **Booking** | Publish booking profiles, list slots, create bookings, and manage guest cancellation. |
| **Integration API** | Check authentication and room access, list allowed rooms, verify rooms, and send invitations. |

This table is an orientation aid rather than a complete endpoint inventory. Swagger is the source of truth for the current methods and schemas.

## Before you begin

1. Open Swagger on the same WEB deployment you intend to integrate.
2. Select an operation and review its security requirements.
3. Use the documented example schema to build the request.
4. Test with a non-production account and room.
5. Handle every documented success and error response before enabling production traffic.

!!! warning "Protect credentials and tokens"
	Do not embed administrator credentials, session tokens, API secrets, confirmation tokens, or cancellation tokens in public client code. Route privileged operations through a trusted backend and grant only the access required for the workflow.

## Validate an integration

Confirm at least these behaviors before deployment:

- The request uses the method and content type shown in Swagger.
- Authentication is supplied only through the documented mechanism.
- IDs, slugs, and tokens are URL-encoded where required.
- Validation, authentication, authorization, not-found, and server errors are handled.
- Retries do not create duplicate users, rooms, invitations, or bookings.
- Logs omit passwords, session data, API secrets, and URL tokens.

## Related documentation

- [MiroTalk WEB overview](index.md)
- [Embed MiroTalk WEB](integration.md)
- [Configure MiroTalk WEB](configurations.md)
- [Self-host MiroTalk WEB](self-hosting.md)
- [SaaS billing with Stripe](stripe.md)
- [Build with MiroTalk](../build/index.md)
