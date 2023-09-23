# REST API

The REST API is comprehensively documented using [Swagger](https://swagger.io/), accessible at [https://your.domain.com/api/v1/docs](https://p2p.mirotalk.com/api/v1/docs).

---

## Meeting Entry Point

Upon a successful request, the API response will provide a Meeting Entry Point or Room URL. The authorization for this request is determined by the `API_KEY_SECRET` configuration specified in your `.env` file.

## JavaScript Example

```javascript
"use strict";

try {
  // Dynamically import 'node-fetch' with 'await'
  const { default: fetch } = await import("node-fetch");

  const API_KEY_SECRET = "mirotalk_default_secret";
  const MIROTALK_URL = "https://p2p.mirotalk.com/api/v1/meeting";

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

## PHP Example

```php
$API_KEY_SECRET = "mirotalk_default_secret";
$MIROTALK_URL = "https://p2p.mirotalk.com/api/v1/meeting";

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

## Python Example

```python
import requests
import json

API_KEY_SECRET = "mirotalk_default_secret"
MIROTALK_URL = "https://p2p.mirotalk.com/api/v1/meeting"

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

## Bash Example

```bash
#!/bin/bash

API_KEY_SECRET="mirotalk_default_secret"
MIROTALK_URL="https://p2p.mirotalk.com/api/v1/meeting"

curl $MIROTALK_URL \
    --header "authorization: $API_KEY_SECRET" \
    --header "Content-Type: application/json" \
    --request POST
```

---

**Note:** Replace `p2p.mirotalk.com` in the code snippets with `your.domain.com`.

---

