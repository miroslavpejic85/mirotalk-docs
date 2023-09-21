# Exposing MiroTalk BRO with Ngrok

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
ngrokBroadcast: 'https://xxxx-xx-xx-xxx-xx.ngrok.io/broadcast?id=123&name=Broadcaster',
ngrokViewer: 'https://xxxx-xx-xx-xxx-xx.ngrok.io/viewer?id=123&name=Viewer',
```

**Step 3: Access MiroTalk**

Open one of the provided URLs in your web browser:

- To be a broadcaster, visit the `ngrokBroadcast` URL.
- To be a viewer, visit the `ngrokViewer` URL.

Choose your role and enjoy MiroTalk WebRTC Live Broadcast!

---