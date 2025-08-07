# MiroTalk C2C Integration

## Iframe

Easily integrate MiroTalk C2C into your website by embedding it with a simple `iframe` as Landing Page Mode.

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>MiroTalk C2C - Video Call</title>
    </head>
    <body>
        <iframe
            id="mirotalkC2C"
            allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
            src="https://YOUR-DOMAIN-NAME"
            style="height: 100vh; width: 100vw; border: 0px;"
        ></iframe>
    </body>
</html>
```

> **Important:** Replace `YOUR-DOMAIN-NAME` with your actual MiroTalk C2C server URL.

---

## Integration Options

Choose the integration method that best fits your use case:

`Landing Page Mode`
Users see the homepage and can create or join rooms manually.

```html
<iframe
    allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
    src="https://YOUR-DOMAIN-NAME"
    style="height: 100vh; width: 100vw; border: 0px;"
></iframe>
```

**Use Case:** General-purpose integration where users choose their room names.

---

`Pre-set Room`
Direct users to a specific room, but they still need to enter their name.

```html
<iframe
    allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
    src="https://YOUR-DOMAIN-NAME/?room=consultation-room"
    style="height: 100vh; width: 100vw; border: 0px;"
></iframe>
```

**Use Case:** Scheduled meetings, support rooms, or dedicated consultation spaces.

---

`Direct Join`
Skip the landing page entirely - users join immediately with pre-set credentials.

```html
<iframe
    allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
    src="https://YOUR-DOMAIN-NAME/join?room=meeting-123&name=John"
    style="height: 100vh; width: 100vw; border: 0px;"
></iframe>
```

**Use Case:** Automated workflows, customer portals, or when user details are already known.