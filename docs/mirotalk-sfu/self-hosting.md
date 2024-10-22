# MiroTalk SFU - Self Hosting

## Requirements

- Server Selection:
    - [Hetzner](https://www.hetzner.com/cloud) (CPX11) - Use [this link](https://hetzner.cloud/?ref=XdRifCzCK3bn) to receive `€⁠20 in cloud credits`
    - [Contabo](https://www.dpbolvw.net/click-101027391-14462707) (VPS-1)
- OS: Ubuntu 22.04 LTS.
- [Node.js](https://nodejs.org/en/) (LTS) and npm
- [FFmpeg](https://ffmpeg.org/download.html) for optional [RTMP](../mirotalk-sfu/rtmp.md) streaming support.
- Domain or Subdomain Name (e.g., `your.domain.name`) with a DNS A record pointing to your server's IPv4 address.

---

## Installation

!!! note

    Many of the installation steps require `root` or `sudo` access

```bash
# Gcc g++ make
$ apt-get update
$ apt-get install -y build-essential

# Python 3.8 and pip
$ DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata
$ apt install -y software-properties-common
$ add-apt-repository -y ppa:deadsnakes/ppa
$ apt update
$ apt install -y python3.8 python3-pip

# FFmpeg
$ apt install -y ffmpeg
```

---

Install `NodeJS 18.X` and `npm` using [Node Version Manager](../utility/nvm.md)

---

## Quick start

```bash
# Clone this repo
$ git clone https://github.com/miroslavpejic85/mirotalksfu.git

# Go to to dir mirotalksfu
$ cd mirotalksfu

# Copy app/src/config.template.js in app/src/config.js
$ cp app/src/config.template.js app/src/config.js
```

---

### Config.js

Change the `IPv4` with `Your Server public IPv4` in `app/src/config.js`

```js
const IPv4 = 'Your Server Public IPv4'; // This is your server's public IP address. If you're using AWS EC2, you'll use the Elastic IP associated with your instance, as this is the public IP that's persistent across reboots.
```

<br /> 

```javascript
{
    protocol: "udp",
    ip: "0.0.0.0",
    announcedAddress: IPv4,
    portRange: { min: 40000, max: 40100 } },
{
    protocol: "tcp",
    ip: "0.0.0.0",
    announcedAddress: IPv4,
    portRange: { min: 40000, max: 40100 }
},

// If you are not behind a NAT
{
    protocol: "udp",
    ip: IPv4,
    portRange: { min: 40000, max: 40100 }
},
{
    protocol: "tcp",
    ip: IPv4,
    portRange: { min: 40000, max: 40100 }
},
```

### FireWall

Set the `inbound rules` if needed

| Port range  | Protocol | Source    | Description         |
| ----------- | -------- | --------- | ------------------- |
| 3010        | TCP      | 0.0.0.0/0 | App listen on tcp   |
| 40000-40100 | TCP      | 0.0.0.0/0 | RTC port ranges tcp |
| 40000-40100 | UDP      | 0.0.0.0/0 | RTC port ranges udp |

```bash
# Check the firewall Status: (active/inactive)
ufw status

# If active then allow traffic
ufw allow 3010/tcp
ufw allow 40000:40100/tcp
ufw allow 40000:40100/udp

# ssh, http, https, nginx...
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
```

---

### WebRTCServer (optional)

You can activate the `WebRTCServer` option by setting `webRtcServerActive: true` in the `app/src/config.js`.

Here's how it works:

- MiroTalk instantiates a `Worker` for each `CPU`.
- Each `Worker` has its own `WebRTCServer`, which listens on a single port starting from `40000`.
- This setup simplifies port management because you only need to open ports for the number of `Workers` you have.

```javascript
{
    protocol: 'udp',
    ip: '0.0.0.0',
    announcedAddress: IPv4,
    portRange: { min: 40000, max: 40000 + numWorkers }
},
{
    protocol: 'tcp',
    ip: '0.0.0.0',
    announcedAddress: IPv4,
    portRange: { min: 40000, max: 40000 + numWorkers }
},
```

---

### Install dependencies and start the server

```bash
# Install dependencies - be patient, the first time will take a few minutes, in the meantime have a good coffee ;)
$ npm install

# Start the server
$ npm start
```

Check if is correctly installed: [http://your.domain.name:3010](http://your.domain.name:3010)

---

## Using [PM2](https://pm2.keymetrics.io) (Process Manager)

![pm2](../images/pm2.png)

```bash
# Install pm2
$ npm install -g pm2

# Start the server
$ pm2 start app/src/Server.js

# Takes a snapshot
$ pm2 save

# Add it on startup
$ pm2 startup
```

---

## Using Docker

![docker](../images/docker.png)

```bash
# Install docker
$ sudo apt install -y docker.io

# Instal docker-compose
$ sudo apt install -y docker-compose

# Clone this repo
$ git clone https://github.com/miroslavpejic85/mirotalksfu.git

# Go to to dir mirotalksfu
$ cd mirotalksfu

# Copy app/src/config.template.js in app/src/config.js IMPORTANT (edit it according to your needs)
$ cp app/src/config.template.js app/src/config.js

# Copy docker-compose.template.yml in docker-compose.yml and customize it according to your needs if needed
$ cp docker-compose.template.yml docker-compose.yml

# Pull the official Docker image
$ docker pull mirotalk/sfu:latest

# Create and start containers (-d as daemon)
$ docker-compose up
```

Check if is correctly installed: [http://your.domain.name:3010](http://your.domain.name:3010)

---

## Configuring Nginx & Certbot

![nginx](../images/nginx.png)

In order to use it without the port number and to have encrypted communications (`mandatory to make it work correctly`), we going to install [nginx](https://www.nginx.com) and [certbot](https://certbot.eff.org)

```bash
# Install Nginx
$ sudo apt-get install -y nginx

# Install Certbot (SSL certificates)
$ sudo apt install -y snapd
$ sudo snap install core; sudo snap refresh core
$ sudo snap install --classic certbot
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Configure Nginx
$ sudo vim /etc/nginx/sites-enabled/default
```

Add the following:

```bash
# HTTP — redirect all traffic to HTTPS
server {
    listen 80;
    listen [::]:80;
    server_name your.domain.name;

    return 301 https://$host$request_uri;
}
```

```bash
# Test Nginx configuration
$ sudo nginx -t

# Enable HTTPS with Certbot (follow the instruction)
$ sudo certbot certonly --nginx

# Add Let's Encrypt configuration to Nginx
$ sudo vim /etc/nginx/sites-enabled/default
```

Paste this:

```bash
# MiroTalk SFU - HTTPS — proxy all requests to the Node app
server {
    # Enable HTTP/2
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name your.domain.name;

    # Use the Let’s Encrypt certificates
    ssl_certificate /etc/letsencrypt/live/your.domain.name/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your.domain.name/privkey.pem;

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_pass http://localhost:3010/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

```bash
# Test Nginx configuration again
$ sudo nginx -t

# Restart nginx
$ service nginx restart
$ service nginx status

# Set up auto-renewal for SSL certificates
$ sudo certbot renew --dry-run

# Show certificates
$ sudo certbot certificates
```

Check Your MiroTalk SFU instance: [http://your.domain.name](http://your.domain.name)

---

## Apache Virtual Host (Alternative to Nginx)

![apache](../images/apache.png)

If you prefer `Apache`, configure it with the equivalent settings provided in this guide.

```bash
# Edit the apache sites
vim /etc/apache2/sites-enabled/your.domain.name.conf
```

Add the following:

```bash
# HTTP — redirect all traffic to HTTPS
<VirtualHost *:80>
    ServerName your.domain.name
    Redirect permanent / https://your.domain.name
</VirtualHost>

# MiroTalk SFU - HTTPS — proxy all requests to the Node app
<VirtualHost *:443>
    ServerName your.domain.name

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/your.domain.name/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/your.domain.name/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf

    # Enable HTTP/2 support
    Protocols h2 http/1.1

    <Location />
        # Proxy Configuration for Node.js App
        ProxyPass http://localhost:3010/
        ProxyPassReverse http://localhost:3010/

        ProxyPreserveHost On

        RequestHeader set X-Forwarded-For "%{REMOTE_ADDR}s"
        RequestHeader set X-Forwarded-Proto "https"
        RequestHeader set Host "%{HTTP_HOST}s"

        # Enable WebSocket proxy support for Socket.IO
        RewriteEngine On
        RewriteCond %{HTTP:Upgrade} =websocket [NC]
        RewriteRule /(.*) ws://localhost:3010/socket.io/$1 [P,L]
        # Adjust the WebSocket path according to your Socket.IO configuration
        # For Socket.IO 3.x or higher, use /socket.io/?EIO=4&transport=websocket
    </Location>
</VirtualHost>
```

```bash
# Check configuration
sudo apache2ctl configtest

sudo a2enmod proxy # Enables the `mod_proxy` module, which is essential for proxying HTTP and WebSocket connections.
sudo a2enmod proxy_http # Enables the `mod_proxy_http` module, which adds support for proxying HTTP connections.
sudo a2enmod proxy_wstunnel # Enables the `mod_proxy_wstunnel` module, which provides support for tunneling WebSocket connections

# Restart apache
sudo systemctl restart apache2
```

---

## Updating Your Instance

To keep your MiroTalk SFU instance up to date, create an update script:

```bash
cd
# Create a file sfuUpdate.sh
$ vim sfuUpdate.sh
```

---

For `PM2`:

```bash
#!/bin/bash

cd mirotalksfu
git pull
pm2 stop app/src/Server.js
sudo npm install
pm2 start app/src/Server.js
```

---

For `Docker`:

```bash
#!/bin/bash

cd mirotalksfu
git pull
docker pull mirotalk/sfu:latest
docker-compose up -d
docker images |grep '<none>' |awk '{print $3}' |xargs docker rmi
```

---

Make the script executable

```bash
$ chmod +x sfuUpdate.sh
```

To update your MiroTalk SFU instance to the latest version, run the script:

```bash
./sfuUpdate.sh
```

---

## Changelogs

Stay informed about project updates by following the commits of the MiroTalk SFU project [here](https://github.com/miroslavpejic85/mirotalksfu/commits/main)

---
