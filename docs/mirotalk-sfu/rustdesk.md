# Self-hosted RustDesk + MiroTalk SFU Remote Control

MiroTalk only brokers the consent handshake (ID + one-time password). The actual remote session runs through the RustDesk clients and your own RustDesk server. No MiroTalk code changes are needed.

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
Optional: build or distribute a preconfigured client so participants don't need to enter anything (the Pro option, or a self-compiled OSS client).

## 5. Configure MiroTalk SFU

In `.env`:

```env
REMOTE_CONTROL_ENABLED=true
REMOTE_CONTROL_DOWNLOAD_URL=https://your-domain/rustdesk-download  # page with your preconfigured client / instructions (http/https only)
```

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
