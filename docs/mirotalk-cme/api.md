# REST API

![api](../images/api.png)

The REST API is comprehensively documented using [Swagger](https://swagger.io/), accessible at [https://YOUR-DOMAIN-NAME/api/v1/docs](https:/cme.mirotalk.com/api/v1/docs).

---

## Users Entry Point

Get a lists of all connected users

### JavaScript Example

```javascript
'use strict';

// Optionally filter by room: append ?room=Support (returns all rooms when omitted)
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

// Optionally filter by room: append ?room=Support (returns all rooms when omitted)
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

# Optionally filter by room: append ?room=Support (returns all rooms when omitted)
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

# Optionally filter by room: append ?room=Support (returns all rooms when omitted)
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

// Optionally scope to a room: append &room=Support (defaults to the public room)
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

// Optionally scope to a room: append &room=Support (defaults to the public room)
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

# Optionally scope to a room: append &room=Support (defaults to the public room)
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

# Optionally scope to a room: append &room=Support (defaults to the public room)
url="http://localhost:8000/api/v1/connected?user=call-me";

authorization="call_me_api_key_secret"

response=$(curl -s -X GET "$url" -H "authorization: call_me_api_key_secret" -H "Content-Type: application/json")

echo "$response"
```

---

## Rooms Entry Point

List active rooms with user counts and active call counts

### JavaScript Example

```javascript
'use strict';

// List active rooms with user counts and active call counts
const url = 'http://localhost:8000/api/v1/rooms';

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

// List active rooms with user counts and active call counts
$url = "http://localhost:8000/api/v1/rooms";

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

# List active rooms with user counts and active call counts
url = "http://localhost:8000/api/v1/rooms"

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

# List active rooms with user counts and active call counts
url="http://localhost:8000/api/v1/rooms";

authorization="call_me_api_key_secret"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```

---

## Calls Entry Point

Get a list of active calls

### JavaScript Example

```javascript
'use strict';

// Optionally filter by room: append ?room=Support (returns all rooms when omitted)
const url = 'http://localhost:8000/api/v1/calls';

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

// Optionally filter by room: append ?room=Support (returns all rooms when omitted)
$url = "http://localhost:8000/api/v1/calls";

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

# Optionally filter by room: append ?room=Support (returns all rooms when omitted)
url = "http://localhost:8000/api/v1/calls"

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

# Optionally filter by room: append ?room=Support (returns all rooms when omitted)
url="http://localhost:8000/api/v1/calls";

authorization="call_me_api_key_secret"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```

---

## Stats Entry Point

Aggregate server statistics: version, uptime, total users, rooms and active calls

### JavaScript Example

```javascript
'use strict';

// Aggregate server statistics: version, uptime, total users, rooms and active calls
const url = 'http://localhost:8000/api/v1/stats';

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

// Aggregate server statistics: version, uptime, total users, rooms and active calls
$url = "http://localhost:8000/api/v1/stats";

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

# Aggregate server statistics: version, uptime, total users, rooms and active calls
url = "http://localhost:8000/api/v1/stats"

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

# Aggregate server statistics: version, uptime, total users, rooms and active calls
url="http://localhost:8000/api/v1/stats";

authorization="call_me_api_key_secret"

response=$(curl -s -X GET "$url" -H "Authorization: $authorization" -H "Content-Type: application/json")

echo "$response"
```