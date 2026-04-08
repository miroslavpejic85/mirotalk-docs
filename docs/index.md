# MiroTalk Home

![mirotalk](./images/mirotalk.gif)

## MiroTalk Projects

| Project | Live Demo | Description |
| :--- | :--- | :--- |
| 🏆 **SFU** | [sfu.mirotalk.com](https://sfu.mirotalk.com) | Scalable group video conferencing |
| 🚀 **P2P** | [p2p.mirotalk.com](https://p2p.mirotalk.com) | Peer-to-peer video calls |
| ✨ **C2C** | [c2c.mirotalk.com](https://c2c.mirotalk.com) | Cam-to-Cam communication |
| 📡 **BRO** | [bro.mirotalk.com](https://bro.mirotalk.com) | Broadcasting one-to-many streaming |
| 🟢 **CME** | [cme.mirotalk.com](https://cme.mirotalk.com) | Instant click-to-call video calls |
| 🛠 **WEB** | [webrtc.mirotalk.com](https://webrtc.mirotalk.com) | Room scheduler and meeting manager |
| ⚙️ **ADMIN** | [Self-hosting guide](https://docs.mirotalk.com/mirotalk-admin/self-hosting) | Manage updates, configurations, and settings |

---

View the complete [MiroTalk projects overview and comparisons](overview/index.html).

---

## License

Support the ongoing development and adapt MiroTalk to your unique needs.

🌐 [Check our licensing options](./license/licensing-options.md)

---

## Questions & Support

Check the [Frequently Asked Questions](./faq/index.md) for common topics, or join our [MiroTalk Community Forum](https://discord.gg/rgGYfeYW3N) for discussions and support.

---

## About

MiroTalk WebRTC enables real-time audio and video communication directly through web browsers — no plugins or software installations required.

| Advantage | Description |
| :--- | :--- |
| 🌐 **Ease of Use** | Connect via any web browser — no complex setups or downloads needed |
| ⚡ **Low Latency** | Smooth, near-instantaneous audio and video for real-time interactions |
| 🔒 **Security** | End-to-end encryption for private and confidential conversations |
| 💻 **Cross-Platform** | Works on Windows, macOS, Linux, Android, and iOS |
| 📈 **Scalability** | Supports one-on-one calls through large-scale conferences |
| 🔗 **Integration** | Embeds seamlessly into existing platforms and applications |
| 🛠️ **Flexible** | Open codebase lets developers build tailored solutions |
| 💰 **Reduced Costs** | No dedicated hardware or software licenses required |
| 🎮 **Versatile** | Use for video conferencing, live streaming, customer support, and more |

---

## Fast Integration

![iframe](./images/iframe.png)

Embed MiroTalk into your website or app with a simple iframe:

```html
<iframe
  allow="camera; microphone; speaker-selection; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay; picture-in-picture"
  src="https://sfu.mirotalk.com/newroom"
  style="width: 100vw; height: 100vh; border: 0px;"
></iframe>
```

Just change the `src` to match the MiroTalk variant you need:

| Project | Source URL | CodePen |
| :--- | :--- | :--- |
| **SFU** | `https://sfu.mirotalk.com/newroom` | [Demo](https://codepen.io/Miroslav-Pejic/pen/LYXRbmE) |
| **P2P** | `https://p2p.mirotalk.com/newcall` | [Demo](https://codepen.io/Miroslav-Pejic/pen/jOQMVzx) |
| **C2C** | `https://c2c.mirotalk.com` | [Demo](https://codepen.io/Miroslav-Pejic/pen/ExOgNbJ) |
| **BRO** | `https://bro.mirotalk.com` | [Demo](https://codepen.io/Miroslav-Pejic/pen/OJaRbZg) |
| **CME** | `https://cme.mirotalk.com` | [Demo](https://codepen.io/Miroslav-Pejic/pen/empeGYJ) |
| **WEB** | `https://webrtc.mirotalk.com` | [Demo](https://codepen.io/Miroslav-Pejic/pen/jOQMVxx) |

See also: [React integration example](https://codepen.io/Miroslav-Pejic/pen/QWzmGaZ)

After setting up your MiroTalk instances, update the `src` attribute with your custom domain or subdomain.

---

## Quick Custom Integration

Integrate MiroTalk into existing platforms like Perfex, PlayTube, Sngine, Wowonder, or any web application.

### Step 1: HTML Button

Add a button to trigger a video conference session:

```html
<!-- Button for Javascript -->

<button id="startConferenceButton">Start Video Conference</button>

<!-- Button for PHP-->

<form method="post">
  <button type="submit" name="startConferenceButton" id="startConferenceButton">
    Start Conference
  </button>
</form>
```

### Step 2: Handle the Click Event

**JavaScript:**

```javascript
document
  .getElementById("startConferenceButton")
  .addEventListener("click", function () {
    window.open("videoConference.html", "_blank");
    // toggleMiroTalk();
  });
```

**PHP:**

```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 if (isset($_POST['startConferenceButton'])) {
  echo '<script> window.open("videoConference.html", "_blank"); </script>';
  // echo '<script> toggleMiroTalk(); </script>';
 }
}
```

### Step 3: Video Conference Page

Create a dedicated `videoConference.html` page:

```html
<!-- videoConference.html -->
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>

  <body>
    <!-- HTML container for the video conference -->
    <iframe
      id="mirotalkIframe"
      allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
      src="https://sfu.mirotalk.com/newroom"
      style="height: 100vh; width: 100vw; border: 0px;"
    ></iframe>
  </body>

  <!--
    The iframe 'src' attribute can be any of:
      - https://sfu.mirotalk.com
      - https://p2p.mirotalk.com
      - https://c2c.mirotalk.com
      - https://bro.mirotalk.com
      - https://cme.mirotalk.com
      - https://webrtc.mirotalk.com
      - ...
	-->
</html>
```

Alternatively, embed the iframe in your existing page and toggle its visibility:

```javascript
function toggleMiroTalk() {
  const mirotalkIframe = document.getElementById("mirotalkIframe");
  mirotalkIframe.style.display =
    mirotalkIframe.style.display === "none" ||
    mirotalkIframe.style.display === ""
      ? "block"
      : "none";
}
```

After setting up your MiroTalk instances, update the `src` attribute with your custom domain or subdomain.

### Step 4: Customize the iframe `src`

Use query parameters to customize the URL — see the join-room guide for each variant:

- [MiroTalk SFU direct join](./mirotalk-sfu/join-room.md)
- [MiroTalk P2P direct join](./mirotalk-p2p/join-room.md)
- [MiroTalk C2C direct join](./mirotalk-c2c/join-room.md)
- [MiroTalk BRO direct join](./mirotalk-bro/join-room.md)
- [MiroTalk CME direct join](./mirotalk-cme/join-room.md)

---

You can also generate meeting URLs via the REST API:

- [MiroTalk SFU REST API](./mirotalk-sfu/api.md)
- [MiroTalk P2P REST API](./mirotalk-p2p/api.md)
- [MiroTalk C2C REST API](./mirotalk-c2c/api.md)
- [MiroTalk BRO REST API](./mirotalk-bro/api.md)
- [MiroTalk CME REST API](./mirotalk-cme/api.md)
- [MiroTalk WEB REST API](./mirotalk-web/api.md)

---

## Self-Hosting

Deploy MiroTalk on your own server for full control over your data and infrastructure.

| Project | Self-Hosting Guide | Configurations |
| :--- | :--- | :--- |
| 🏆 **SFU** | [Self-hosting](./mirotalk-sfu/self-hosting.md) | [Config](./mirotalk-sfu/configurations.md) |
| 🚀 **P2P** | [Self-hosting](./mirotalk-p2p/self-hosting.md) | [Config](./mirotalk-p2p/configurations.md) |
| ✨ **C2C** | [Self-hosting](./mirotalk-c2c/self-hosting.md) | [Config](./mirotalk-c2c/configurations.md) |
| 📡 **BRO** | [Self-hosting](./mirotalk-bro/self-hosting.md) | [Config](./mirotalk-bro/configurations.md) |
| 🟢 **CME** | [Self-hosting](./mirotalk-cme/self-hosting.md) | [Config](./mirotalk-cme/configurations.md) |
| 🛠 **WEB** | [Self-hosting](./mirotalk-web/self-hosting.md) | [Config](./mirotalk-web/configurations.md) |
| ⚙️ **ADMIN** | [Self-hosting](./mirotalk-admin/self-hosting.md) | — |

---

## Deployment Options

Multiple deployment methods are available to suit different environments:

| Method | Description | Guide |
| :--- | :--- | :--- |
| 📜 **Install Scripts** | Automated setup on Ubuntu with a single command | [Scripts guide](./scripts/about.md) |
| 🐳 **Docker Compose** | Containerized deployment for easy management | [Docker guide](./utility/docker-compose.md) |
| ☁️ **Cloudron** | One-click deployment with automatic updates and backups | [Cloudron guide](./cloudron/cloudron.md) |

---

## WebRTC Architectures

Understanding WebRTC architectures helps you choose the right MiroTalk product for your use case:

| Architecture | How It Works | Best For |
| :--- | :--- | :--- |
| **Mesh (P2P)** | Peers connect directly to each other | Small groups, low latency |
| **SFU** | Central server selectively forwards streams | Larger meetings, scalable |
| **MCU** | Server mixes all streams into one | Centralized control, media mixing |

📖 [Learn more about WebRTC architectures](./webrtc/architectures.md)

---

## Advanced Features

MiroTalk offers powerful capabilities beyond basic video conferencing:

| Feature | Description | Guide |
| :--- | :--- | :--- |
| 📺 **RTMP Streaming** | Live stream to platforms via Node Media Server or Nginx RTMP | [RTMP guide](./mirotalk-sfu/rtmp.md) |
| 📈 **Scalability** | Scale to 100–1000+ concurrent users with vertical or horizontal scaling | [Scalability guide](./mirotalk-sfu/scalability.md) |
| 🔗 **Webhooks** | Event-driven integrations for room and user events | [SFU webhooks](./mirotalk-sfu/webhook.md) · [P2P webhooks](./mirotalk-p2p/webhook.md) |
| 🛡️ **Host Protection** | Restrict room access and manage participants | [SFU](./mirotalk-sfu/host-protection.md) · [P2P](./mirotalk-p2p/host-protection.md) |
| 🎨 **Rebranding** | Customize the look and feel with your own brand | [SFU](./mirotalk-sfu/rebranding.md) · [P2P](./mirotalk-p2p/rebranding.md) |

---

## Infrastructure & Utilities

Guides for setting up the supporting infrastructure:

| Topic | Description | Guide |
| :--- | :--- | :--- |
| 🌐 **STUN/TURN** | NAT traversal with Coturn for reliable peer connections | [STUN/TURN overview](./coturn/stun-turn.md) · [Installation](./coturn/installation.md) |
| 🔧 **Ngrok** | Expose local servers via secure public URLs for development and testing | [Ngrok guide](./ngrok/ngrok.md) |
| 📦 **NVM** | Manage multiple Node.js versions on your server | [NVM guide](./utility/nvm.md) |
| 📁 **FTP** | Set up an FTP server for file transfers | [FTP guide](./utility/ftp.md) |
| 🔄 **System Updates** | Keep your server up to date | [Update guide](./utility/update.md) |

---
