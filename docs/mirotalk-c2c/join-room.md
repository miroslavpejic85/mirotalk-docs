# Joining Room Options

---

## Homepage

**URL**: [https://YOUR-DOMAIN-NAME](https://c2c.mirotalk.com)

Users can access the homepage to define the desired room and set their username. This provides full control over room selection and personal identification.

---

## Pre-set Room

**URL**: [https://YOUR-DOMAIN-NAME/?room=ROOM-NAME](https://c2c.mirotalk.com/?room=ROOM-NAME)

Allows users to specify a room via URL parameter while choosing their username on the page. Replace the `room` parameter to access different rooms.

---

## Direct Join

**URL**: [https://YOUR-DOMAIN-NAME/join?room=ROOM-NAME&name=USER-NAME&audio=0&video=1](https://c2c.mirotalk.com/join?room=test&name=mirotalkc2c&audio=0&video=1)

Provides immediate access to a specific room with room name, username, and media preferences preconfigured in the URL.

---

## Parameters

| Params  | Type    | Description                                        |
| ------- | ------- | -------------------------------------------------- |
| `room`  | string  | Unique room identifier.                            |
| `name`  | string  | Display name.                                      |
| `audio` | boolean | Enable (`1`) or disable (`0`) audio on join.       |
| `video` | boolean | Enable (`1`) or disable (`0`) video on join.       |

---

## Customization

Replace `ROOM-NAME` and `USER-NAME` in the URLs with your preferred values, and set `audio` / `video` to `1` (enabled) or `0` (disabled) to personalize the room entry experience.

---
