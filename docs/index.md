# MiroTalk Home

Welcome to MiroTalk documentations!

## Live demos

- `MiroTalk SFU`: [https://sfu.mirotalk.com](https://sfu.mirotalk.com)
- `MiroTalk P2P`: [https://p2p.mirotalk.com](https://p2p.mirotalk.com)
- `MiroTalk C2C`: [https://c2c.mirotalk.com](https://c2c.mirotalk.com)
- `MiroTalk BRO`: [https://bro.mirotalk.com](https://bro.mirotalk.com)
- `MiroTalk WEB`: [https://webrtc.mirotalk.com](https://webrtc.mirotalk.com)

---

## Join for Questions & Support

To engage in `questions`, `discussions`, or seek `assistance and support`, we invite you to join us on our [Discord server](https://discord.gg/rgGYfeYW3N).

---

## About

MiroTalk WebRTC is a real-time communication technology that enables audio and video communication over the internet through web browsers without the need for additional plugins or software installations. It stands out as a core component of many web-based video conferencing and communication platforms, offering several advantages:

Pros of MiroTalk WebRTC:

1. `Ease of Use:` MiroTalk WebRTC simplifies online communication by allowing users to connect via web browsers, eliminating the need for complex setups or downloads.

2. `Low Latency:` It provides low-latency audio and video transmission, ensuring a smooth and near-instantaneous conversation experience, crucial for real-time interactions.

3. `Security:` WebRTC offers end-to-end encryption, enhancing the security and privacy of your online conversations, making it suitable for confidential or sensitive discussions.

4. `Cross-Platform Compatibility:` MiroTalk WebRTC works on various platforms, including Windows, macOS, Linux, Android, and iOS, ensuring broad accessibility.

5. `Scalability:` It is highly scalable, making it suitable for both one-on-one conversations and large-scale conferences, adapting to your communication needs.

6. `Integration:` Many communication platforms and applications integrate MiroTalk WebRTC, enabling seamless communication within existing software or services.

7. `Flexible and Extensible:` MiroTalk WebRTC's allows developers to tap into code, facilitating innovation and enabling tailored solutions to meet specific communication requirements.

8. `Reduced Costs:` Since it doesn't require dedicated hardware or software licenses, it can be a cost-effective solution for businesses and individuals.

9. `Versatile Applications:` Besides video conferencing, MiroTalk WebRTC can be used for various applications like online gaming, customer support, and live streaming.

Overall, MiroTalk WebRTC is a versatile, user-friendly, and secure technology that has revolutionized online communication by providing high-quality, real-time audio and video capabilities directly through web browsers. Its widespread adoption has made it a fundamental tool for businesses, organizations, and individuals seeking efficient and effective online interactions.

---

## Fast integration

Easily incorporate MiroTalk into your website or app with a straightforward iframe and just a few lines of code!

[MiroTalk SFU example](https://codepen.io/Miroslav-Pejic/pen/LYXRbmE)

```html
<iframe
  allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; autoplay"
  src="https://sfu.mirotalk.com/newroom"
  style="width: 100vh; height: 100vw; border: 0px;"
></iframe>
```

[MiroTalk P2P example](https://codepen.io/Miroslav-Pejic/pen/jOQMVzx)

```html
<iframe
  allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; autoplay"
  src="https://p2p.mirotalk.com/newcall"
  style="width: 100vh; height: 100vw; border: 0px;"
></iframe>
```

[MiroTalk C2C example](https://codepen.io/Miroslav-Pejic/pen/ExOgNbJ)

```html
<iframe
  allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; autoplay"
  src="https://c2c.mirotalk.com"
  style="width: 100vh; height: 100vw; border: 0px;"
></iframe>
```

[MiroTalk BRO example](https://codepen.io/Miroslav-Pejic/pen/OJaRbZg)

```html
<iframe
  allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; autoplay"
  src="https://bro.mirotalk.com"
  style="width: 100vh; height: 100vw; border: 0px;"
></iframe>
```

[MiroTalk WEB example](https://codepen.io/Miroslav-Pejic/pen/jOQMVxx)

```html
<iframe
  allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; autoplay"
  src="https://webrtc.mirotalk.com"
  style="width: 100vh; height: 100vw; border: 0px;"
></iframe>
```

An example of how to integrate MiroTalk with a [React application](https://codepen.io/Miroslav-Pejic/pen/QWzmGaZ)

After setting up your MiroTalk instances, please update the `src` attribute with your custom domain or subdomain name.

---

## Custom integration

Integrating MiroTalk into existing platforms like `Perfex, PlayTube, Sngine, Wowonder` and other web applications can be relatively straightforward. Let's break down the process in a more detailed and structured manner:

`Initial Setup`: In your existing application, determine where you want to include the video conferencing feature. This could be within a specific module or page. For the sake of illustration, let's assume you want to provide a video conferencing option.

`HTML Button`: In the HTML of your target page, create a button element that users can click to initiate a video conference session. This button acts as a trigger to start the video conference.

```html
<button id="startConferenceButton">Start Video Conference></button>
```

Here the `PHP` version

```html
<!-- Your HTML form -->
<form method="post">
  <button type="submit" name="startConferenceButton" id="startConferenceButton">
    Start Conference>
  </button>
</form>
```

`JavaScript or PHP Function`:

Incorporate JavaScript to handle the button click event and open a new window or tab where the video conference will take place:

```javascript
document
  .getElementById("startConferenceButton")
  .addEventListener("click", function () {
    window.open("videoConference.html", "_blank");
  });
```

Or You can use PHP to manage the button click event, enabling the opening of a new window or tab for the video conference to take place:

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
 // Check if the button was clicked (you can adjust the condition as needed)
 if (isset($_POST['startConferenceButton'])) {
  echo '<script> window.open("videoConference.html", "_blank"); </script>';
 }
}
```

Video Conference HTML Page: Create a new HTML page, let's call it `videoConference.html`. This page will host the video conferencing functionality.

```html
<!-- videoConference.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  </head>

  <body>
    <!-- HTML container for the video conference -->
    <iframe
      allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; autoplay"
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
		- https://webrtc.mirotalk.com
	-->
</html>
```

After setting up your MiroTalk instances, please update the `src` attribute with your custom domain or subdomain name.
