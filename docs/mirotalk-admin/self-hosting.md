# MiroTalk Admin Self-Hosting Guide

![mirotalk-admin](../images/mirotalk/adm.png)

## Description

MiroTalk ADMIN is a management panel for monitoring, updating, and maintaining MiroTalk instances. It provides tools for user oversight, system updates, and secure deployments.

## Requirements

- Server Selection:
    - [Hetzner](https://www.hetzner.com/cloud) - Use [this link](https://hetzner.cloud/?ref=XdRifCzCK3bn) to receive `€⁠20 in cloud credits`
    - [Netcup](https://www.netcup.com/en/?ref=309627)
    - [Hostinger](https://hostinger.com/?REFERRALCODE=MIROTALK)
    - [Contabo](https://www.dpbolvw.net/click-101027391-14462707)
- OS: Ubuntu 22.04 LTS.
- [Node.js](https://nodejs.org/en/) (LTS) and npm
- Domain or Subdomain Name (e.g., `YOUR.DOMAIN.NAME`) with a DNS A record pointing to your server's IPv4 address.

---

## Installation

![nodejs](../images/nodejs.png)

Install `NodeJS` and `npm` using [Node Version Manager](../utility/nvm.md)

---

## Quick start

```bash
# Clone the repository
git clone https://github.com/miroslavpejic85/mirotalk-admin.git

# Navigate to the project directory
cd mirotalk-admin

# Copy and customize the config template
cp backend/config/index.template.js backend/config/index.js

# Copy and customize the environment template
cp .env.template .env
```

!!! warning
    **Before starting the service, make sure to:** Set `ADMIN_DASHBOARD_ENABLED=true` in your `.env` file. Update admin credentials, JWT secret and SSH configuration with secure, custom values. Specify the correct absolute paths for your MiroTalk directories.

```bash
# Install dependencies
npm ci

# Start the server
npm start
```

Verify the installation: [http://YOUR.DOMAIN.NAME:9999/admin](http://YOUR.DOMAIN.NAME:9999/admin)

---

## Using [PM2](https://pm2.keymetrics.io) (Process Manager)

![pm2](../images/pm2.png)

```bash
# Install PM2
npm install -g pm2

# Start the server
pm2 start backend/server.js --name mirotalk-admin

# Save the process list
pm2 save

# Enable auto-start on boot
pm2 startup
```

---

## Using Docker

![docker](../images/docker.png)

```bash
# Install Docker and Docker Compose
sudo apt install -y docker.io
sudo apt install -y docker-compose

# Clone the repository
git clone https://github.com/miroslavpejic85/mirotalk-admin.git

# Navigate to the project directory
cd mirotalk-admin

# Copy and customize the config template
cp backend/config/index.template.js backend/config/index.js

# Copy and customize the environment template
cp .env.template .env
```

!!! warning
    **Before starting the service, make sure to:** Set `ADMIN_DASHBOARD_ENABLED=true` in your `.env` file. Update admin credentials, JWT secret and SSH configuration with secure, custom values. Specify the correct absolute paths for your MiroTalk directories.

```bash
# Copy and customize the Docker Compose template
cp docker-compose.template.yml docker-compose.yml
```

Example of `docker-compose.yml`:

```yaml 
services:
    mirotalkadmin:
        image: mirotalk/admin:latest
        container_name: mirotalkadmin
        hostname: mirotalkadmin
        restart: unless-stopped
        ports:
            - '${ADMIN_PORT}:${ADMIN_PORT}'
        volumes:
            - ./frontend:/app/frontend:ro
            - ./backend:/app/backend:ro
            - ./.env:/app/.env:ro
```

```bash
# Pull the official Docker image
docker-compose pull

# Create and start containers (add -d to run in background)
docker-compose up
```

Verify the installation: [http://YOUR.DOMAIN.NAME:9999/admin](http://YOUR.DOMAIN.NAME:9999/admin)

---


## Configuring Nginx & Certbot

![nginx](../images/nginx.png)

To use MiroTalk Admin without the port number and with encrypted communications (required for proper functionality), install [Nginx](https://www.nginx.com) and [Certbot](https://certbot.eff.org):

```bash
# Install Nginx
sudo apt-get install -y nginx

# Install Certbot (SSL certificates)
sudo apt install -y snapd
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# Configure Nginx
sudo vim /etc/nginx/sites-enabled/default
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
sudo nginx -t

# Enable HTTPS with Certbot (follow the prompts)
sudo certbot certonly --nginx

# Add Let's Encrypt configuration to Nginx
sudo vim /etc/nginx/sites-enabled/default
```

Add the following:

```bash
# MiroTalk Admin - HTTPS — proxy all requests to the Node app
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
        proxy_pass http://localhost:9999/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

```bash
# Test Nginx configuration again
sudo nginx -t

# Restart Nginx
service nginx restart
service nginx status

# Set up auto-renewal for SSL certificates
sudo certbot renew --dry-run --cert-name YOUR.DOMAIN.NAME

# Show certificates
sudo certbot certificates
```

Verify your MiroTalk Admin instance: [https://YOUR.DOMAIN.NAME](https://YOUR.DOMAIN.NAME)

---

## Apache Virtual Host (Alternative to Nginx)

![apache](../images/apache.png)

If you prefer `Apache`, configure it with the equivalent settings provided in this guide.

```bash
# Install apache with certbot
apt install python3-certbot-apache -y

# Setting up ssl
certbot --apache --non-interactive --agree-tos -d YOUR.DOMAIN.NAME -m your.email.address

# Edit the apache sites
sudo vim /etc/apache2/sites-enabled/YOUR.DOMAIN.NAME.conf
```

Add the following:

```bash
# HTTP — redirect all traffic to HTTPS
<VirtualHost *:80>
    ServerName YOUR.DOMAIN.NAME
    Redirect permanent / https://YOUR.DOMAIN.NAME
</VirtualHost>

# MiroTalk Admin - HTTPS — proxy all requests to the Node app
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
        ProxyPass http://localhost:9999/
        ProxyPassReverse http://localhost:9999/

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

To keep your MiroTalk Admin instance up to date, create an update script:

```bash
cd
# Create a file adminUpdate.sh
vim adminUpdate.sh
```

---

For `PM2`:

```bash
#!/bin/bash

cd mirotalk-admin
git pull
sudo npm ci
pm2 restart mirotalk-admin
```

---

For `Docker`:

```bash
#!/bin/bash

cd mirotalk-admin
git pull
docker-compose down
docker-compose pull
docker image prune -f
docker-compose up -d
```

---

Make the script executable:

```bash
chmod +x adminUpdate.sh
```

To update your MiroTalk Admin instance to the latest version, run the script:

```bash
./adminUpdate.sh
```

---

## Changelogs

Stay informed about project updates by following the commits of the MiroTalk Admin project [here](https://github.com/miroslavpejic85/mirotalk-admin/commits/main/).

---
