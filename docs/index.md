# MiroTalk Home

Welcome to MiroTalk documentations!

## Live demos

- `MiroTalk SFU`: [https://sfu.mirotalk.com](https://sfu.mirotalk.com)
- `MiroTalk P2P`: [https://p2p.mirotalk.com](https://p2p.mirotalk.com)
- `MiroTalk C2C`: [https://c2c.mirotalk.com](https://c2c.mirotalk.com)
- `MiroTalk BRO`: [https://bro.mirotalk.com](https://bro.mirotalk.com)
- `MiroTalk WEB`: [https://webrtc.mirotalk.com](https://webrtc.mirotalk.com)

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

An example of how to integrate MiroTalk with a [React application](https://playcode.io/1600830)

After setting up your MiroTalk instances, please update the `src` attribute with your custom domain or subdomain name.

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
		<button type="submit" name="startConferenceButton" id="startConferenceButton">Start Conference></button>
</form>
```

`JavaScript or PHP Function`:

Incorporate JavaScript to handle the button click event and open a new window or tab where the video conference will take place:

```javascript
document.getElementById('startConferenceButton').addEventListener('click', function () {
	window.open('videoConference.html', '_blank');
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
		<iframe allow="camera; microphone; display-capture; fullscreen; clipboard-read; clipboard-write; autoplay"
			src="https://sfu.mirotalk.com/newroom" style="height: 100vh; width: 100vw; border: 0px;"></iframe>
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