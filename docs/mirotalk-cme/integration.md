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