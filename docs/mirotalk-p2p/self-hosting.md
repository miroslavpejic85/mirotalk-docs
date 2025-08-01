# MiroTalk P2P - Self Hosting

![mirotalk-p2p](../images/mirotalk/p2p.png)

## Requirements

- Server Selection:
    - [Hetzner](https://www.hetzner.com/cloud) (CX11) - Use [this link](https://hetzner.cloud/?ref=XdRifCzCK3bn) to receive `€⁠20 in cloud credits`
    - [Hostinger](https://hostinger.com/?REFERRALCODE=MIROTALK) (KVM 2)
    - [Contabo](https://www.dpbolvw.net/click-101027391-14462707) (VPS-1)
- OS: Ubuntu 22.04 LTS.
- [Node.js](https://nodejs.org/en/) (LTS) and npm
- Domain or Subdomain Name (e.g., `YOUR.DOMAIN.NAME`) with a DNS A record pointing to your server's IPv4 address.
- `Recommend` utilizing a [Turn Server](../coturn/stun-turn.md) the installation documentation accessible [here](../coturn/installation.md).

---

## Installation

![nodejs](../images/nodejs.png)

Install `NodeJS` and `npm` using [Node Version Manager](../utility/nvm.md)

---

## Quick start

```bash
# Clone MiroTalk P2P repo
$ git clone https://github.com/miroslavpejic85/mirotalk.git

# Go to mirotalk dir
$ cd mirotalk

# Copy .env.template to .env and customize it according to your needs if needed
$ cp .env.template .env

# Copy app/src/config.template.js in app/src/config.js (edit it according to your needs)
$ cp app/src/config.template.js app/src/config.js

# Install dependencies
$ npm ci

# Start the server
$ npm start
```

Check if is correctly installed: [http://YOUR.DOMAIN.NAME:3000](http://YOUR.DOMAIN.NAME:3000)

---

## Using [PM2](https://pm2.keymetrics.io) (Process Manager)

![pm2](../images/pm2.png)

```bash
# Install pm2
$ npm ci -g pm2

# Start the server
$ pm2 start app/src/server.js --name mirotalkp2p

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

# Clone MiroTalk P2P repo
$ git clone https://github.com/miroslavpejic85/mirotalk.git

# Go to mirotalk dir
$ cd mirotalk

# Copy .env.template to .env and customize it according to your needs if needed
$ cp .env.template .env

# Copy app/src/config.template.js in app/src/config.js (edit it according to your needs)
$ cp app/src/config.template.js app/src/config.js

# Copy docker-compose.template.yml in docker-compose.yml (edit it according to your needs)
$ cp docker-compose.template.yml docker-compose.yml
```

Example of `docker-compose.yml`:

```yaml 
services:
    mirotalk:
        image: mirotalk/p2p:latest
        container_name: mirotalk
        hostname: mirotalk
        restart: unless-stopped
        ports:
            - '3000:3000'
        volumes:
            - .env:/src/.env:ro
            - ./app/:/src/app/:ro
            - ./public/:/src/public/:ro
```

```bash
# Pull the official Docker image
$ docker-compose pull

# Create and start containers (-d as daemon)
$ docker-compose up
```

Check if is correctly installed: [http://YOUR.DOMAIN.NAME:3000](http://YOUR.DOMAIN.NAME:3000)

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
    server_name YOUR.DOMAIN.NAME;

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
# MiroTalk P2P - HTTPS — proxy all requests to the Node app
server {
    # Enable HTTP/2
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name YOUR.DOMAIN.NAME;

    # Use the Let’s Encrypt certificates
    ssl_certificate /etc/letsencrypt/live/YOUR.DOMAIN.NAME/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/YOUR.DOMAIN.NAME/privkey.pem;

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_pass http://localhost:3000/;
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

Check Your MiroTalk P2P instance: [https://YOUR.DOMAIN.NAME](https://YOUR.DOMAIN.NAME)

---

## Apache Virtual Host (Alternative to Nginx)

![apache](../images/apache.png)

If you prefer `Apache`, configure it with the equivalent settings provided in this guide.

```bash
# Install apache with certbot
$ apt install python3-certbot-apache -y

# Setting up ssl
$ certbot --apache --non-interactive --agree-tos -d YOUR.DOMAIN.NAME -m your.email.address

# Edit the apache sites
$ sudo vim /etc/apache2/sites-enabled/YOUR.DOMAIN.NAME.conf
```

Add the following:

```bash
# HTTP — redirect all traffic to HTTPS
<VirtualHost *:80>
    ServerName YOUR.DOMAIN.NAME
    Redirect permanent / https://YOUR.DOMAIN.NAME
</VirtualHost>

# MiroTalk P2P - HTTPS — proxy all requests to the Node app
<VirtualHost *:443>
    ServerName YOUR.DOMAIN.NAME

    # SSL Configuration
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/YOUR.DOMAIN.NAME/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/YOUR.DOMAIN.NAME/privkey.pem
    Include /etc/letsencrypt/options-ssl-apache.conf

    # Enable HTTP/2 support
    Protocols h2 http/1.1

    <Location />
        # Proxy Configuration for Node.js App
        ProxyPass http://localhost:3000/
        ProxyPassReverse http://localhost:3000/

        ProxyPreserveHost On

        RequestHeader set X-Forwarded-For "%{REMOTE_ADDR}s"
        RequestHeader set X-Forwarded-Proto "https"
        RequestHeader set Host "%{HTTP_HOST}s"

        # Enable WebSocket proxy support for Socket.IO
        RewriteEngine On
        RewriteCond %{HTTP:Upgrade} =websocket [NC]
        RewriteRule /(.*) ws://localhost:3000/socket.io/$1 [P,L]
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

To keep your MiroTalk P2P instance up to date, create an update script:

```bash
cd
# Create a file p2pUpdate.sh
$ vim p2pUpdate.sh
```

---

For `PM2`:

```bash
#!/bin/bash

cd mirotalk
git pull
sudo npm ci
pm2 restart app/src/server.js
```

---

For `Docker`:

```bash
#!/bin/bash

cd mirotalk
git pull
docker-compose down
docker-compose pull
docker image prune -f
docker-compose up -d
```

---

Make the script executable

```bash
$ chmod +x p2pUpdate.sh
```

To update your MiroTalk P2P instance to the latest version, run the script:

```bash
./p2pUpdate.sh
```

---

## Changelogs

Stay informed about project updates by following the commits of the MiroTalk P2P project [here](https://github.com/miroslavpejic85/mirotalk/commits/master)

---
