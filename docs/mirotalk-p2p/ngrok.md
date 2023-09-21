# Exposing MiroTalk P2P with Ngrok

To make MiroTalk accessible from outside your `local PC` via `HTTPS` using `Ngrok`, follow these steps:

**Step 1: Configure Ngrok**

- Visit [ngrok.com](https://ngrok.com)
- Sign up for a free account.
- Replace `YourNgrokAuthToken` with [your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)

Open the `.env` file and make the following adjustments:

```bash
NGROK_ENABLED=true
NGROK_AUTH_TOKEN=YourNgrokAuthToken
```

**Step 2: Start MiroTalk**

When you run MiroTalk with `npm start`, you'll see a line in the console log like this:

```bash
server_tunnel: 'https://xxxxxxxxxxxxxxxxxx.ngrok.io'
```

**Step 3: Access MiroTalk**

Open the provided URL in your web browser. You can now join a room, share the link with others, and wait for participants to join.

---