# MiroTalk RND Configuration

MiroTalk RND uses `.env` for server behavior, metadata, WebRTC network fallback, and protection limits.

Start by copying the template:

```bash
cp .env.template .env
```

Reference: [`.env.template` in mirotalkrnd](https://github.com/miroslavpejic85/mirotalkrnd/blob/main/.env.template)

## Core options

| Variable | Purpose | Example |
| --- | --- | --- |
| `APP_OFFLINE` | Toggle maintenance/offline mode | `false` |
| `APP_NAME` | Application display name | `Random Talk` |
| `REPORT_EMAIL` | Support/contact email | `support@example.com` |
| `OFFLINE_MESSAGE` | Message shown when offline mode is enabled | `We are currently offline...` |

## Social preview metadata

| Variable | Purpose |
| --- | --- |
| `OG_TITLE` | Open Graph title |
| `OG_DESCRIPTION` | Open Graph description |
| `OG_IMAGE` | Preview image path |
| `OG_URL` | Canonical app URL |
| `TWITTER_CARD` | Twitter card type |

## Server and TLS

| Variable | Purpose | Example |
| --- | --- | --- |
| `NODE_ENV` | Runtime mode | `development` or `production` |
| `PORT` | HTTP/HTTPS server port | `4010` |
| `USE_HTTPS` | Enable built-in HTTPS listener | `false` |
| `SSL_KEY_PATH` | Local path to TLS private key | `./ssl/key.pem` |
| `SSL_CERT_PATH` | Local path to TLS certificate | `./ssl/cert.pem` |

## Capacity and abuse protection

| Variable | Purpose | Default |
| --- | --- | --- |
| `MAX_ACTIVE_USERS` | Maximum concurrent connected users | `200` |
| `MAX_QUEUE_USERS` | Maximum waiting users in queue | `200` |
| `MAX_CONNECTIONS_PER_IP` | Max parallel connections allowed per IP | `5` |
| `SKIP_RATE_LIMIT_PER_10S` | Skip/next actions allowed per 10 seconds | `8` |
| `API_RATE_LIMIT_WINDOW_MS` | API rate-limit window duration | `60000` |
| `API_RATE_LIMIT_MAX_REQUESTS` | Max requests per rate-limit window | `120` |

## STUN and TURN

| Variable | Purpose |
| --- | --- |
| `STUN_URLS` | Comma-separated STUN servers |
| `TURN_URLS` | Comma-separated TURN server URLs |
| `TURN_USERNAME` | TURN username |
| `TURN_PASSWORD` | TURN password |

!!! note "Apply changes"

    Restart the process after updating `.env` so new values are loaded.

