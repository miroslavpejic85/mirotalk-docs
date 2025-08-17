# Webhooks

![Webhook](../images/webhooks.png)

This guide explains how to configure and handle MiroTalk SFU webhook events such as `join`, `exit`, and `disconnect`.

---

### 1. Enable Webhooks

Update your `.env` file to activate webhooks and set your endpoint:

```bash
WEBHOOK_ENABLED=true
WEBHOOK_URL=https://YOUR-DOMAIN-NAME/webhook-endpoint
```

---

### 2. Webhook Event Structure

When an event occurs, MiroTalk SFU sends an HTTP `POST` request to your webhook endpoint with a JSON payload.

**Sample Payload:**

```json
{
    "event": "join",
    "data": {}
}
```

- **event**: The event type (`join`, `exit`, or `disconnect`)
- **data**: Additional event-specific information

---

For a server-side example of handling webhook events, see [this example](https://github.com/miroslavpejic85/mirotalksfu/tree/main/webhook).
