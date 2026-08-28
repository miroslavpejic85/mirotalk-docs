---
title: MiroTalk C2C REST API
description: Create meetings and direct call links with the authenticated MiroTalk C2C REST API.
---

# MiroTalk C2C REST API

![MiroTalk C2C REST API documentation](../images/api.png)

The deployed [C2C Swagger specification](https://c2c.mirotalk.com/api/v1/docs) identifies itself as MiroTalk C2C API 1.0.0 using OAS 2.0. A self-hosted instance exposes the same interface at `https://YOUR-DOMAIN-NAME/api/v1/docs`.

| Method | Path | Authentication | Purpose |
| --- | --- | --- | --- |
| `POST` | `/meeting` | `Authorization: YOUR_API_KEY_SECRET` | Create a meeting URL. |
| `POST` | `/join` | `Authorization: YOUR_API_KEY_SECRET` | Create a direct call join URL. |

!!! warning "Protect the API secret"
  Replace `YOUR_API_KEY_SECRET` with the value configured in `.env`. Keep it on a trusted backend and never ship it in public browser code.

---

## `POST /meeting`

Upon a successful request, the API response will provide a Meeting Entry Point or Room URL. The authorization for this request is determined by the `API_KEY_SECRET` configuration specified in your `.env` file.

### JavaScript Example

```javascript
"use strict";

// npm i node-fetch

try {
  // Dynamically import 'node-fetch' with 'await'
  const { default: fetch } = await import("node-fetch");

  const API_KEY_SECRET = "YOUR_API_KEY_SECRET";
  const MIROTALK_URL = "https://c2c.mirotalk.com/api/v1/meeting";

  const response = await fetch(MIROTALK_URL, {
    method: "POST",
    headers: {
      authorization: API_KEY_SECRET,
      "Content-Type": "application/json",
    },
  });

  const data = await response.json();

  if (data.error) {
    console.log("Error:", data.error);
  } else {
    console.log("Meeting:", data.meeting);
  }
} catch (error) {
  console.error("Error fetching data:", error);
}
```

### PHP Example

```php
<?php

$API_KEY_SECRET = "YOUR_API_KEY_SECRET";
$MIROTALK_URL = "https://c2c.mirotalk.com/api/v1/meeting";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $MIROTALK_URL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);

$headers = [
    'authorization:' . $API_KEY_SECRET,
    'Content-Type: application/json'
];

curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "HTTP Status Code: $httpcode \n";
$data = json_decode($response);
echo "Meeting: ", $data->{'meeting'}, "\n";
```

### Python Example

```python
# pip3 install requests

import requests
import json

API_KEY_SECRET = "YOUR_API_KEY_SECRET"
MIROTALK_URL = "https://c2c.mirotalk.com/api/v1/meeting"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

response = requests.post(
    MIROTALK_URL,
    headers=headers
)

print("HTTP Status Code:", response.status_code)
data = json.loads(response.text)
print("Meeting:", data["meeting"])
```

### Bash Example

```bash
#!/bin/bash

API_KEY_SECRET="YOUR_API_KEY_SECRET"
MIROTALK_URL="https://c2c.mirotalk.com/api/v1/meeting"

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --request POST
```

---

## `POST /join`

Upon a successful request, the API response will provide a Meeting Entry Point for the direct join to the room. The authorization for this request is determined by the `API_KEY_SECRET` configuration specified in your `.env` file.

### JavaScript Join example

```javascript
"use strict";

// npm i node-fetch

try {
  // Use dynamic import with await
  const { default: fetch } = await import("node-fetch");

  const API_KEY = "YOUR_API_KEY_SECRET";
  const MIROTALK_URL = "https://c2c.mirotalk.com/api/v1/join";

  const response = await fetch(MIROTALK_URL, {
    method: "POST",
    headers: {
      authorization: API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      room: "test",
      name: "mirotalkc2c",
    }),
  });
  const data = await response.json();
  if (data.error) {
    console.log("Error:", data.error);
  } else {
    console.log("join:", data.join);
  }
} catch (error) {
  console.error("Error fetching data:", error);
}
```

---

### PHP Join example

```php
<?php

$API_KEY_SECRET = "YOUR_API_KEY_SECRET";
$MIROTALK_URL = "https://c2c.mirotalk.com/api/v1/join";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $MIROTALK_URL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);

$headers = [
    'authorization:' . $API_KEY_SECRET,
    'Content-Type: application/json'
];

curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$data = array(
    "room"          => "test",
    "name"          => "mirotalkc2c",
);
$data_string = json_encode($data);

curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status code: $httpcode \n";
$data = json_decode($response);
echo "join: ", $data->{'join'}, "\n";
```

---

### Python Join example

```py
# pip3 install requests

import requests
import json

API_KEY_SECRET = "YOUR_API_KEY_SECRET"
MIROTALK_URL = "https://c2c.mirotalk.com/api/v1/join"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

data = {
    "room": "test",
    "name": "mirotalkc2c",
}

response = requests.post(
    MIROTALK_URL,
    headers=headers,
    json=data,
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("join:", data["join"])
```

---

### Bash Join example

```bash
#!/bin/bash

API_KEY_SECRET="YOUR_API_KEY_SECRET"
MIROTALK_URL="https://c2c.mirotalk.com/api/v1/join"

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --data '{"room":"test","name":"mirotalkc2c"}' \
    --request POST
```

---

!!! note

    Replace `c2c.mirotalk.com` in the code snippets with `YOUR-DOMAIN-NAME`.

---
