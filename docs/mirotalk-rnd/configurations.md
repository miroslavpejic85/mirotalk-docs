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

## Reports and bans (community moderation)

Users can report their partner. When `REPORT_BAN_THRESHOLD` different IPs report the same IP within `REPORT_WINDOW_HOURS`, that IP is banned for `BAN_DURATION_HOURS`. Repeat bans double in length (max 30 days). Set `REPORT_BAN_THRESHOLD=0` to disable reporting.

| Variable | Purpose | Default |
| --- | --- | --- |
| `REPORT_BAN_THRESHOLD` | Number of different IPs that must report the same IP to trigger a ban; `0` disables reporting | `3` |
| `REPORT_WINDOW_HOURS` | Time window in which reports are counted | `24` |
| `BAN_DURATION_HOURS` | Length of the first ban; repeat bans double in length (max 30 days) | `24` |

!!! note "Ban storage"

    Bans live in memory unless `REDIS_URL` is set, so a single instance without Redis forgets them on restart.

!!! warning "Behind a reverse proxy"

    IP detection follows `X-Forwarded-For` only for proxies trusted via `TRUST_PROXY`. Set `TRUST_PROXY` correctly when behind a reverse proxy, or every user appears to have the proxy's IP.

## Multi-instance matchmaking

Multi-instance matchmaking is optional and disabled by default. Set the same `REDIS_URL` on every instance to match users across instances. `MAX_ACTIVE_USERS` and `MAX_CONNECTIONS_PER_IP` remain per instance, while `MAX_QUEUE_USERS` becomes global. When running behind a load balancer, enable sticky sessions if Socket.IO long-polling is enabled.

| Variable | Purpose | Default |
| --- | --- | --- |
| `REDIS_URL` | Redis connection URL shared by all instances for cross-instance matchmaking | *(empty; disabled)* |
| `SOCKET_WEBSOCKET_ONLY` | Use WebSocket transport only, avoiding the need for sticky sessions; users on networks that block WebSockets cannot connect | `false` |
| `SKIP_AVOID_SAME_PARTNER` | Prevent users from being immediately re-matched with each other after a skip; when `false`, they may be paired again if nobody else is waiting | `false` |

## STUN and TURN

| Variable | Purpose |
| --- | --- |
| `STUN_URLS` | Comma-separated STUN servers |
| `TURN_URLS` | Comma-separated TURN server URLs |
| `TURN_USERNAME` | TURN username |
| `TURN_PASSWORD` | TURN password |

## Sentry error reporting

Error reporting with [Sentry](https://sentry.io) is optional and disabled by default. Set `SENTRY_ENABLED=true` and provide `SENTRY_DSN` to enable it. See [`.env.template`](https://github.com/miroslavpejic85/mirotalkrnd/blob/main/.env.template) for the complete configuration.

| Variable | Purpose | Default |
| --- | --- | --- |
| `SENTRY_ENABLED` | Enable Sentry error reporting | `false` |
| `SENTRY_DSN` | Sentry project data source name | *(empty)* |
| `SENTRY_ENVIRONMENT` | Environment name reported to Sentry | `NODE_ENV` |
| `SENTRY_RELEASE` | Release identifier reported to Sentry | *(empty)* |
| `SENTRY_TRACES_SAMPLE_RATE` | Performance tracing sample rate, from `0` to `1` | `0` |

PII, request headers and bodies, and user data are stripped before events are sent.

## Umami analytics

Umami analytics is optional and disabled by default. When enabled, the privacy policy is updated automatically. See [`.env.template`](https://github.com/miroslavpejic85/mirotalkrnd/blob/main/.env.template) for the complete configuration.

| Variable | Purpose | Default |
| --- | --- | --- |
| `UMAMI_ENABLED` | Enable Umami analytics | `false` |
| `UMAMI_SCRIPT_URL` | URL of the Umami tracking script | `https://analytics.example.com/script.js` |
| `UMAMI_WEBSITE_ID` | Umami website identifier | *(empty)* |
| `UMAMI_DOMAINS` | Optional comma-separated hostnames to track | *(all hostnames)* |
| `UMAMI_DO_NOT_TRACK` | Honor the browser's Do Not Track setting | `true` |

!!! note "Apply changes"

    Restart the process after updating `.env` so new values are loaded.
