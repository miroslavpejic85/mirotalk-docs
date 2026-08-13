#!/bin/bash

set -euo pipefail

#---------------------------------------------
# MiroTalk Whisper Uninstall Script
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

    MiroTalk Whisper Automated Uninstall Script             
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
SITES_AVAILABLE="/etc/nginx/sites-available/$PROJECT_NAME"
SITES_ENABLED="/etc/nginx/sites-enabled/$PROJECT_NAME"

#---------------------------------------------
# Set variables
#---------------------------------------------

read -p $'⚠️ \e[33m[READ] Remove SSL certificates for the domain: \e[0m' DOMAIN

#---------------------------------------------
# Check for empty variables
#---------------------------------------------

if [[ -z "$DOMAIN" ]]; then
    error "All fields are required. Exiting..."
fi

#---------------------------------------------
# Stop and remove MiroTalk Docker container
#---------------------------------------------

if [ -f "$PROJECT_DIR/$COMPOSE_FILE" ]; then
    info "Stopping and removing MiroTalk Whisper containers and volumes..."
    (cd "$PROJECT_DIR" && docker-compose -f "$COMPOSE_FILE" --profile cpu --profile gpu down -v) || true
fi

if docker ps -a | grep -q $CONTAINER_NAME; then
    info "Stopping MiroTalk container..."
    docker stop $CONTAINER_NAME || true
    info "Removing MiroTalk container..."
    docker rm $CONTAINER_NAME || true
fi

#---------------------------------------------
# Remove docker-compose directory
#---------------------------------------------

if [ -d "$PROJECT_DIR" ]; then
    info "Removing $PROJECT_DIR folder..."
    rm -rf "$PROJECT_DIR"
fi

#---------------------------------------------
# Remove Nginx site config
#---------------------------------------------

if [ -f "$SITES_AVAILABLE" ]; then
    info "Removing Nginx site configuration..."
    rm -f "$SITES_AVAILABLE"
fi

if [ -f "$SITES_ENABLED" ]; then
    info "Removing Nginx enabled site..."
    rm -f "$SITES_ENABLED"
fi

#---------------------------------------------
# Remove SSL certificates for the domain
#---------------------------------------------

if [ -n "$DOMAIN" ] && [ -d "/etc/letsencrypt/live/$DOMAIN" ]; then
    info "Removing Let's Encrypt SSL certificates for $DOMAIN..."
    certbot delete --cert-name "$DOMAIN" --non-interactive
fi

#---------------------------------------------
# Reload Nginx
#---------------------------------------------

info "Reloading Nginx..."
nginx -t && systemctl reload nginx

info "Rollback complete!"
