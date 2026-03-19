# Frequently Asked Questions

---

## General

??? question "What is MiroTalk?"

    MiroTalk is an open-source, self-hosted suite of **WebRTC-based** applications for real-time video conferencing, live broadcasting, and communication. It includes multiple products designed for different use cases — from one-on-one calls to large-scale meetings and live streaming.

    - 🏆 **MiroTalk SFU** — Group video conferencing (large meetings, webinars)
    - 🚀 **MiroTalk P2P** — Peer-to-peer video calls (small groups)
    - ✨ **MiroTalk C2C** — Client-to-client cam-2-cam communication
    - 📡 **MiroTalk BRO** — One-to-many live broadcasting
    - 🛠 **MiroTalk WEB** — Meeting room scheduler and manager
    - ⚙️ **MiroTalk ADMIN** — Centralized dashboard to manage all instances

??? question "What is WebRTC?"

    **WebRTC** (Web Real-Time Communication) is an open-source technology that enables real-time audio, video, and data communication directly in web browsers without requiring plugins or additional software. MiroTalk is built entirely on top of WebRTC.

??? question "What are the differences between Mesh, SFU, and MCU architectures?"

    - **Mesh (P2P):** Each participant connects directly to every other participant. Low latency but bandwidth and CPU usage grow with more participants. Best for 2–4 users.
    - **SFU (Selective Forwarding Unit):** A central server receives all streams and selectively forwards them to participants. Reduced bandwidth per participant, ideal for 5+ users.
    - **MCU (Multipoint Control Unit):** The server mixes all streams into a single composite stream. Most resource-intensive on the server side.

    MiroTalk uses **Mesh** (P2P, C2C, BRO) and **SFU** architectures.

---

## Products

??? question "Which MiroTalk product should I choose?"

    | Product | Best For | Max Users | Architecture |
    |---------|----------|-----------|--------------|
    | **SFU** | Large meetings, webinars, conferences | 50–1000+ (with scaling) | Selective Forwarding Unit |
    | **P2P** | Small group calls, embedded apps | 2–4 participants | Peer-to-Peer (Mesh) |
    | **C2C** | Private cam-2-cam, direct messaging | 2 participants | Peer-to-Peer (Mesh) |
    | **BRO** | Live broadcasting, one-to-many streaming | 1 broadcaster + viewers | Peer-to-Peer (Mesh) |
    | **WEB** | Meeting scheduling and management | N/A (scheduler) | Web-based |

    For large group calls and scalability, choose **SFU**. For lightweight, low-latency small calls, choose **P2P**.

??? question "How many users can MiroTalk SFU handle?"

    MiroTalk SFU supports both **vertical** and **horizontal** scaling:

    **Vertical Scaling (Single Server):**

    - 4-core CPU: ~400 users
    - 8-core CPU: ~800 users
    - 16-core CPU: ~1600 users
    - Formula: `numWorkers × ~100 users`

    **Horizontal Scaling (Multiple Servers):**

    - Multiple SFU servers behind a load balancer (Nginx/HAProxy)
    - Uses consistent hashing on room parameters for sticky sessions
    - Example: 3 servers × 800 users = 2400+ total users

??? question "Can MiroTalk BRO handle large-scale broadcasts?"

    MiroTalk BRO uses a **Peer-to-Peer (Mesh)** architecture, so it works best for **small audiences**. For large-scale live streaming, consider using **MiroTalk SFU** with **RTMP streaming** to platforms like YouTube or Twitch.

??? question "What is MiroTalk WEB?"

    MiroTalk WEB is a browser-based **meeting room scheduler** that lets you organize and manage meetings. It integrates links to all MiroTalk products, uses a MongoDB backend for storing meeting/room data, and optionally supports email verification. Default port: `9000`.

??? question "What is MiroTalk ADMIN?"

    MiroTalk ADMIN is a centralized dashboard for managing all your MiroTalk instances. It supports:

    - Starting, stopping, and restarting services
    - Updating all products
    - Editing configurations
    - Managing via **SSH**, **Docker**, or **PM2**

---

## Self-Hosting & Deployment

??? question "How can I self-host MiroTalk?"

    MiroTalk supports multiple deployment methods:

    1. **Manual (Node.js):** Clone the repo, configure `.env` and `config.js`, run with `npm start`. Recommended OS: Ubuntu 22.04 LTS.
    2. **Docker / Docker Compose:** Pre-built images on Docker Hub. Recommended for production.
    3. **PM2 Process Manager:** Keeps services running with auto-restart on failure.
    4. **Cloudron:** One-click deployment with automatic updates and backups.
    5. **Bash Scripts:** Automated install/uninstall/update scripts available for each product.

??? question "What are the server requirements?"

    - **OS:** Ubuntu 22.04 LTS (recommended)
    - **Runtime:** Node.js LTS + npm
    - **SFU additional:** Ports `40000-40100` (TCP & UDP) for media traffic
    - **Reverse proxy:** Nginx or Apache with SSL (Let's Encrypt via Certbot)
    - **TURN server:** Recommended for production (coturn)

    Default ports:

    | Product | Port |
    |---------|------|
    | P2P     | 3000 |
    | SFU     | 3010 |
    | BRO     | 3016 |
    | C2C     | 8080 |
    | WEB     | 9000 |

??? question "How do I deploy MiroTalk with Docker Compose?"

    Each MiroTalk product provides a `docker-compose.yml` template. For SFU, note that `network_mode: 'host'` is required for optimal WebRTC performance. Pull the pre-built images from Docker Hub, configure your `.env` file, and run:

    ```bash
    docker-compose up -d
    ```

    Refer to the [Docker Compose](../utility/docker-compose.md) utility page for details.

??? question "Can I deploy MiroTalk on Cloudron?"

    Yes. MiroTalk supports **Cloudron** for one-click deployment with automatic updates, backups, and integrated user management. See the [Cloudron](../cloudron/cloudron.md) guide for setup instructions.

??? question "How do I use a reverse proxy (Nginx/Apache) with MiroTalk?"

    Configure Nginx or Apache as a reverse proxy to:

    - Run MiroTalk on any port while accessing it without a port number
    - Enable **SSL/TLS** encryption (via Let's Encrypt / Certbot)
    - Support **WebSocket** connections (required for signaling)
    - Enable **HTTP/2** for better performance

    Each product's self-hosting guide includes sample Nginx configuration.

---

## STUN & TURN Servers

??? question "What are STUN and TURN servers, and why do I need them?"

    - **STUN** (Session Traversal Utilities for NAT): Discovers your public IP and port to help establish direct peer-to-peer connections. It does **not** relay media traffic.
    - **TURN** (Traversal Using Relays Around NAT): Acts as an intermediary to relay media traffic when a direct connection fails (e.g., behind restrictive firewalls or symmetric NATs).

    For production deployments, a **TURN server** is recommended to ensure connectivity for all users. See the [STUN & TURN](../coturn/stun-turn.md) guide for more details.

??? question "How do I set up a TURN server with coturn?"

    [Coturn](../coturn/installation.md) is the recommended open-source STUN/TURN server:

    1. Install coturn on your server (Docker or manual installation)
    2. Obtain an SSL certificate (Let's Encrypt / Certbot)
    3. Configure `/etc/turnserver.conf` with your domain, credentials, and ports
    4. Secure it by blocking private IPs, using strong credentials, and running as a dedicated user

    Ports used:

    - STUN: `3478` (UDP/TCP)
    - TURNS: `5349` (TLS-encrypted)

---

## Configuration

??? question "What configuration files does MiroTalk use?"

    All MiroTalk products use two main configuration files:

    1. **`config.js`** — Non-sensitive settings: application behavior, features, branding, API settings.
    2. **`.env`** — Sensitive credentials: API keys, secrets, database URLs. Stored in `.gitignore`.

    Refer to each product's [configurations](../mirotalk-sfu/configurations.md) page for available options.

??? question "What are the critical SFU configuration settings?"

    Key `.env` settings for MiroTalk SFU:

    ```bash
    ENVIRONMENT=production
    SFU_ANNOUNCED_IP=Your_Server_IP_or_Domain
    SFU_MIN_PORT=40000
    SFU_MAX_PORT=40100
    SFU_NUM_WORKERS=<CPU_core_count>
    SFU_SERVER=true
    API_KEY_SECRET=your_secret
    ```

    Ensure firewall rules allow:

    - Port `3010/TCP` (HTTP/signaling)
    - Ports `40000-40100` (TCP & UDP, RTC media)

---

## API & Integration

??? question "Does MiroTalk have a REST API?"

    Yes. All MiroTalk products expose a **REST API** with endpoints such as:

    - `/api/v1/stats` — Get active rooms and user count
    - `/api/v1/meetings` — List active meetings
    - Swagger docs at `/api/v1/docs`

    Authentication uses an `API_KEY_SECRET` header. Code examples are provided in JavaScript, PHP, Python, and Bash.

??? question "How can I embed MiroTalk in my website?"

    MiroTalk supports multiple integration methods:

    **Simple iframe:**

    ```html
    <iframe
      allow="camera; microphone; display-capture; autoplay; clipboard-write"
      src="https://your-domain.com/newroom"
      style="width: 100vw; height: 100vh; border: 0px;">
    </iframe>
    ```

    **IframeAPI:** Full programmatic control with JavaScript.

    **Widget.js:** A support-style widget with drag, online status, and custom headers.

    Configurable parameters include: `room`, `name`, `avatar`, `audio`, `video`, `screen`, `chat`, `hide`, `notify`, `token`.

    See each product's [integration](../mirotalk-sfu/integration.md) page for details.

---

## Features

??? question "Can I live stream to YouTube or Twitch with MiroTalk?"

    Yes, **MiroTalk SFU** supports **RTMP streaming** to platforms like YouTube, Twitch, and others. Two server options are available:

    1. **Node Media Server** — With admin dashboard and API
    2. **Nginx RTMP** — Lightweight option

    Both require **FFmpeg**. See the [RTMP](../mirotalk-sfu/rtmp.md) guide for setup.

??? question "What is Host Protection?"

    Host Protection adds authentication to your MiroTalk rooms:

    - `HOST_PROTECTED=true` — Require login to create rooms
    - `HOST_USER_AUTH=true` — Require login for all participants
    - **JWT tokens** for direct room access (configurable expiration, default: 1 hour)

    See the host protection guides for [P2P](../mirotalk-p2p/host-protection.md) and [SFU](../mirotalk-sfu/host-protection.md).

??? question "Does MiroTalk support Webhooks?"

    Yes. MiroTalk can send HTTP POST notifications to a configured endpoint on events such as:

    - `join` — A user joins a room
    - `disconnect` — A user leaves a room

    The payload includes event type and relevant data in JSON format. See the webhook guides for [P2P](../mirotalk-p2p/webhook.md) and [SFU](../mirotalk-sfu/webhook.md).

??? question "Can I rebrand MiroTalk with my own logo and colors?"

    Yes, rebranding is available with a **Regular** or **Extended** license:

    - **HTML Injection mode:** Customize text and labels via `config.js`
    - **Full customization:** Edit frontend files directly (landing page, room pages, Open Graph tags)

    See the rebranding guides for [P2P](../mirotalk-p2p/rebranding.md) and [SFU](../mirotalk-sfu/rebranding.md).

---

## Licensing

??? question "What are the licensing options for MiroTalk?"

    MiroTalk offers **three licensing tiers**:

    | License | Price | Use Case | Source Code |
    |---------|-------|----------|-------------|
    | **AGPLv3** | Free | Open-source, modifications must be shared publicly | Public |
    | **Regular** | $39–$299 | Personal or closed-source (non-commercial) | Private |
    | **Extended** | $199–$1499 | Commercial / revenue-generating use | Private |

    **Pricing by product:**

    | Product | Regular | Extended |
    |---------|---------|----------|
    | ULTIMATE Bundle | $299 | $1499 |
    | SFU | $99 | $499 |
    | P2P | $79 | $499 |
    | C2C | $69 | $249 |
    | BRO | $59 | $249 |
    | WEB | $39 | $199 |

    See the [Licensing Options](../license/licensing-options.md) page for full details.

---

## Troubleshooting

??? question "My video/audio is not working. What should I check?"

    1. **Browser permissions:** Ensure the browser has granted camera and microphone access.
    2. **HTTPS:** WebRTC requires a secure context (`https://` or `localhost`). Make sure your server has a valid SSL certificate.
    3. **TURN server:** If connections fail behind firewalls or NATs, configure a TURN server (coturn recommended).
    4. **Firewall rules:** Ensure the required ports are open (signaling port + media port range for SFU).
    5. **Browser compatibility:** Use a modern browser (Chrome, Firefox, Edge, Safari).

??? question "How do I update MiroTalk to the latest version?"

    **Manual installation:**

    ```bash
    git pull
    npm ci
    ```

    **Docker:**

    ```bash
    docker-compose pull
    docker-compose up -d
    ```

    **Scripts:** Use the provided update scripts (e.g., `sfu-update.sh`, `p2p-update.sh`).

    **MiroTalk ADMIN:** Use the centralized dashboard to update all instances at once.

??? question "How do I test MiroTalk locally without a domain or SSL?"

    Use **ngrok** to create a secure tunnel from your local machine to a public HTTPS URL:

    ```bash
    ngrok http 3000
    ```

    This is useful for development, webhook testing, and sharing demos. See the [Ngrok](../ngrok/ngrok.md) guide for setup.
