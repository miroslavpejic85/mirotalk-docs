# Joining Room Options

---

**URL**: [https://your.domain.com/join?room=test&name=mirotalk&audio=0&video=0&screen=0&hide=0&notify=0](https://p2p.mirotalk.com/join?room=test&name=mirotalk&audio=0&video=0&screen=0&hide=0&notify=0)

**Description**: This URL allows you to directly enter a `room` named test. You can specify your username using the `name` parameter. Additionally, you have the option to control your audio, video, screen sharing, hide myself, and welcome message preferences through the `audio`, `video`, `screen`, `hide`, and `notify` parameters.

---

## Parameters

| Params     | Type    | Description                                                                                                                                    |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `room`     | string  | This parameter represents the unique identifier or ID of the room you want to join                                                             |
| `name`     | string  | This parameter represents your username or unique identifier, allowing you to define your identity within the room                             |
| `audio`    | boolean | Use this parameter to control your audio stream. Set to `0` for no audio or `1` to enable audio                                                |
| `video`    | boolean | Control your video stream using this parameter. Set to `0` for no video or `1` to enable video                                                 |
| `screen`   | boolean | To control screen sharing, use this parameter. Set to `0` for no screen sharing or `1` to enable screen sharing                                |
| `hide`     | boolean | Determines whether to hide the user from the room view. Set to `0` to not hide or `1` to hide                                                  |
| `notify`   | boolean | You can specify whether or not to display a welcome message upon joining the room by setting this parameter to `0` (disable) or `1` (enable)   |
| `username` | string  | Represents the authentication username for the user. Only required if `HOST_PROTECTED` or `HOST_USER_AUTH` is set to `true` in the `.env` file |
| `password` | string  | Represents the authentication password for the user. Only required if `HOST_PROTECTED` or `HOST_USER_AUTH` is set to `true` in the `.env` file |

---

By utilizing these URLs and parameters, you can seamlessly customize your room entry experience, including your identity, audio and video preferences, screen sharing options, and welcome messages on the respective platforms.

---
