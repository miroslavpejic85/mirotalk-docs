# Exposing MiroTalk RND with ngrok

Use ngrok to expose a local MiroTalk RND server over HTTPS for remote testing.

## Step 1: Configure ngrok

- Create an account at [ngrok.com](https://ngrok.com)
- Get your auth token from the ngrok dashboard
- In `.env`, set:

```bash
PORT=4010
```

Start RND locally:

```bash
npm start
```

## Step 2: Start ngrok tunnel

In a separate terminal:

```bash
ngrok http 4010
```

ngrok prints a public HTTPS URL such as:

```text
https://xxxx-xx-xx-xxx-xx.ngrok-free.app
```

## Step 3: Test remote access

Open the ngrok HTTPS URL in a browser and test random matching from another device/network.

!!! warning "Temporary URL"

    Free ngrok URLs can change between restarts. Update any shared links each time you create a new tunnel.

