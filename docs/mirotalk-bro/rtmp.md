---
title: MiroTalk BRO - RTMP upstream source
description: Use an RTMP publisher such as an ATEM, OSEE switcher, or OBS as the broadcaster of a MiroTalk BRO SFU room through MediaMTX and FFmpeg.
---

# RTMP upstream source

MiroTalk BRO can use an RTMP publisher such as a Blackmagic ATEM, OSEE switcher, or OBS as the broadcaster for an SFU room. MediaMTX receives RTMP, FFmpeg converts H.264/AAC into VP8/Opus RTP, and mediasoup distributes the result to WebRTC viewers.

## Requirements

RTMP ingest is available only when `BROADCASTING=sfu`. A room can have one source at a time: either a browser broadcaster or an RTMP publisher.

The MiroTalk image already ships FFmpeg. MediaMTX runs as a separate service, kept out of the main Compose file so P2P deployments never start it. For a non-Docker installation, install FFmpeg separately and run a MediaMTX instance that uses [mediamtx.yml](https://github.com/miroslavpejic85/mirotalkbro/blob/main/mediamtx.yml).

## Configuration

Set these values in `.env`:

```dotenv
BROADCASTING=sfu
RTMP_ENABLED=true
RTMP_PUBLISH_TOKEN=replace_with_a_long_random_value
```

When deploying behind NAT, also set `MEDIASOUP_ANNOUNCED_IP` to the public IP and expose the configured mediasoup UDP/TCP port range. Expose TCP port `1936` for RTMP publishers.

Start the Docker services with the MediaMTX overlay:

```bash
docker compose -f docker-compose.yml -f docker-compose-mediamtx.yml up -d
```

Without `-f docker-compose-mediamtx.yml`, only MiroTalk starts and RTMP ingest is unavailable.

!!! warning "Keep the publish token private"

    Plain RTMP does not encrypt the token or media in transit. Restrict the publish port to the encoder's network, or see [Encrypt the publish link (RTMPS)](#encrypt-the-publish-link-rtmps) below.

## Run without Docker

Install FFmpeg and MediaMTX. On macOS:

```bash
brew install ffmpeg mediamtx
```

Install MiroTalk dependencies:

```bash
npm install
```

Configure `.env`:

```dotenv
BROADCASTING=sfu
RTMP_ENABLED=true
RTMP_PUBLISH_TOKEN=my-secret-token
RTMP_SOURCE_URL=rtmp://127.0.0.1:1936
FFMPEG_PATH=ffmpeg
MEDIASOUP_ANNOUNCED_IP=127.0.0.1
```

From the project directory, start MediaMTX:

```bash
mediamtx mediamtx.yml
```

In another terminal, start MiroTalk:

```bash
npm start
```

For viewers on another device, replace `127.0.0.1` with the server's LAN or public IP. Allow TCP ports `1936` and `3016`, together with the configured mediasoup UDP/TCP port range, through the firewall.

## Publish

For a room named `studio`, configure the hardware encoder with:

```text
Server:     rtmp://YOUR_HOST:1936/live
Stream key: studio?token=YOUR_RTMP_PUBLISH_TOKEN
```

The complete publish URL is:

```text
rtmp://YOUR_HOST:1936/live/studio?token=YOUR_RTMP_PUBLISH_TOKEN
```

The `live/` prefix is required, and the room ID accepts only letters, digits, `-` and `_`. Any other path is rejected and the viewer keeps waiting for a broadcaster.

Viewers join the normal MiroTalk URL:

```text
https://YOUR_HOST/viewer?id=studio&name=Viewer
```

To let viewers choose their own display name first, share the join page instead:

```text
https://YOUR_HOST/home?id=studio
```

That page only offers the viewer role when a room ID is present, and it labels the room with an **RTMP** badge once the publisher is live, so the audience knows the feed comes from an external encoder rather than a browser host.

MediaMTX asks MiroTalk to authenticate the publisher. Once accepted, MiroTalk creates mediasoup plain RTP producers and starts FFmpeg. When the publisher disconnects, FFmpeg exits and MiroTalk closes the room and its media resources.

## Encrypt the publish link (RTMPS)

Plain RTMP sends the publish token and the media in the clear. On a LAN or VPN that is usually acceptable; if the publish port is reachable from the internet, enable RTMPS in `mediamtx.yml`:

```yaml
rtmpEncryption: optional # keep plain RTMP for the internal bridge, add RTMPS for encoders
rtmpAddress: :1936
rtmpsAddress: :1937 # must differ from rtmpAddress
rtmpServerKey: server.key
rtmpServerCert: server.crt
```

Encoders then publish to `rtmps://YOUR_HOST:1937/live/ROOM_ID?token=...`, and only that port needs to be exposed.

Use `optional` rather than `strict`. The FFmpeg bridge reads the stream back from MediaMTX over the internal network, and leaving plain RTMP available on `rtmpAddress` means `RTMP_SOURCE_URL` keeps working unchanged. With `strict`, plain RTMP is disabled entirely and `RTMP_SOURCE_URL` must be switched to an `rtmps://` URL as well.

The certificate must be signed by a CA the encoder trusts. Browsers let you click through a self-signed certificate, but hardware encoders simply fail the TLS handshake and report a generic connection error, so the bundled self-signed certificate in [app/ssl](https://github.com/miroslavpejic85/mirotalkbro/tree/main/app/ssl) is not usable here. Not all hardware supports RTMPS at all — Blackmagic ATEM does, but some encoders are plain RTMP only.

## Tuning

The default converted video bitrate is `1500k`. Override it with:

```dotenv
RTMP_VIDEO_BITRATE=2500k
```

The bridge limits converted video to 720p at 30 frames per second by default. Hosts with more encoding capacity can override the limits:

```dotenv
RTMP_VIDEO_WIDTH=1920
RTMP_VIDEO_HEIGHT=1080
RTMP_VIDEO_FPS=30
```

The VP8 encoder runs on `min(4, cpu cores)` threads. Override it with:

```dotenv
RTMP_VIDEO_THREADS=8
```

The conversion intentionally uses VP8 and Opus for predictable browser compatibility. Video transcoding consumes CPU, so capacity depends on resolution, frame rate, host CPU, and the number of simultaneous RTMP rooms. If MediaMTX repeatedly logs `reader is too slow` and then an I/O timeout, FFmpeg is not converting quickly enough. Raise `RTMP_VIDEO_THREADS`, lower the output width, height, or frame rate, or reduce the source settings in the publisher.

If the bridge dies while the publisher stays connected, MiroTalk respawns FFmpeg automatically and viewers keep watching; MediaMTX only authenticates a publisher once, so without this the room could not recover until the encoder reconnected.

## Related pages

| Goal | Documentation |
| --- | --- |
| Install MiroTalk BRO | [Self-hosting guide](self-hosting.md) |
| Review the environment settings | [Configuration reference](configurations.md) |
| Build viewer links | [Join options](join-room.md) |
