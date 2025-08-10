# Joining Room Options

---

**URL**: [https://your.domain.com/join?room=test&roomPassword=0&name=mirotalksfu&avatar=0&audio=0&video=0&screen=0&chat=0&hide=0&notify=0&duration=unlimited](https://sfu.mirotalk.com/join?room=test&roomPassword=0&name=mirotalksfu&avatar=0&audio=0&video=0&screen=0&chat=0&hide=0&notify=0&duration=unlimited)

**Description**: This URL allows you to directly enter a `room` named test. You can specify your username using the `name` parameter and avatar image URL using the `avatar` parameter. Additionally, you have the option to set room password, control your audio, video, screen sharing, welcome message and room duration preferences through the `roomPassword`, `audio`, `video`, `screen`, `hide`, `notify` and `duration` parameters.

---

## Parameters

| Params         | Type           | Description                                                                                                                                        |
| -------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `room`         | string         | This parameter represents the unique identifier or ID of the room you want to join                                                                 |
| `roomPassword` | string/boolean | You can set a room password using this parameter. If no password is required, you can use `0` as a placeholder                                     |
| `name`         | string         | This parameter represents your username or unique identifier, allowing you to define your identity within the room                                 |
| `avatar` 			 | Mixed          | This parameter specifies the avatar image that will be displayed when your camera is turned off in the room																	       |
| `audio`        | boolean        | Use this parameter to control your audio stream. Set to `0` for no audio or `1` to enable audio                                                    |
| `video`        | boolean        | Control your video stream using this parameter. Set to `0` for no video or `1` to enable video                                                     |
| `screen`       | boolean        | To control screen sharing, use this parameter. Set to `0` for no screen sharing or `1` to enable screen sharing                                    |
| `chat`         | boolean        | To control chat, use this parameter. Set to `0` for no screen sharing or `1` to enable chat                                                        |
| `hide`         | boolean        | Determines whether to hide the user from the room view. Set to `0` to not hide or `1` to hide                                                      |
| `notify`       | boolean        | You can specify whether or not to display a welcome message upon joining the room by setting this parameter to `0` (disable) or `1` (enable)       |
| `duration`     | string         | Defines the maximum allowed duration for the room in `HH:MM:SS` format. Once the specified duration is reached, the room will automatically close  |
| `token`        | string         | Represents the token for the user. Optional if `host.protected` or `host.user_auth` is set to `true` in the `config.js` file                       |

---

By utilizing this URL and its associated parameters, you can seamlessly customize your room entry experience, including your identity, room password, audio and video preferences, screen sharing options, hide myself, and welcome messages.

---
