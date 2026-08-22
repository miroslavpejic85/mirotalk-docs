# MiroTalk WEB Integration

## Iframe

Easily integrate MiroTalk WEB into your website by embedding it with a simple `iframe` as Landing Page Mode.

```html
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>MiroTalk WEB - Video Call</title>
    </head>
    <body>
        <iframe
            id="mirotalkWEB"
            allow="camera; microphone; speaker-selection; display-capture; fullscreen; clipboard-read; clipboard-write; web-share; autoplay; picture-in-picture"
            src="https://YOUR-DOMAIN-NAME"
            style="height: 100vh; width: 100vw; border: 0px;"
        ></iframe>
    </body>
</html>
```

> **Important:** Replace `YOUR-DOMAIN-NAME` with your actual MiroTalk WEB server URL.

## Calendar

Scheduled meetings can be added to external calendars directly from the invitation:

- **Google Calendar**
- **Outlook Calendar**

## Email Reminders

Automatic email reminders are sent to the participants before the scheduled meeting starts.