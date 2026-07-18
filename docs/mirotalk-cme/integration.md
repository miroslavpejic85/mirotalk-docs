# MiroTalk CME Integration

## Iframe

Easily integrate MiroTalk CME into your website by embedding it with a simple `iframe` as Landing Page Mode.

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>MiroTalk CME - Video Call</title>
    </head>
    <body>
        <iframe
            id="mirotalkCME"
            allow="camera; microphone; speaker-selection; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay; picture-in-picture"
            src="https://YOUR-DOMAIN-NAME"
            style="height: 100vh; width: 100vw; border: 0px;"
        ></iframe>
    </body>
</html>
```

> **Important:** Replace `YOUR-DOMAIN-NAME` with your actual MiroTalk CME server URL.

**Use Case:** Customer support, telehealth, online tutoring, consultations, or any scenario requiring instant one-to-one video calls.

---

## Click-to-Call Widget

Add a **click-to-call widget** to your website so visitors can start or join a call in one click. The call opens inside an embedded `iframe`.

![widget](https://raw.githubusercontent.com/miroslavpejic85/call-me/main/integration/widget.png)

Ready-to-use examples are available in the repository:

- [widget.html](https://github.com/miroslavpejic85/call-me/blob/main/integration/widget.html) — the caller types the username to call.
- [widgetHttps.html](https://github.com/miroslavpejic85/call-me/blob/main/integration/widgetHttps.html) — auto-fetches connected users from the [REST API](api.md) (requires HTTPS) and shows them in a dropdown.

> **Important:** Replace the `domain` value with your actual MiroTalk CME server URL, and keep your `call_me_api_key_secret` in sync with your server. Never expose a production API key in publicly accessible client code, use a backend proxy when appropriate.

**Use Case:** Support desks, call centers, or any landing page where visitors should start or join a call with an available agent.