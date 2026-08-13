# MiroTalk Whisper Self-Hosting Guide

## Description

MiroTalk Whisper is a self-hosted, OpenAI-compatible speech-to-text (Speech recognition) server that powers the in-room **Whisper mode** transcription feature. It lets you transcribe meeting audio locally on your own infrastructure, so audio never leaves your server or gets sent to the OpenAI API.

It runs the [`fedirz/faster-whisper-server`](https://github.com/fedirz/faster-whisper-server) image, which exposes an OpenAI-compatible endpoint at `/v1/audio/transcriptions`. Because the API matches OpenAI's, MiroTalk can talk to your self-hosted instance exactly like it would with the official service, giving you:

- **Privacy** — audio is processed entirely on your own server.
- **No API costs** — no per-request charges from OpenAI.
- **Flexibility** — run on CPU (any VPS/VDS) or GPU (NVIDIA + `nvidia-container-toolkit`) and choose the model size that best fits your accuracy and performance needs (`tiny`, `base`, `small`, `medium`, `large-v3`).

## Requirements

- Server Selection:
    - [Hetzner](https://www.hetzner.com/cloud) - Use [this link](https://hetzner.cloud/?ref=XdRifCzCK3bn) to receive `€⁠20 in cloud credits`
    - [Netcup](https://www.netcup.com/en/?ref=309627)
    - [Hostinger](https://hostinger.com/?REFERRALCODE=MIROTALK)
    - [Contabo](https://www.dpbolvw.net/click-101027391-14462707)
- OS: Ubuntu 22.04 LTS.
- [Node.js](https://nodejs.org/en/) (LTS) and npm
- Domain or Subdomain Name (e.g., `YOUR.DOMAIN.NAME`) with a DNS A record pointing to your server's IPv4 address.

---

## Installation

![docker](../images/docker.png)

```bash
# Install Docker and Docker Compose
sudo apt install -y docker.io
sudo apt install -y docker-compose

```

Example of `docker-compose-whisper.yml`:

```yaml 
services:
    # -------------------------------------------------------------------------
    # CPU variant — runs anywhere, no GPU required.
    # -------------------------------------------------------------------------
    whisper:
        image: fedirz/faster-whisper-server:latest-cpu
        container_name: mirotalkwhisper
        hostname: whisper
        restart: unless-stopped
        profiles: ['cpu']
        ports:
            # Host 8000 -> container 8000 (matches WHISPER default basePath).
            - '${WHISPER_PORT:-8000}:8000'
        environment:
            # Model downloaded on first run and cached in the volume below.
            # Smaller = faster/less RAM, larger = more accurate.
            # Options: tiny | base | small | medium | large-v3 (Systran/faster-whisper-*)
            WHISPER__MODEL: '${WHISPER_MODEL:-Systran/faster-whisper-small}'
            WHISPER__INFERENCE_DEVICE: 'cpu'
        volumes:
            - whisper_cache:/root/.cache/huggingface

    # -------------------------------------------------------------------------
    # GPU variant — requires an NVIDIA GPU and nvidia-container-toolkit.
    # -------------------------------------------------------------------------
    whisper-gpu:
        image: fedirz/faster-whisper-server:latest-cuda
        container_name: mirotalkwhisper
        hostname: whisper
        restart: unless-stopped
        profiles: ['gpu']
        ports:
            - '${WHISPER_PORT:-8000}:8000'
        environment:
            WHISPER__MODEL: '${WHISPER_MODEL:-Systran/faster-whisper-medium}'
            WHISPER__INFERENCE_DEVICE: 'cuda'
        volumes:
            - whisper_cache:/root/.cache/huggingface
        deploy:
            resources:
                reservations:
                    devices:
                        - driver: nvidia
                          count: all
                          capabilities: [gpu]

volumes:
    whisper_cache:
        driver: local
```

```bash
# CPU mode
docker compose -f docker-compose-whisper.yml --profile cpu up -d
# GPU mode
docker compose -f docker-compose-whisper.yml --profile gpu up -d
```

Verify the installation: [http://YOUR.DOMAIN.NAME:8000](http://YOUR.DOMAIN.NAME:8000)

---

## Configuring Nginx & Certbot

![nginx](../images/nginx.png)

To expose MiroTalk Whisper over HTTPS without the port number (encrypted communication is required so the OpenAI-compatible API can be reached securely), install [Nginx](https://www.nginx.com) and [Certbot](https://certbot.eff.org):

```bash
# Install Nginx
sudo apt-get install -y nginx

# Install Certbot (SSL certificates)
sudo apt install -y snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Configure Nginx
sudo vim /etc/nginx/sites-enabled/default
```

Add the following:

```bash
# HTTP — redirect all traffic to HTTPS
server {
    listen 80;
    listen [::]:80;
    server_name YOUR.DOMAIN.NAME;

    return 301 https://$host$request_uri;
}
```

```bash
# Test Nginx configuration
sudo nginx -t

# Enable HTTPS with Certbot (follow the prompts)
sudo certbot certonly --nginx

# Add Let's Encrypt configuration to Nginx
sudo vim /etc/nginx/sites-enabled/default
```

Add the following:

```bash
# MiroTalk Whisper - HTTPS — proxy all requests to the Whisper server
server {
    # Enable HTTP/2
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name YOUR.DOMAIN.NAME;

    # Use the Let’s Encrypt certificates
    ssl_certificate /etc/letsencrypt/live/YOUR.DOMAIN.NAME/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/YOUR.DOMAIN.NAME/privkey.pem;

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_pass http://localhost:8000/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        # Optional: increase buffers to accommodate large headers/cookies.
        # May be required with some OIDC / SSO providers (e.g. Azure AD/Entra,
        # Keycloak with many group claims) whose tokens exceed nginx defaults.
        proxy_buffer_size       128k;
        proxy_buffers         8 256k;
        proxy_busy_buffers_size 512k;
    }
}
```

```bash
# Test Nginx configuration again
sudo nginx -t

# Restart Nginx
service nginx restart
service nginx status

# Set up auto-renewal for SSL certificates
sudo certbot renew --dry-run --cert-name YOUR.DOMAIN.NAME

# Show certificates
sudo certbot certificates
```

Verify your MiroTalk Whisper instance: [https://YOUR.DOMAIN.NAME](https://YOUR.DOMAIN.NAME)

---

## Apache Virtual Host (Alternative to Nginx)

![apache](../images/apache.png)

If you prefer `Apache`, configure it with the equivalent settings provided in this guide.

```bash
# Install Apache with Certbot
apt install python3-certbot-apache -y

# Set up SSL
certbot --apache --non-interactive --agree-tos -d YOUR.DOMAIN.NAME -m your.email.address

# Edit the Apache site configuration
sudo vim /etc/apache2/sites-enabled/YOUR.DOMAIN.NAME.conf
```

Add the following:

```bash
# HTTP — redirect all traffic to HTTPS
<VirtualHost *:80>
    ServerName YOUR.DOMAIN.NAME
    Redirect permanent / https://YOUR.DOMAIN.NAME
</VirtualHost>

# MiroTalk Whisper - HTTPS — proxy all requests to the Whisper server
<VirtualHost *:443>
    ServerName YOUR.DOMAIN.NAME

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/YOUR.DOMAIN.NAME/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/YOUR.DOMAIN.NAME/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf

    # Enable HTTP/2 support
    Protocols h2 http/1.1

    <Location />
        # Proxy Configuration for the Whisper server
        ProxyPass http://localhost:8000/
        ProxyPassReverse http://localhost:8000/

        ProxyPreserveHost On

        RequestHeader set X-Forwarded-For "%{REMOTE_ADDR}s"
        RequestHeader set X-Forwarded-Proto "https"
        RequestHeader set Host "%{HTTP_HOST}s"
    </Location>
</VirtualHost>
```

```bash
# Check configuration
sudo apache2ctl configtest

sudo a2enmod proxy # Enables the `mod_proxy` module, which is essential for proxying HTTP connections.
sudo a2enmod proxy_http # Enables the `mod_proxy_http` module, which adds support for proxying HTTP connections.

# Restart apache
sudo systemctl restart apache2
```
