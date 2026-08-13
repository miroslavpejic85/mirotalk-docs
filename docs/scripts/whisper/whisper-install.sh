#!/bin/bash

set -euo pipefail

#---------------------------------------------
# MiroTalk Whisper Install Script
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

    MiroTalk Whisper Automated Install Script             
        Tested: Ubuntu 22.04 | 24.04 LTS               
            (c) 2026 Miroslav Pejic                  
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

PROJECT_NAME="whisper"
PROJECT_DIR="/root/$PROJECT_NAME"
CONTAINER_NAME="mirotalkwhisper"
COMPOSE_FILE="docker-compose-whisper.yml"
DOCKER_COMPOSE_VERSION="5.0.1"     # https://github.com/docker/compose/releases

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
    warning "Some packages like nginx, docker, or nodejs are already installed. MiroTalk Whisper requires specific versions of these packages and will install them as part of its installation. Please start with a fresh Ubuntu install and run this script again."
fi

#---------------------------------------------
# Set variables
#---------------------------------------------

read -p $'⚠️ \e[33m[READ] Enter your domain or sub.domain: \e[0m' DOMAIN
read -p $'⚠️ \e[33m[READ] Enter your Whisper API key (leave empty for NO AUTH — endpoint will be PUBLIC): \e[0m' WHISPER_API_KEY
read -p $'⚠️ \e[33m[READ] Enter the inference device [cpu/gpu] (default: cpu): \e[0m' PROFILE
read -p $'⚠️ \e[33m[READ] Enter the Whisper model [tiny|base|small|medium|large-v3] (default: small): \e[0m' MODEL_SIZE

#---------------------------------------------
# Check for empty variables
#---------------------------------------------

if [[ -z "$DOMAIN" ]]; then
    error "Domain is required. Exiting..."
fi

PROFILE=${PROFILE:-cpu}
if [[ "$PROFILE" != "cpu" && "$PROFILE" != "gpu" ]]; then
    error "Invalid inference device '$PROFILE'. Use 'cpu' or 'gpu'."
fi

MODEL_SIZE=${MODEL_SIZE:-small}
WHISPER_MODEL="Systran/faster-whisper-$MODEL_SIZE"

if [[ "$PROFILE" == "cpu" ]]; then
    WHISPER_IMAGE="ghcr.io/speaches-ai/speaches:latest-cpu"
    WHISPER_DEVICE="cpu"
else
    WHISPER_IMAGE="ghcr.io/speaches-ai/speaches:latest-cuda"
    WHISPER_DEVICE="cuda"
fi

WHISPER_PORT=8000

info "Using image: $WHISPER_IMAGE (device: $WHISPER_DEVICE, model: $WHISPER_MODEL)"

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
    info "Domain $DOMAIN points to this server."
else
    error "Domain $DOMAIN does NOT point to this server (expected $SERVER_IP, got $DOMAIN_IP)."
fi

#---------------------------------------------
# Create Whisper directory
#---------------------------------------------

info "Create whisper dir"
mkdir -p $PROJECT_DIR
cd $PROJECT_DIR

#---------------------------------------------
# Generate .env
#---------------------------------------------

cat > $PROJECT_DIR/.env <<EOF
WHISPER_PORT=$WHISPER_PORT
WHISPER_MODEL=$WHISPER_MODEL
WHISPER_API_KEY=$WHISPER_API_KEY
EOF

info ".env generated successfully."

#---------------------------------------------
# Generate docker-compose-whisper.yml
#---------------------------------------------

if [[ "$PROFILE" == "cpu" ]]; then
    cat > $PROJECT_DIR/$COMPOSE_FILE <<EOF
services:
    whisper:
        image: $WHISPER_IMAGE
        container_name: $CONTAINER_NAME
        hostname: whisper
        restart: unless-stopped
        profiles: ['cpu']
        ports:
            - '\${WHISPER_PORT:-8000}:8000'
        environment:
            PRELOAD_MODELS: '["\${WHISPER_MODEL:-Systran/faster-whisper-small}"]'
            WHISPER__INFERENCE_DEVICE: 'cpu'
            API_KEY: '\${WHISPER_API_KEY:-}'
        volumes:
            - speaches_cache:/home/ubuntu/.cache/huggingface/hub

volumes:
    speaches_cache:
EOF
else
    cat > $PROJECT_DIR/$COMPOSE_FILE <<EOF
services:
    whisper-gpu:
        image: $WHISPER_IMAGE
        container_name: $CONTAINER_NAME
        hostname: whisper
        restart: unless-stopped
        profiles: ['gpu']
        ports:
            - '\${WHISPER_PORT:-8000}:8000'
        environment:
            PRELOAD_MODELS: '["\${WHISPER_MODEL:-Systran/faster-whisper-medium}"]'
            WHISPER__INFERENCE_DEVICE: 'cuda'
            API_KEY: '\${WHISPER_API_KEY:-}'
        volumes:
            - speaches_cache:/home/ubuntu/.cache/huggingface/hub
        deploy:
            resources:
                reservations:
                    devices:
                        - driver: nvidia
                          count: all
                          capabilities: [gpu]

volumes:
    speaches_cache:
EOF
fi

info "$COMPOSE_FILE generated successfully."

#---------------------------------------------
# Install Docker and Docker Compose
#---------------------------------------------

info "Installing Docker and Docker Compose..."
apt-get install -y docker.io
wget https://github.com/docker/compose/releases/download/v$DOCKER_COMPOSE_VERSION/docker-compose-linux-x86_64 -O /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
info "Docker Compose version: $(docker-compose --version)"

#---------------------------------------------
# Pull Docker image and start container
#---------------------------------------------

info "Pulling Docker images..."
docker-compose -f $COMPOSE_FILE --profile $PROFILE pull
info "Starting containers..."
docker-compose -f $COMPOSE_FILE --profile $PROFILE up -d --force-recreate

#---------------------------------------------
# Download model and verify auth
#---------------------------------------------

info "Downloading Whisper model $WHISPER_MODEL (this may take a while)..."
sleep 10
curl -s -o /dev/null -w "download HTTP %{http_code}\n" \
    -X POST "http://localhost:$WHISPER_PORT/v1/models/$WHISPER_MODEL" \
    -H "Authorization: Bearer $WHISPER_API_KEY"

info "Verifying API-key authentication..."
curl -s -o /dev/null -w "valid key %{http_code}\n" "http://localhost:$WHISPER_PORT/v1/models" -H "Authorization: Bearer $WHISPER_API_KEY"
curl -s -o /dev/null -w "wrong key %{http_code}\n" "http://localhost:$WHISPER_PORT/v1/models" -H "Authorization: Bearer wrong"

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

info "Configuring Nginx for MiroTalk Whisper..."
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
# Setup HTTPS reverse proxy
#---------------------------------------------

info "Configuring Nginx HTTPS reverse proxy..."
cat > /etc/nginx/sites-available/$PROJECT_NAME <<EOF
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN;
    return 301 https://\$host\$request_uri;
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name $DOMAIN;

    ssl_certificate /etc/letsencrypt/live/$DOMAIN/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$DOMAIN/privkey.pem;

    location / {
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header Host \$host;
        proxy_pass http://localhost:$WHISPER_PORT/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_buffer_size       128k;
        proxy_buffers         8 256k;
        proxy_busy_buffers_size 512k;
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

info "MiroTalk Whisper installation complete!"
echo -e "Check: \e[32mhttps://$DOMAIN\e[0m"
