# Exposing MiroTalk C2C with Ngrok

To make MiroTalk accessible from outside your `local PC` via `HTTPS` using `Ngrok`, follow these steps:

**Step 1: Configure Ngrok**

- Visit [ngrok.com](https://ngrok.com)
- Sign up for a free account.
- Replace `YourNgrokAuthToken` with [your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken)

Open the `.env` file and update the Ngrok settings as follows:

```bash
NGROK_ENABLED=true
NGROK_AUTH_TOKEN=YourNgrokAuthToken
```

**Step 2: Run MiroTalk**

Start MiroTalk with `npm start`. After running the command, you will see the following lines in the console log:

```bash
ngrokHome: 'https://xxxx-xx-xx-xxx-xx.ngrok.io',
ngrokRoom: 'https://xxxx-xx-xx-xxx-xx.ngrok.io/?room=test',
ngrokJoin: 'https://xxxx-xx-xx-xxx-xx.ngrok.io/join?room=test&name=test',
```

**Step 3: Access MiroTalk**

Open the provided URL in your web browser. You can now join a room, click the "Share" button to obtain the URL, and share it with others. Wait for participants to join your MiroTalk C2C session.

---
