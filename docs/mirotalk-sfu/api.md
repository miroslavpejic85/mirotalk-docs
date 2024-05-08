# REST API

![api](../images/api.png)

The REST API is comprehensively documented using [Swagger](https://swagger.io/), accessible at [https://your.domain.com/api/v1/docs](https://sfu.mirotalk.com/api/v1/docs).

---

## Meetings Entry Point

Upon a successful request, the API response will provide the active Meetings. The authorization for this request is determined by the `api.keySecret` configuration specified in your `config.js` file.

```javascript
"use strict";

// npm i node-fetch

async function getMeetings() {
  try {
    // Use dynamic import with await
    const { default: fetch } = await import("node-fetch");

    const API_KEY_SECRET = "mirotalksfu_default_secret";
    const MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/meetings";

    const response = await fetch(MIROTALK_URL, {
      method: "GET",
      headers: {
        authorization: API_KEY_SECRET,
        "Content-Type": "application/json",
      },
    });
    const data = await response.json();
    if (data.error) {
      console.log("Error:", data.error);
    } else {
      if (data && data.meetings) {
        const meetings = data.meetings;
        const formattedData = JSON.stringify({ meetings }, null, 2);
        console.log(formattedData);
      }
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
}

getMeetings();
```

### PHP Example

```php
<?php

$API_KEY_SECRET = "mirotalksfu_default_secret";
$MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/meetings";

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $MIROTALK_URL);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_HTTPGET, true);

$headers = [
    'authorization:' . $API_KEY_SECRET,
    'Content-Type: application/json'
];

curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status code: $httpcode \n";

if ($response) {
    echo json_encode(json_decode($response), JSON_PRETTY_PRINT);
} else {
    echo "Failed to retrieve data.\n";
}
```

### Python Example

```python
# pip3 install requests
import requests
import json

API_KEY_SECRET = "mirotalksfu_default_secret"
MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/meetings"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

response = requests.get(
    MIROTALK_URL,
    headers=headers
)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    pretty_printed_data = json.dumps(data, indent=4)
    print(data)
else:
    print("Failed to retrieve data. Error:", response.text)
```

### Bash Example

```bash
#!/bin/bash

API_KEY_SECRET="mirotalksfu_default_secret"
MIROTALK_URL="https://sfu.mirotalk.com/api/v1/meetings"

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --request GET
```

---

## Meeting Entry Point

Upon a successful request, the API response will provide a Meeting Entry Point or Room URL. The authorization for this request is determined by the `api.keySecret` configuration specified in your `config.js` file.

### JavaScript Example

```javascript
"use strict";

// npm i node-fetch

try {
  // Dynamically import 'node-fetch' with 'await'
  const { default: fetch } = await import("node-fetch");

  const API_KEY_SECRET = "mirotalksfu_default_secret";
  const MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/meeting";

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

$API_KEY_SECRET = "mirotalksfu_default_secret";
$MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/meeting";

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

API_KEY_SECRET = "mirotalksfu_default_secret"
MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/meeting"

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

API_KEY_SECRET="mirotalksfu_default_secret"
MIROTALK_URL="https://sfu.mirotalk.com/api/v1/meeting"

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --request POST
```

---

## Direct Join Entry Point

Upon a successful request, the API response will provide a Meeting Entry Point for the direct join to the room. The authorization for this request is determined by the `api.keySecret` configuration specified in your `config.js` file.

### JavaScript Join example

```javascript
"use strict";

// npm i node-fetch

try {
  // Use dynamic import with await
  const { default: fetch } = await import("node-fetch");

  const API_KEY = "mirotalksfu_default_secret";
  const MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/join";

  const response = await fetch(MIROTALK_URL, {
    method: "POST",
    headers: {
      authorization: API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      room: "test",
      roomPassword: false,
      name: "mirotalksfu",
      audio: true,
      video: true,
      screen: false,
      hide: false,
      notify: true,
      // Token configuration is required if the host system is protected, user authentication is needed, or a room presenter is specified.
      token: {
        username: "username",
        password: "password",
        presenter: true,
        expire: "1h",
      },
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

$API_KEY_SECRET = "mirotalksfu_default_secret";
$MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/join";

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
    "roomPassword"  => false,
    "name"          => "mirotalksfu",
    "audio"         => true,
    "video"         => true,
    "screen"        => false,
    "hide"          => false,
    "notify"        => true,
    // Token configuration is required if the host system is protected, user authentication is needed, or a room presenter is specified
    "token"         => array(
        "username"      => "username",
        "password"      => "password",
        "presenter"     => true,
        "expire"        => "1h",
    ),
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

API_KEY_SECRET = "mirotalksfu_default_secret"
MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/join"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

data = {
    "room": "test",
    "roomPassword": "false",
    "name": "mirotalksfu",
    "audio": "true",
    "video": "true",
    "screen": "false",
    "hide": "false",
    "notify": "true",
    # Token configuration is required if the host system is protected, user authentication is needed, or a room presenter is specified
    "token": {
        "username": "username",
        "password": "password",
        "presenter": "true",
        "expire": "1h",
    }
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

API_KEY_SECRET="mirotalksfu_default_secret"
MIROTALK_URL="https://sfu.mirotalk.com/api/v1/join"

# Token configuration is required if the host system is protected, user authentication is needed, or a room presenter is specified

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --data '{"room":"test","roomPassword":"false","name":"mirotalksfu","audio":"true","video":"true","screen":"false","hide":"false","notify":"true", "token":{"username":"username","password":"password","presenter":"true", "expire":"1h"}}' \
    --request POST
```

---

## Token Entry Point

Upon a successful request, the API response will provide a valid Token for the meeting. The authorization for this request is determined by the `api.keySecret` configuration specified in your `config.js` file.

### JavaScript Token example

```javascript
"use strict";

// npm i node-fetch

try {
  // Use dynamic import with await
  const { default: fetch } = await import("node-fetch");

  const API_KEY_SECRET = "mirotalksfu_default_secret";
  const MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/token";

  const response = await fetch(MIROTALK_URL, {
    method: "POST",
    headers: {
      authorization: API_KEY_SECRET,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username: "username",
      password: "password",
      presenter: true,
      expire: "1h",
    }),
  });
  const data = await response.json();
  if (data.error) {
    console.log("Error:", data.error);
  } else {
    console.log("token:", data.token);
  }
} catch (error) {
  console.error("Error fetching data:", error);
}
```

---

### PHP Token example

```php
<?php

$API_KEY_SECRET = "mirotalksfu_default_secret";
$MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/token";

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
    "username"      => "username",
    "password"      => "password",
    "presenter"     => true,
    "expire"        => "1h",
);

$data_string = json_encode($data);

curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status code: $httpcode \n";
$data = json_decode($response);
echo "token: ", $data->{'token'}, "\n";
```

---

### Python Token example

```py
# pip3 install requests

import requests
import json

API_KEY_SECRET = "mirotalksfu_default_secret"
MIROTALK_URL = "https://sfu.mirotalk.com/api/v1/token"

headers = {
    "authorization": API_KEY_SECRET,
    "Content-Type": "application/json",
}

data = {
    "username": "username",
    "password": "password",
    "presenter": "true",
    "expire": "1h"
}

response = requests.post(
    MIROTALK_URL, 
    headers=headers, 
    json=data
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("token:", data["token"])
```

---

### Bash Token example

```bash
#!/bin/bash

API_KEY_SECRET="mirotalksfu_default_secret"
MIROTALK_URL="https://sfu.mirotalk.com/api/v1/token"

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --data '{"username":"username","password":"password","presenter":"true", "expire":"1h"}' \
    --request POST
```

---

!!! note

    - Replace `sfu.mirotalk.com` in the code snippets with `your.domain.com`.
    - In the `app/src/config` under the `api` section, you can enable or disable these endpoints in the `allowed` section.

    ```javascript
    api: {
        // Default secret key for app/api
        keySecret: 'mirotalksfu_default_secret',
        // Define which endpoints are allowed
        allowed: {
            meetings: true,
            meeting: true,
            join: true,
            token: true,
            // Add more endpoints here as needed
        },
    },
    ```
---
