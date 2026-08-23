---
title: Quick Custom Integration
description: Add any MiroTalk project to an existing website with a button and an iframe.
---

# Quick Custom Integration

Use this project-neutral pattern to add MiroTalk to an existing website or application. It works with plain HTML, server-rendered templates, content platforms, and frameworks such as Perfex, PlayTube, Sngine, and WoWonder.

Choose a MiroTalk project first, then replace the example `src` with its hosted URL or your self-hosted domain.

## Choose a Source URL

| Project | Starting URL | Typical use |
| :--- | :--- | :--- |
| **SFU** | `https://sfu.mirotalk.com/newroom` | Scalable meetings and webinars |
| **P2P** | `https://p2p.mirotalk.com/newcall` | Private and small-group calls |
| **C2C** | `https://c2c.mirotalk.com` | One-to-one calls |
| **BRO** | `https://bro.mirotalk.com` | One-to-many broadcasts |
| **CME** | `https://cme.mirotalk.com` | Customer click-to-call |
| **WEB** | `https://webrtc.mirotalk.com` | Scheduling and room management |

!!! tip "Self-hosted instances"
    Replace the hosted URL with your own domain after deploying and configuring the selected project.

## Option 1: Open a Meeting Page

This approach keeps the meeting separate from the page that launches it.

### 1. Add a Button

```html
<button id="startConferenceButton" type="button">
  Start video conference
</button>
```

### 2. Open the Meeting Page

```javascript
document
  .getElementById("startConferenceButton")
  .addEventListener("click", function () {
    window.open("videoConference.html", "_blank", "noopener,noreferrer");
  });
```

For a server-rendered page, the same behavior can be expressed without JavaScript:

```html
<form action="videoConference.html" method="get" target="_blank">
  <button type="submit">Start video conference</button>
</form>
```

### 3. Create `videoConference.html`

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Video conference</title>
    <style>
      html,
      body,
      iframe {
        width: 100%;
        height: 100%;
        margin: 0;
        border: 0;
      }
    </style>
  </head>
  <body>
    <iframe
      allow="camera; microphone; speaker-selection; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay; picture-in-picture"
      src="https://sfu.mirotalk.com/newroom"
      title="MiroTalk video conference"
    ></iframe>
  </body>
</html>
```

## Option 2: Toggle an Inline Meeting

Place the iframe directly in an existing page when users should remain inside your application.

```html
<button id="toggleConferenceButton" type="button" aria-controls="mirotalkIframe" aria-expanded="false">
  Start video conference
</button>

<iframe
  id="mirotalkIframe"
  allow="camera; microphone; speaker-selection; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay; picture-in-picture"
  src="https://sfu.mirotalk.com/newroom"
  title="MiroTalk video conference"
  style="display: none; width: 100%; height: 80vh; border: 0;"
></iframe>
```

```javascript
const toggleButton = document.getElementById("toggleConferenceButton");
const mirotalkIframe = document.getElementById("mirotalkIframe");

toggleButton.addEventListener("click", function () {
  const shouldShow = mirotalkIframe.style.display === "none";

  mirotalkIframe.style.display = shouldShow ? "block" : "none";
  toggleButton.setAttribute("aria-expanded", String(shouldShow));
});
```

## Customize the Meeting URL

Use query parameters to prefill room and participant settings. The available parameters depend on the selected project:

- [MiroTalk SFU direct join](../mirotalk-sfu/join-room.md)
- [MiroTalk P2P direct join](../mirotalk-p2p/join-room.md)
- [MiroTalk C2C direct join](../mirotalk-c2c/join-room.md)
- [MiroTalk BRO direct join](../mirotalk-bro/join-room.md)
- [MiroTalk CME direct join](../mirotalk-cme/join-room.md)

For production applications, generate meeting URLs on the server when authentication, room ownership, or private credentials are required:

- [MiroTalk SFU REST API](../mirotalk-sfu/api.md)
- [MiroTalk P2P REST API](../mirotalk-p2p/api.md)
- [MiroTalk C2C REST API](../mirotalk-c2c/api.md)
- [MiroTalk BRO REST API](../mirotalk-bro/api.md)
- [MiroTalk CME REST API](../mirotalk-cme/api.md)
- [MiroTalk WEB REST API](../mirotalk-web/api.md)

!!! warning "Keep credentials on the server"
    Never expose API secrets in browser JavaScript, iframe URLs, or public source code.

## Project-Specific Integration

Use the selected project's complete integration guide for production behavior and supported options:

- [MiroTalk SFU integration](../mirotalk-sfu/integration.md)
- [MiroTalk P2P integration](../mirotalk-p2p/integration.md)
- [MiroTalk C2C integration](../mirotalk-c2c/integration.md)
- [MiroTalk BRO integration](../mirotalk-bro/integration.md)
- [MiroTalk CME integration](../mirotalk-cme/integration.md)
- [MiroTalk WEB integration](../mirotalk-web/integration.md)
