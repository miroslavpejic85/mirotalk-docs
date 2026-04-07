# REST API

![api](../images/api.png)

The REST API is comprehensively documented using [Swagger](https://swagger.io/), accessible at [https://YOUR-DOMAIN-NAME/api/v1/docs](https:/cme.mirotalk.com/api/v1/docs).

---

## Users Entry Point

Get a lists of all connected users

### JavaScript Example

```javascript
'use strict';

const url = 'http://localhost:8000/api/v1/users';

const authorization = 'call_me_api_key_secret';

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

$url = "http://localhost:8000/api/v1/users";

$authorization = "call_me_api_key_secret";

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

url = "http://localhost:8000/api/v1/users"

authorization = "call_me_api_key_secret"

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

url="http://localhost:8000/api/v1/users";

authorization="call_me_api_key_secret"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```

---

## Connected Entry Point

Get a lists of all connected users to call

### JavaScript Example

```javascript
'use strict';

const url = 'http://localhost:8000/api/v1/connected?user=call-me';

const authorization = 'call_me_api_key_secret';

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

$url = "http://localhost:8000/api/v1/connected?user=call-me";

$authorization = "call_me_api_key_secret";

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

url = "http://localhost:8000/api/v1/connected?user=call-me"

authorization = "call_me_api_key_secret"

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

url="http://localhost:8000/api/v1/connected?user=call-me";

authorization="call_me_api_key_secret"

response=$(curl -s -X GET "$url" -H "authorization: call_me_api_key_secret" -H "Content-Type: application/json")

echo "$response"
```