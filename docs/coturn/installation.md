# Coturn STUN/TURN Server

![stunTurn](../images/stun-turn.png)

## Requirements

-  Server Selection (Recommended: [Hetzner](https://www.hetzner.com/cloud) CX11, OS: Ubuntu 20.04 LTS / 22.04 LTS).
-  Use my [personal link](https://hetzner.cloud/?ref=XdRifCzCK3bn) to receive `€⁠20 in cloud credits`.
-  [Node.js](https://nodejs.org/en/) (LTS) and npm
-  Domain Name (e.g., `your.domain.name`) with a DNS A record pointing to your server's IPv4 address.
-   [Certbot](https://certbot.eff.org/) to generate `cert` & `pkey`.

## Installation

Install [coturn](https://github.com/coturn/coturn):

```bash
$ sudo apt-get -y update
$ sudo apt-get -y install coturn
```

Uncomment the following line to run Coturn as an automatic system service daemon in `/etc/default/coturn`

```ini
TURNSERVER_ENABLED=1
```

Open `/etc/turnserver.conf` and add the following:

```ini
listening-port=3478
tls-listening-port=5349

min-port=10000
max-port=20000

fingerprint
lt-cred-mech

user=your.username:your.password

server-name=your.domain.name
realm=your.domain.name

total-quota=100
stale-nonce=600

cert=/etc/letsencrypt/live/your.domain.name/fullchain.pem
pkey=/etc/letsencrypt/live/your.domain.name/privkey.pem
cipher-list="ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384"

no-stdout-log
```

If you can't reach coturn on `tls-listening-port`, try to edit `/etc/systemd/system/multi-user.target.wants/coturn.service`

```ini
[Service]
User=root
Group=root
```

Reload daemon:

```bash
$ sudo systemctl daemon-reload
```

## Coturn commands

```bash
$ sudo service coturn status
$ sudo service coturn stop
$ sudo service coturn start
$ sudo service coturn restart
```

# Test

Test if it's working:

-   [trickle-ice](https://webrtc.github.io/samples/src/content/peerconnection/trickle-ice/)
-   [icetest](https://icetest.info/)

You can also utilize the built-in MiroTalk service by simply replacing `your.domain.name`, `your.username` and `your.password` with your own values in the following URLs:

```ini
# Default listening port
https://p2p.mirotalk.com/test?iceServers=[{"urls":"stun:your.domain.name:3478"},{"urls":"turn:your.domain.name:3478","username":"your.username","credential":"your.password"}]

# Tls listening port
https://p2p.mirotalk.com/test?iceServers=[{"urls":"stun:your.domain.name:5349"},{"urls":"turn:your.domain.name:5349","username":"your.username","credential":"your.password"}]
```
