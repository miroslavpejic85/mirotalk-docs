# Self-hosted RustDesk + MiroTalk SFU Remote Control

MiroTalk only brokers the consent handshake (ID + one-time password). The actual remote session runs through the RustDesk clients and your own RustDesk server. No MiroTalk code changes are needed, only `.env` settings (requires MiroTalk SFU v2.6.14 or newer for the built-in setup page).

## Automated setup (optional)

On a clean **Ubuntu 22.04 / 24.04** server, as root, the [install, update and uninstall scripts](../scripts/about.md#rustdesk) automate steps 1-3 (deploy the server, open the ufw ports and print the public key):

```bash
wget -qO rustdesk-install.sh https://docs.mirotalk.com/scripts/rustdesk/rustdesk-install.sh \
  && chmod +x rustdesk-install.sh \
  && ./rustdesk-install.sh
```

Or follow the manual steps below.

## 1. Deploy the RustDesk server

On your server:

```bash
mkdir -p ~/rustdesk && cd ~/rustdesk

# Choose ONE (both write to compose.yml):
wget rustdesk.com/oss.yml -O compose.yml     # Free / open source
# wget rustdesk.com/pro.yml -O compose.yml   # Pro (requires license)

docker compose up -d
docker compose ps
```

## 2. Open firewall ports

| Port        | Protocol | Purpose                    |
|-------------|----------|----------------------------|
| 21115       | TCP      | NAT type test              |
| 21116       | TCP+UDP  | ID server / registration   |
| 21117       | TCP      | Relay server               |
| 21118-21119 | TCP      | Web client (optional)      |
| 21114       | TCP      | Pro web console (Pro only) |

Example (ufw):

```bash
sudo ufw allow 21115:21119/tcp
sudo ufw allow 21116/udp
# Pro only:
sudo ufw allow 21114/tcp
```

## 3. Get the public key

```bash
docker compose logs hbbs | grep -i key
# or read the file from the data volume:
cat ./data/id_ed25519.pub
```

(The path may differ depending on the compose file volume.)

## 4. Configure every RustDesk client (presenter AND participant)

RustDesk → Settings → Network → ID/Relay Server:

- **ID Server:** `rustdesk.yourdomain.com` (or server IP)
- **Relay Server:** same host (or leave empty)
- **Key:** contents of `id_ed25519.pub`

Both sides must use the same server, otherwise the ID will not resolve.
Participants can also get these values from the MiroTalk setup page (see step 5), so they don't need to type them by hand.
Optional: build or distribute a preconfigured client so participants don't need to enter anything (the Pro option, or a self-compiled OSS client).

## 5. Configure MiroTalk SFU

In `.env`:

```env
REMOTE_CONTROL_ENABLED=true

# Self-hosted RustDesk server, shown to participants on the built-in setup page (/remote-control/setup)
REMOTE_CONTROL_SERVER_HOST=rustdesk.yourdomain.com   # ID server (or server IP)
REMOTE_CONTROL_SERVER_RELAY=                         # Relay server (optional, empty = same host)
REMOTE_CONTROL_SERVER_API=                           # API server (optional, Pro only, http(s) URL)
REMOTE_CONTROL_SERVER_KEY=<contents of id_ed25519.pub>  # PUBLIC key only, never the private key

# Optional
REMOTE_CONTROL_DOWNLOAD_URL=                         # Custom link shown to participants (must start with http(s):// or /)
REMOTE_CONTROL_DOWNLOAD_URL_PUBLIC=false             # true = setup page open to anyone, false = only via the room request link (token)
```

When `REMOTE_CONTROL_SERVER_HOST` is set and `REMOTE_CONTROL_DOWNLOAD_URL` is empty, participants get a link to the built-in setup page (`/remote-control/setup`) with the server details and key to copy into their RustDesk client. By default the page requires the short-lived token sent with the remote control request, set `REMOTE_CONTROL_DOWNLOAD_URL_PUBLIC=true` to make it open to anyone with the URL.

If `REMOTE_CONTROL_SERVER_HOST` is empty, `REMOTE_CONTROL_DOWNLOAD_URL` defaults to `https://rustdesk.com/`. You can also point it at your own page with a preconfigured client / instructions.

Restart MiroTalk:

```bash
# Docker
docker compose restart
# or PM2
pm2 restart all
```

## 6. Test

1. Join a room as presenter, and join as a participant from another device.
2. Presenter: participants menu → **Remote control**.
3. Participant: accept, share RustDesk ID + one-time password.
4. Presenter: **Open RustDesk** (launches `rustdesk://connection/new/<id>`) and enter the password.
5. Check that the connection goes through your server (RustDesk shows "Connected" with your relay or ID server, and `docker compose logs hbbs hbbr` shows activity).

## Notes

- Use `docker compose down` / `up -d` to restart the RustDesk server. Keep the data volume, because deleting it changes the key and breaks all configured clients.
- A DNS name for the RustDesk server is recommended over a raw IP.
