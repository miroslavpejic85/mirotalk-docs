---
title: MiroTalk CME REST API
description: Authenticate with the MiroTalk CME REST API and query connected users, rooms, calls, and server statistics.
---

# MiroTalk CME REST API

![MiroTalk CME REST API documentation](../images/api.png)

Use the CME REST API to inspect active users, rooms, and calls from a trusted backend service. The complete interactive contract is available in [CME Swagger](https://cme.mirotalk.com/api/v1/docs) or at `https://YOUR-DOMAIN-NAME/api/v1/docs` on a self-hosted instance.

## Before you begin

- Set `YOUR-DOMAIN-NAME` to the hostname of your CME deployment.
- Set `YOUR_API_KEY_SECRET` to the API secret configured on that deployment.
- Send the secret in the `Authorization` request header for protected endpoints.
- Keep production secrets on the server. Do not expose them in browser-delivered JavaScript.

All endpoints below use the base URL `https://YOUR-DOMAIN-NAME/api/v1` and return JSON. The contract reflects the deployed CME Swagger specification, Call-me API 1.1.0.

| Method and path | Auth | Query parameters | `200` response | Error |
| --- | --- | --- | --- | --- |
| `GET /users` | Required | `room` optional; `details=true` returns detailed descriptors | `UsersResponse` | `403 Unauthorized` |
| `GET /connected` | Required | `user` required; `room` optional and defaults to the public room | `connectedResponse` | `403 Unauthorized` |
| `GET /vapidPublicKey` | Not required | None | `VapidPublicKeyResponse` | Not specified |
| `GET /rooms` | Required | None | `RoomsResponse` | `403 Unauthorized` |
| `GET /calls` | Required | `room` optional | `CallsResponse` | `403 Unauthorized` |
| `GET /stats` | Required | None | `StatsResponse` | `403 Unauthorized` |

---

## `GET /users`

Get a lists of all connected users

### JavaScript Example

```javascript
'use strict';

// Optionally append ?room=Support or ?details=true
const url = 'https://YOUR-DOMAIN-NAME/api/v1/users';

const authorization = 'YOUR_API_KEY_SECRET';

fetch(url, {
    method: 'GET',
    headers: {
        Authorization: authorization,
        'Content-Type': 'application/json',
    },
})
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));

```

### PHP Example

```php
<?php

// Optionally append ?room=Support or ?details=true
$url = "https://YOUR-DOMAIN-NAME/api/v1/users";

$authorization = "YOUR_API_KEY_SECRET";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "authorization: $authorization",
    "Content-Type: application/json"
));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### Python Example

```python
import requests # pip3 install requests

# Optionally append ?room=Support or ?details=true
url = "https://YOUR-DOMAIN-NAME/api/v1/users"

authorization = "YOUR_API_KEY_SECRET"

headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.json())
```

### Bash Example

```bash
#!/bin/bash

# Optionally append ?room=Support or ?details=true
url="https://YOUR-DOMAIN-NAME/api/v1/users";

authorization="YOUR_API_KEY_SECRET"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```

---

## `GET /connected`

Get a lists of all connected users to call

### JavaScript Example

```javascript
'use strict';

// Optionally scope to a room: append &room=Support (defaults to the public room)
const url = 'https://YOUR-DOMAIN-NAME/api/v1/connected?user=call-me';

const authorization = 'YOUR_API_KEY_SECRET';

fetch(url, {
    method: 'GET',
    headers: {
        Authorization: authorization,
        'Content-Type': 'application/json',
    },
})
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
```

### PHP Example

```php
<?php

// Optionally scope to a room: append &room=Support (defaults to the public room)
$url = "https://YOUR-DOMAIN-NAME/api/v1/connected?user=call-me";

$authorization = "YOUR_API_KEY_SECRET";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "authorization: $authorization",
    "Content-Type: application/json"
));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### Python Example

```python
import requests  # pip3 install requests

# Optionally scope to a room: append &room=Support (defaults to the public room)
url = "https://YOUR-DOMAIN-NAME/api/v1/connected?user=call-me"

authorization = "YOUR_API_KEY_SECRET"

headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.json())
```

### Bash Example

```bash
#!/bin/bash

# Optionally scope to a room: append &room=Support (defaults to the public room)
url="https://YOUR-DOMAIN-NAME/api/v1/connected?user=call-me";

authorization="YOUR_API_KEY_SECRET"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```

---

## `GET /vapidPublicKey`

Get the public VAPID key used to create Web Push subscriptions. This endpoint does not require the API secret.

### Bash Example

```bash
#!/bin/bash

url="https://YOUR-DOMAIN-NAME/api/v1/vapidPublicKey"

curl -s -X GET "$url" -H "Content-Type: application/json"
```

---

## `GET /rooms`

List active rooms with user counts and active call counts

### JavaScript Example

```javascript
'use strict';

// List active rooms with user counts and active call counts
const url = 'https://YOUR-DOMAIN-NAME/api/v1/rooms';

const authorization = 'YOUR_API_KEY_SECRET';

fetch(url, {
    method: 'GET',
    headers: {
        Authorization: authorization,
        'Content-Type': 'application/json',
    },
})
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
```

### PHP Example

```php
<?php

// List active rooms with user counts and active call counts
$url = "https://YOUR-DOMAIN-NAME/api/v1/rooms";

$authorization = "YOUR_API_KEY_SECRET";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "authorization: $authorization",
    "Content-Type: application/json"
));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### Python Example

```python
import requests  # pip3 install requests

# List active rooms with user counts and active call counts
url = "https://YOUR-DOMAIN-NAME/api/v1/rooms"

authorization = "YOUR_API_KEY_SECRET"

headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.json())
```

### Bash Example

```bash
#!/bin/bash

# List active rooms with user counts and active call counts
url="https://YOUR-DOMAIN-NAME/api/v1/rooms";

authorization="YOUR_API_KEY_SECRET"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```

---

## `GET /calls`

Get a list of active calls

### JavaScript Example

```javascript
'use strict';

// Optionally filter by room: append ?room=Support (returns all rooms when omitted)
const url = 'https://YOUR-DOMAIN-NAME/api/v1/calls';

const authorization = 'YOUR_API_KEY_SECRET';

fetch(url, {
    method: 'GET',
    headers: {
        Authorization: authorization,
        'Content-Type': 'application/json',
    },
})
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
```

### PHP Example

```php
<?php

// Optionally filter by room: append ?room=Support (returns all rooms when omitted)
$url = "https://YOUR-DOMAIN-NAME/api/v1/calls";

$authorization = "YOUR_API_KEY_SECRET";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "authorization: $authorization",
    "Content-Type: application/json"
));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### Python Example

```python
import requests  # pip3 install requests

# Optionally filter by room: append ?room=Support (returns all rooms when omitted)
url = "https://YOUR-DOMAIN-NAME/api/v1/calls"

authorization = "YOUR_API_KEY_SECRET"

headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.json())
```

### Bash Example

```bash
#!/bin/bash

# Optionally filter by room: append ?room=Support (returns all rooms when omitted)
url="https://YOUR-DOMAIN-NAME/api/v1/calls";

authorization="YOUR_API_KEY_SECRET"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```

---

## `GET /stats`

Aggregate server statistics: version, uptime, total users, rooms and active calls

### JavaScript Example

```javascript
'use strict';

// Aggregate server statistics: version, uptime, total users, rooms and active calls
const url = 'https://YOUR-DOMAIN-NAME/api/v1/stats';

const authorization = 'YOUR_API_KEY_SECRET';

fetch(url, {
    method: 'GET',
    headers: {
        Authorization: authorization,
        'Content-Type': 'application/json',
    },
})
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error:', error));
```

### PHP Example

```php
<?php

// Aggregate server statistics: version, uptime, total users, rooms and active calls
$url = "https://YOUR-DOMAIN-NAME/api/v1/stats";

$authorization = "YOUR_API_KEY_SECRET";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "authorization: $authorization",
    "Content-Type: application/json"
));

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### Python Example

```python
import requests  # pip3 install requests

# Aggregate server statistics: version, uptime, total users, rooms and active calls
url = "https://YOUR-DOMAIN-NAME/api/v1/stats"

authorization = "YOUR_API_KEY_SECRET"

headers = {
    'Authorization': authorization,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

print(response.json())
```

### Bash Example

```bash
#!/bin/bash

# Aggregate server statistics: version, uptime, total users, rooms and active calls
url="https://YOUR-DOMAIN-NAME/api/v1/stats";

authorization="YOUR_API_KEY_SECRET"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```