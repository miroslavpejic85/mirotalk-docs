# MiroTalk BRO Integration

## Iframe

Easily integrate MiroTalk BRO into your website by embedding it with a simple `iframe` as Landing Page Mode.

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>MiroTalk BRO - Video Call</title>
    </head>
    <body>
        <iframe
            id="mirotalkBRO"
            allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
            src="https://YOUR-DOMAIN-NAME"
            style="height: 100vh; width: 100vw; border: 0px;"
        ></iframe>
    </body>
</html>
```

> **Important:** Replace `YOUR-DOMAIN-NAME` with your actual MiroTalk C2C server URL.

---

## 🔧 Integration Options

Skip the landing page entirely - users join immediately with pre-set credentials as either broadcaster or viewer.

**Broadcaster (Stream Host):**
```html
<iframe
    allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
    src="https://YOUR-DOMAIN-NAME/broadcast?id=demo&name=Broadcaster"
    style="height: 100vh; width: 100vw; border: 0px;"
></iframe>
```

**Viewer (Audience):**
```html
<iframe
    allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay"
    src="https://YOUR-DOMAIN-NAME/viewer?id=demo&name=Viewer"
    style="height: 100vh; width: 100vw; border: 0px;"
></iframe>
```

**Use Case:** Live streaming, webinars, presentations, or automated workflows where user roles are predefined.

**URL Examples:**

- Broadcast: [https://YOUR-DOMAIN-NAME/broadcast?id=demo&name=Broadcaster](https://bro.mirotalk.com/broadcast?id=demo&name=Broadcaster)
- Viewer: [https://YOUR-DOMAIN-NAME/viewer?id=demo&name=Viewer](https://bro.mirotalk.com/viewer?id=demo&name=Viewer)