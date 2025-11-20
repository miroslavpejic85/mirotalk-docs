#!/bin/bash

set -euo pipefail

#---------------------------------------------
# MiroTalk BRO Install Script (Root)
#---------------------------------------------

echo -e "\e[32m"
cat <<'EOF'
$$\      $$\ $$\                  $$$$$$$$\        $$\ $$\       
$$$\    $$$ |\__|                 \__$$  __|       $$ |$$ |      
$$$$\  $$$$ |$$\  $$$$$$\   $$$$$$\  $$ | $$$$$$\  $$ |$$ |  $$\ 
$$\$$\$$ $$ |$$ |$$  __$$\ $$  __$$\ $$ | \____$$\ $$ |$$ | $$  |
$$ \$$$  $$ |$$ |$$ |  \__|$$ /  $$ |$$ | $$$$$$$ |$$ |$$$$$$  / 
$$ |\$  /$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ |$$ |$$  _$$<  
$$ | \_/ $$ |$$ |$$ |      \$$$$$$  |$$ |\$$$$$$$ |$$ |$$ | \$$\ 
\__|     \__|\__|\__|       \______/ \__| \_______|\__|\__|  \__|

      MiroTalk BRO Automated Install Script             
        Tested: Ubuntu 22.04 | 24.04 LTS               
            (c) 2025 Miroslav Pejic                  
EOF
echo -e "\e[0m"

#---------------------------------------------
# Logging
#---------------------------------------------

info()    { echo -e "✅ \e[32m[INFO]\e[0m $*"; }
warning() { echo -e "⚠️ \e[33m[WARNING]\e[0m $*"; }
error()   { echo -e "❌ \e[31m[ERROR]\e[0m $*"; exit 1; }

#---------------------------------------------
# Variables
#---------------------------------------------

SERVER_PORT=3016
PROJECT_NAME="mirotalkbro"
PROJECT_DIR="/root/$PROJECT_NAME"
DOCKER_COMPOSE_VERSION="2.40.3"     # https://github.com/docker/compose/releases
NODE_VERSION="22.21.1"              # https://nodejs.org/en/download/releases/
NVM_VERSION="0.40.3"                # https://github.com/nvm-sh/nvm/releases

export NVM_DIR="/root/.nvm"

#---------------------------------------------
# Check RooT
#---------------------------------------------

if [[ ${EUID} -ne 0 ]]; then
    error "This script should be run as root." > /dev/stderr
fi

#---------------------------------------------
# Check OS
#---------------------------------------------

OS=$(lsb_release -si)
VERSION=$(lsb_release -sr)

if [[ "$OS" != "Ubuntu" ]] || [[ "$VERSION" != "22.04" && "$VERSION" != "24.04" ]]; then
    error "This script only supports Ubuntu 22.04 or 24.04 LTS"
fi

#---------------------------------------------
# Check CPU, RAM, Disk
#---------------------------------------------

CPU=$(nproc)
RAM=$(free -m | awk '/Mem:/ {print $2}')
DISK=$(df / | tail -1 | awk '{print $4}')
ARCH=$(uname -m)

if [[ $CPU -lt 2 || $RAM -lt 2048 || $DISK -lt 20000000 || "$ARCH" != "x86_64" ]]; then
    error "Server does not meet requirements:
        - CPU cores >= 2 (found $CPU)
        - RAM >= 2GB (found ${RAM}MB)
        - Disk >= 20GB (found ${DISK}KB)
        - Architecture x86_64 / amd64 (found $ARCH)"
fi

info "System requirements OK: CPU=$CPU, RAM=${RAM}MB, Disk=${DISK}KB, Arch=$ARCH"

#---------------------------------------------
# Ensure no Apache, Nginx, Docker, or Node.js is installed
#---------------------------------------------

if command -v nginx >/dev/null || command -v docker >/dev/null || command -v node >/dev/null; then
    error "Some packages like nginx, docker, or nodejs are already installed. MiroTalk requires specific versions of these packages and will install them as part of its installation. Please start with a fresh Ubuntu install and run this script again."
fi

#---------------------------------------------
# Set domain or subdomain
#---------------------------------------------

read -p $'⚠️ \e[33m[READ] Enter your domain or sub.domain: \e[0m' DOMAIN

if [[ -z "$DOMAIN" ]]; then
    error "All fields are required. Exiting..."
fi

#---------------------------------------------
# Set Server Public IPv4
#---------------------------------------------

SERVER_IP=$(wget -qO- http://api.ipify.org)

if [[ -z "$SERVER_IP" ]]; then
    read -p $'⚠️ \e[33m[READ] Enter your SERVER public IP: \e[0m' SERVER_IP
fi

if [[ -z "$SERVER_IP" ]]; then
    error "SERVER public IP is required. Exiting..."
fi

info "Server Public IP $SERVER_IP"

#---------------------------------------------
# Resolve domain to IP
#---------------------------------------------

apt update
apt install -y dnsutils

DOMAIN_IP=$(dig +short "$DOMAIN" | tail -n1)

if [[ -z "$DOMAIN_IP" ]]; then
    error "Could not resolve $DOMAIN. Check DNS settings."
fi

info "Domain resolves to: $DOMAIN_IP"

#---------------------------------------------
# Compare domain IP to server IP
#---------------------------------------------

if [[ "$DOMAIN_IP" == "$SERVER_IP" ]]; then
    info "Domain $DOMAIN points correctly to this server."
else
    error "Domain $DOMAIN does NOT point to this server (expected $SERVER_IP, got $DOMAIN_IP)."
fi

#---------------------------------------------
# Install NVM and Node.js 22 LTS
#---------------------------------------------

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v$NVM_VERSION/install.sh | bash
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
nvm install "$NODE_VERSION"
nvm use "$NODE_VERSION"
nvm alias default "$NODE_VERSION"
info "Node.js version $(node -v) installed successfully"

##---------------------------------------------
# Clone MiroTalk BRO repo
#---------------------------------------------

info "Cloning MiroTalk BRO repository..."
git clone https://github.com/miroslavpejic85/mirotalkbro.git $PROJECT_DIR
cd $PROJECT_DIR

#---------------------------------------------
# Copy config files
#---------------------------------------------

info "Setting up configuration files..."
cp .env.template .env

#---------------------------------------------
# Set environment
#---------------------------------------------

sed -i "s|NODE_ENV=.*|NODE_ENV=production|" .env
sed -i "s|PORT=.*|PORT=$SERVER_PORT|" .env

#---------------------------------------------
# Customize docker-compose.yml network and volumes
#---------------------------------------------

cat > $PROJECT_DIR/docker-compose.yml <<EOF
services:
    $PROJECT_NAME:
        image: mirotalk/bro:latest
        container_name: $PROJECT_NAME
        hostname: $PROJECT_NAME
        restart: unless-stopped
        ports:
            - '${SERVER_PORT}:${SERVER_PORT}'
        volumes:
            - $PROJECT_DIR/.env:/src/.env:ro
            - $PROJECT_DIR/app/:/src/app/:ro
            - $PROJECT_DIR/public/:/src/public/:ro
EOF

info "docker-compose.yml generated successfully."

#---------------------------------------------
# Install Docker and Docker Compose
#---------------------------------------------

info "Installing Docker and Docker Compose..."
apt-get install -y docker.io
wget https://github.com/docker/compose/releases/download/v$DOCKER_COMPOSE_VERSION/docker-compose-linux-x86_64 -O /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
info "Docker Compose version: $(docker-compose --version)"

#---------------------------------------------
# Pull Docker image and start containers
#---------------------------------------------

info "Pulling Docker images..."
docker-compose pull
info "Starting containers..."
docker-compose up -d

#---------------------------------------------
# Install Nginx and Certbot
#---------------------------------------------

info "Installing Nginx and Certbot..."
apt-get install -y nginx snapd
snap install core; snap refresh core
snap install --classic certbot
# Only create symlink if it doesn't exist
if [ ! -f /usr/bin/certbot ]; then
    ln -s /snap/bin/certbot /usr/bin/certbot
fi

#---------------------------------------------
# Setup HTTP->HTTPS redirect
#---------------------------------------------

info "Configuring Nginx for MiroTalk P2P..."
cat > /etc/nginx/sites-available/$PROJECT_NAME <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN;
    return 301 https://\$host\$request_uri;
}
EOF
ln -sf /etc/nginx/sites-available/$PROJECT_NAME /etc/nginx/sites-enabled/$PROJECT_NAME
nginx -t
systemctl restart nginx

#---------------------------------------------
# Generate SSL certificate
#---------------------------------------------

info "Generating SSL certificate with Certbot..."
certbot certonly --nginx -d $DOMAIN --non-interactive --agree-tos -m admin@$DOMAIN

#---------------------------------------------
# Configure Nginx for HTTPS proxy
#---------------------------------------------

cat > /etc/nginx/sites-available/$PROJECT_NAME <<EOF
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name $DOMAIN;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;

    location / {
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header Host \$host;
        proxy_pass http://localhost:$SERVER_PORT/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
EOF

nginx -t
systemctl restart nginx

#---------------------------------------------
# Setup SSL auto-renew
#---------------------------------------------

info "Setting up SSL auto-renewal..."
certbot renew --dry-run --cert-name $DOMAIN

info "MiroTalk BRO installation complete!"
info "Access your instance at \e[32mhttps://$DOMAIN\e[0m"
