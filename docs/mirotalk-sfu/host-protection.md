# Host protection

![mirotalksfu-hp](../images/mirotalksfu-hp.png)

In the configuration file `app/src/config.js`, you can enable security measures for your video conferencing room using the following parameters:

- `host.protected`: Set to `true` to require the host to provide a valid username and password during room initialization. Default is `false`.
- `host.user_auth`: Set to `true` to enable user authentication for hosts. Default is `false`.

- `host.users`: A JSON array containing user objects with usernames and passwords for valid host users.

Example Configuration:

```javascript
host: {
    protected: true,
    user_auth: false,
    users: [
        { username: 'username', password: 'password' },
        { username: 'username2', password: 'password2' },
        // Add more users as needed
    ],
},
```

---

## Host Protection Logic:

1. When host protection is enabled, hosts must log in using their username and password.
2. Upon successful login, the host's IP is recorded as a valid authentication IP.
3. Once logged in, the host gains the ability to create a room, join a room, and share the room link.
4. Guests are allowed to join the room while the host is logged in.
5. Upon host logout or browser exit, the host's IP is removed from the valid authentication IP list. This measure prevents unauthorized access.
6. After host logout, guests lose the ability to perform any actions within the room.
7. To regain access after host logout, the host needs to provide their username and password again.

---

## Room Initialization

To bypass the login page during room initialization, use URL parameters like this:

- [https://your.domain.com/join/?room=test&username=username&password=password](https://sfu.mirotalk.com/join/?room=test&username=username&password=password)

---

## Participant Room Entry

If `host.protected` is `enabled`, participants can join after host authentication using the URL path:

- [https://sfu.mirotalk.com/join/test](https://sfu.mirotalk.com/join/test)

Alternatively, use query parameters for additional settings:

- [https://your.domain.com/join/?room=test&roomPassword=0&name=mirotalksfu&audio=0&video=0&screen=0&notify=0](https://sfu.mirotalk.com/join/?room=test&roomPassword=0&name=mirotalksfu&audio=0&video=0&screen=0&notify=0)

---

## User Authentication for Participants:

If `host.user_auth` is `enabled`, participants must join with mandatory credentials using the URL path:

- [https://your.domain.com/join/?room=test&username=username&password=password](https://sfu.mirotalk.com/join/?room=test&username=username&password=password)

Alternatively, use query parameters for additional participant settings:

- [https://your.domain.com/join/?room=test&name=mirotalk&audio=0&video=0&screen=0&notify=0&username=username&password=password](https://sfu.mirotalk.com/join/?room=test&name=mirotalk&audio=0&video=0&screen=0&notify=0&username=username&password=password)

---
