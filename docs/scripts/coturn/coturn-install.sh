#!/bin/bash

set -euo pipefail

#---------------------------------------------
# MiroTalk COTURN Install Script
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

    MiroTalk COTURN Automated Install Script             
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

PROJECT_NAME="coturn"
PROJECT_DIR="/root/$PROJECT_NAME"
DOCKER_COMPOSE_VERSION="2.40.3"     # https://github.com/docker/compose/releases

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
    error "Some packages like nginx, docker, or nodejs are already installed. MiroTalk Coturn requires specific versions of these packages and will install them as part of its installation. Please start with a fresh Ubuntu install and run this script again."
fi

#---------------------------------------------
# Set variables
#---------------------------------------------

read -p $'\e[33m[READ] Enter your domain or sub.domain: \e[0m' DOMAIN
read -p $'\e[33m[READ] Enter your stun/turn username: \e[0m' USERNAME
read -p $'\e[33m[READ] Enter your stun/turn strong password: \e[0m' PASSWORD

#---------------------------------------------
# Check for empty variables
#---------------------------------------------

if [[ -z "$DOMAIN" || -z "$USERNAME" || -z "$PASSWORD" ]]; then
    error "All fields are required. Exiting..."
fi

#---------------------------------------------
# Set Server Public IPv4
#---------------------------------------------

SERVER_IP=$(wget -qO- http://api.ipify.org)

if [[ -z "$SERVER_IP" ]]; then
    read -p $'\e[33m[READ] Enter your SERVER public IP: \e[0m' SERVER_IP
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
    info "Domain $DOMAIN points to this server."
else
    error "Domain $DOMAIN does NOT point to this server (expected $SERVER_IP, got $DOMAIN_IP)."
fi

#---------------------------------------------
# Create Coturn directory
#---------------------------------------------

info "Create coturn dir"
mkdir $PROJECT_DIR
cd $PROJECT_DIR

#---------------------------------------------
# Customize turnserver config
#---------------------------------------------

cat > $PROJECT_DIR/turnserver.conf <<EOF
listening-port=3478
tls-listening-port=5349

min-port=10000
max-port=20000

fingerprint
lt-cred-mech

user=$USERNAME:$PASSWORD

server-name=$DOMAIN
realm=$DOMAIN

total-quota=500
stale-nonce=600

cert=/etc/letsencrypt/live/$DOMAIN/fullchain.pem
pkey=/etc/letsencrypt/live/$DOMAIN/privkey.pem

cipher-list="ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384"

no-loopback-peers
no-multicast-peers

simple-log
EOF

info "turnserver.conf generated successfully."

#---------------------------------------------
# Customize docker-compose.yml network and volumes
#---------------------------------------------

cat > $PROJECT_DIR/docker-compose.yml <<EOF
services:
    $PROJECT_NAME:
        image: coturn/coturn
        container_name: $PROJECT_NAME
        hostname: $PROJECT_NAME
        network_mode: "host"
        user: "root"
        restart: unless-stopped
        volumes:
            - $PROJECT_DIR/turnserver.conf:/etc/coturn/turnserver.conf
            - /etc/letsencrypt/live/$DOMAIN/fullchain.pem:/etc/letsencrypt/live/$DOMAIN/fullchain.pem
            - /etc/letsencrypt/live/$DOMAIN/privkey.pem:/etc/letsencrypt/live/$DOMAIN/privkey.pem
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

info "Configuring Nginx for MiroTalk Coturn..."
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

nginx -t
systemctl restart nginx

#---------------------------------------------
# Setup SSL auto-renew
#---------------------------------------------

info "Setting up SSL auto-renewal..."
certbot renew --dry-run --cert-name $DOMAIN

info "MiroTalk Coturn installation complete!"
echo "Check: \e[32mhttps://p2p.mirotalk.com/icetest?iceServers=[{\"urls\":"\stun:$DOMAIN:3478\"},{\"urls\":\"turn:$DOMAIN:3478\",\"username\":"\$USERNAME\",\"credential\":\"$PASSWORD\"}]\e[0m"