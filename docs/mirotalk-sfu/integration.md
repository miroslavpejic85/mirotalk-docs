# MiroTalk SFU Iframe Integration

## Overview

This integration allows you to embed MiroTalk SFU into your website using an iframe. By leveraging the `IframeApi`, you can easily create and manage video conferencing rooms directly within your web application.

## Features

- Seamless iframe embedding
- Customizable room parameters
- Full control over audio, video, and screen sharing
- Password-protected rooms
- Configurable UI visibility options
- Room share notifications
- Unlimited session duration

## Usage

To integrate MiroTalk SFU via an iframe, add the provided HTML and JavaScript snippet to your webpage. Replace `YOUR-DOMAIN-NAME` with the URL of your `MiroTalk SFU instance`.

### Example Implementation

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MiroTalk SFU Iframe Demo</title>

    <script src="https://YOUR-DOMAIN-NAME/js/iframe.js" defer></script>

    <script>
      document.addEventListener("DOMContentLoaded", function () {
        const domain = "YOUR-DOMAIN-NAME";
        const options = {
          room: "test",
          roomPassword: 0,
          name: "mirotalk",
          audio: 0,
          video: 0,
          screen: 0,
          hide: 0,
          notify: 0,
          duration: "unlimited", // HH:MM:SS
          width: "100vw",
          height: "100vh",
          parentNode: document.querySelector("#meet"),
        };
        const api = new IframeApi(domain, options);
      });
    </script>
  </head>
  <body>
    <div id="meet"></div>
  </body>
</html>
```

## Configuration Options

| Parameter      | Type          | Description                                                                                                   |
| -------------- | ------------- | ------------------------------------------------------------------------------------------------------------- |
| `room`         | String        | The room ID to join                                                                                           |
| `roomPassword` | String/Number | Password for the room (0 for no password)                                                                     |
| `name`         | String        | Display name of the participant                                                                               |
| `audio`        | Number        | Enable (1) or disable (0) audio                                                                               |
| `video`        | Number        | Enable (1) or disable (0) video                                                                               |
| `screen`       | Number        | Enable (1) or disable (0) screen sharing                                                                      |
| `hide`         | Number        | Hide Self view (1 to enable, 0 to disable)                                                                    |
| `notify`       | Number        | Enable (1) or disable (0) notifications                                                                       |
| `duration`     | String        | Set a session duration (e.g., "01:30:00" for 1.5 hours)                                                       |
| `token`        | string        | Token for the user. Optional if `host.protected` or `host.user_auth` is set to `true` in the `config.js` file |
| `width`        | String        | Set the width of the iframe (e.g., "100vw")                                                                   |
| `height`       | String        | Set the height of the iframe (e.g., "100vh")                                                                  |
| `parentNode`   | DOM Element   | The parent HTML element where the iframe will be inserted                                                     |

## Installation

1. Replace `YOUR-DOMAIN-NAME` with your actual MiroTalk SFU domain.
2. Include the `iframe.js` script in your HTML file.
3. Configure the `options` object according to your needs.
4. Add an empty `<div id="meet"></div>` where the iframe should be embedded.

## Notes

- Ensure your domain allows embedding via iframe by configuring the proper CORS and X-Frame-Options settings.
- The script must be included with the `defer` attribute to ensure proper execution.
- This integration works with MiroTalk SFU and requires a valid domain setup.
