# MiroTalk C2C Self-Hosting Guide

## Requirements

- Server Selection: Recommended [Hetzner](https://www.hetzner.com/cloud) (CX11) or [Contabo](https://www.dpbolvw.net/click-101027391-14462707) (VPS-S) OS: Ubuntu 22.04 LTS.
- Use my [personal link](https://hetzner.cloud/?ref=XdRifCzCK3bn) to receive `€⁠20 in cloud credits` on Hetzner.
- [Node.js](https://nodejs.org/en/) (LTS) and npm
- Domain or Subdomain Name (e.g., `your.domain.name`) with a DNS A record pointing to your server's IPv4 address.
- `Recommend` utilizing a [Turn Server](../coturn/stun-turn.md) the installation documentation accessible [here](../coturn/installation.md).

---

## Installation

Install `NodeJS 18.X` and `npm` using [Node Version Manager](../nvm/nvm.md)

---

## Quick start

```bash
# Clone the project repo
$ git clone https://github.com/miroslavpejic85/mirotalkc2c.git

# Go to project dir
$ cd mirotalkc2c

# Copy .env.template in .env and customize it according to your needs if needed
$ cp .env.template .env

# Install dependencies
$ npm install

# Start the server
$ npm start
```

Check if is correctly installed: [http://your.domain.name:8080](http://your.domain.name:8080)

---

## Using PM2 (Process Manager)

![pm2](../images/pm2.png)

Install [PM2](https://pm2.keymetrics.io):

```bash
# Install pm2
$ npm install -g pm2

# Start the server
$ pm2 start backend/server.js

# Takes a snapshot
$ pm2 save

# Add it on startup
$ pm2 startup
```

---

## Using Docker

![docker](../images/docker.png)

Install `Docker` and `Docker Compose`:

```bash
# Install docker
$ sudo apt install docker.io

# Instal docker-compose
$ sudo apt install docker-compose

# Copy .env.template in .env and customize it according to your needs if needed
$ cp .env.template .env

# Copy docker-compose.template.yml in docker-compose.yml and customize it according to your needs if needed
$ cp docker-compose.template.yml docker-compose.yml

# Pull the official Docker image
$ docker pull mirotalk/c2c:latest

# Create and start containers (-d as daemon)
$ docker-compose up
```

Check if is correctly installed: [http://your.domain.name:8080](http://your.domain.name:8080)

---

## Configuring Nginx & Certbot

![nginx](../images/nginx.png)

In order to use it without the port number and to have encrypted communications (`mandatory to make it work correctly`), we going to install [nginx](https://www.nginx.com) and [certbot](https://certbot.eff.org)

```bash
# Install Nginx
$ sudo apt-get install nginx

# Install Certbot (SSL certificates)
$ sudo apt install snapd
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

Add the following:

```bash
# MiroTalk C2C - HTTPS — proxy all requests to the Node app
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
        proxy_pass http://localhost:8080/;
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

Check Your MiroTalk C2C instance: [https://your.domain.name](https://your.domain.name)

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

# MiroTalk C2C - HTTPS — proxy all requests to the Node app
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
        ProxyPass http://localhost:8080/
        ProxyPassReverse http://localhost:8080/

        ProxyPreserveHost On

        RequestHeader set X-Forwarded-For "%{REMOTE_ADDR}s"
        RequestHeader set X-Forwarded-Proto "https"
        RequestHeader set Host "%{HTTP_HOST}s"

        # Enable WebSocket proxy support for Socket.IO
        RewriteEngine On
        RewriteCond %{HTTP:Upgrade} =websocket [NC]
        RewriteRule /(.*) ws://localhost:8080/socket.io/$1 [P,L]
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

To keep your MiroTalk C2C instance up to date, create an update script:

```bash
$ cd
# Create a file c2cUpdate.sh
$ vim c2cUpdate.sh
```

---

For `PM2`:

```bash
#!/bin/bash

cd mirotalkc2c
git pull
pm2 stop backend/server.js
sudo npm install
pm2 start server.js
```

---

For `Docker`:

```bash
#!/bin/bash

cd mirotalkc2c
git pull
docker-compose down
docker-compose pull
docker images |grep '<none>' |awk '{print $3}' |xargs docker rmi
docker-compose up -d
```

---

Make the script executable:

```bash
$ chmod +x c2cUpdate.sh
```

To update your MiroTalk C2C instance to the latest version, run the script:

```bash
./c2cUpdate.sh
```

---

## Changelogs

Stay informed about project updates by following the commits of the MiroTalk C2C project [here](https://github.com/miroslavpejic85/mirotalkc2c/commits/main).

---
