# Joining Room Options

---

## Homepage

**URL**: [https://YOUR-DOMAIN-NAME](https://cme.mirotalk.com)

Users can access the homepage to sign in with a username. Once signed in, they can see connected users and initiate a video call with a single click.
 
---

## User 1 Join

**URL**: [https://YOUR-DOMAIN-NAME/join?user=USER-1](https://cme.mirotalk.com/join?user=USER-1)

Allows a user to join directly with a username specified via URL parameter. Replace `USER-1` with the desired username to skip the sign-in step.

---

## User 2 auto-calls User 1

**URL**: [https://YOUR-DOMAIN-NAME/join?user=USER-2&call=USER-1](https://cme.mirotalk.com/join?user=user2&call=user1)

Allows `USER-2` to join and automatically initiate a video call to `USER-1`. Both the caller username and the recipient are preconfigured in the URL.

---

## User 1 Join a specific Room

**URL**: [https://YOUR-DOMAIN-NAME/join?user=USER-1&room=Support](https://cme.mirotalk.com/join?user=user1&room=Support)

By default everyone joins the shared `Public` room. Add a `room` parameter to group users into separate rooms (e.g. `Support`, `Reception`). Users only see and can call others in the same room.

---

## User 2 auto-calls User 1 in a Room

**URL**: [https://YOUR-DOMAIN-NAME/join?user=USER-2&call=USER-1&room=Support](https://cme.mirotalk.com/join?user=user2&call=user1&room=Support)

Allows `USER-2` to join the `Support` room and automatically initiate a video call to `USER-1` in the same room.

> **Note:** The `call` target must be in the same `room` as the caller. If `room` is omitted, users join the default `Public` room.

---

## Customization

Replace `USER-1` and `USER-2` in the URLs with your preferred usernames, and `Support` with your desired room name, to personalize the call experience.

---
