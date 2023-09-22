# Joining Room Options

![globe](../images/globe.png)

---

**URL**: [https://your.domain.com/join?room=test&password=0&name=mirotalksfu&audio=0&video=0&screen=0&notify=0](https://sfu.mirotalk.com/join?room=test&password=0&name=mirotalksfu&audio=0&video=0&screen=0&notify=0)

**Description**: This URL allows you to directly enter a `room` named test. You can specify your username using the `name` parameter. Additionally, you have the option to set room password, control your audio, video, screen sharing, and welcome message preferences through the `password`,`audio`, `video`, `screen`, and `notify` parameters.

---

## Parameters

| Params     | Type           | Description                                                                                                                                  |
| ---------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `room`     | string         | This parameter represents the unique identifier or ID of the room you want to join                                                           |
| `password` | string/boolean | You can set a room password using this parameter. If no password is required, you can use `0` as a placeholder                               |
| `name`     | string         | This parameter represents your username or unique identifier, allowing you to define your identity within the room                           |
| `audio`    | boolean        | Use this parameter to control your audio stream. Set to `0` for no audio or `1` to enable audio                                              |
| `video`    | boolean        | Control your video stream using this parameter. Set to `0` for no video or `1` to enable video                                               |
| `screen`   | boolean        | To control screen sharing, use this parameter. Set to `0` for no screen sharing or `1` to enable screen sharing                              |
| `notify`   | boolean        | You can specify whether or not to display a welcome message upon joining the room by setting this parameter to `0` (disable) or `1` (enable) |

---

By utilizing this URL and its associated parameters, you can seamlessly customize your room entry experience, including your identity, room password, audio and video preferences, screen sharing options, and welcome messages.

---
