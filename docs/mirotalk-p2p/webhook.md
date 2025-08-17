# Webhooks

![Webhook](../images/webhooks.png)

This guide explains how to configure and handle MiroTalk P2P webhook events such as `join` and `disconnect`.

---

### 1. Enable Webhooks

Update your `app/src/config.js` file to activate webhooks and set your endpoint:

```javascript
webhook: {
    enabled: true, // Enable webhook functionality
    url: 'http://localhost:8888/webhook-endpoint', // Webhook server URL
},
```

---

### 2. Webhook Event Structure

When an event occurs, MiroTalk P2P sends an HTTP `POST` request to your webhook endpoint with a JSON payload.

**Sample Payload:**

```json
{
    "event": "join",
    "data": {}
}
```

- **event**: The event type (`join` or `disconnect`)
- **data**: Additional event-specific information

---

For a server-side example of handling webhook events, see [this example](https://github.com/miroslavpejic85/mirotalk/tree/master/webhook).