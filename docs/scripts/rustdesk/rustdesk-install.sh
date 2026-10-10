#!/bin/bash

set -euo pipefail

#---------------------------------------------
# RustDesk Install Script
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

    RustDesk Automated Install Script             
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

PROJECT_DIR="/root/rustdesk"
COMPOSE_FILE="compose.yml"
KEY_FILE="$PROJECT_DIR/data/id_ed25519.pub"
DOCKER_COMPOSE_VERSION="5.0.1"     # https://github.com/docker/compose/releases

#---------------------------------------------
# Check Root
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
# Set variables
#---------------------------------------------

read -p $'⚠️ \e[33m[READ] Enter the RustDesk edition [oss/pro] (default: oss, pro requires a license): \e[0m' EDITION

EDITION=${EDITION:-oss}
if [[ "$EDITION" != "oss" && "$EDITION" != "pro" ]]; then
    error "Invalid edition '$EDITION'. Use 'oss' or 'pro'."
fi

#---------------------------------------------
# Set Server Public IPv4
#---------------------------------------------

SERVER_IP=$(wget -qO- http://api.ipify.org || true)

if [[ -z "$SERVER_IP" ]]; then
    read -p $'⚠️ \e[33m[READ] Enter your SERVER public IP: \e[0m' SERVER_IP
fi

if [[ -z "$SERVER_IP" ]]; then
    error "SERVER public IP is required. Exiting..."
fi

info "Server Public IP $SERVER_IP"

#---------------------------------------------
# Install Docker and Docker Compose
#---------------------------------------------

info "Installing Docker and Docker Compose..."
apt-get update
apt-get install -y docker.io wget
if ! command -v docker-compose >/dev/null; then
    wget https://github.com/docker/compose/releases/download/v$DOCKER_COMPOSE_VERSION/docker-compose-linux-x86_64 -O /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
fi
info "Docker Compose version: $(docker-compose --version)"

#---------------------------------------------
# Download compose file
#---------------------------------------------

if [ -f "$PROJECT_DIR/$COMPOSE_FILE" ]; then
    error "$PROJECT_DIR/$COMPOSE_FILE already exists. Use the update script, or uninstall first."
fi

info "Downloading RustDesk $EDITION compose file..."
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"
wget "https://rustdesk.com/$EDITION.yml" -O "$COMPOSE_FILE"

#---------------------------------------------
# Open firewall ports (only if ufw is active)
#---------------------------------------------

if command -v ufw >/dev/null && ufw status | grep -q "Status: active"; then
    info "Opening RustDesk firewall ports..."
    ufw allow 21115:21119/tcp
    ufw allow 21116/udp
    if [[ "$EDITION" == "pro" ]]; then
        ufw allow 21114/tcp
    fi
else
    warning "ufw is not active. Make sure ports 21115-21119/tcp and 21116/udp are open (21114/tcp for pro)."
fi

#---------------------------------------------
# Start RustDesk server
#---------------------------------------------

info "Starting RustDesk server..."
docker-compose -f "$COMPOSE_FILE" pull
docker-compose -f "$COMPOSE_FILE" up -d
docker-compose -f "$COMPOSE_FILE" ps

#---------------------------------------------
# Get the public key
#---------------------------------------------

info "Waiting for the public key..."
for _ in $(seq 1 30); do
    [ -s "$KEY_FILE" ] && break
    sleep 2
done

if [ ! -s "$KEY_FILE" ]; then
    warning "Public key not found yet. Check: docker-compose -f $PROJECT_DIR/$COMPOSE_FILE logs hbbs"
    KEY="(not available)"
else
    KEY=$(cat "$KEY_FILE")
fi

info "RustDesk installation complete!"
echo -e "ID Server:    \e[32m$SERVER_IP\e[0m (or your DNS name)"
echo -e "Relay Server: \e[32m$SERVER_IP\e[0m (or leave empty)"
echo -e "Key:          \e[32m$KEY\e[0m"
echo -e "Configure every RustDesk client: Settings -> Network -> ID/Relay Server"
echo -e "Keep $PROJECT_DIR/data, deleting it changes the key and breaks all configured clients."
