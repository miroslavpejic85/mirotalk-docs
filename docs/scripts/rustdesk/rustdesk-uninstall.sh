#!/bin/bash

set -euo pipefail

#---------------------------------------------
# RustDesk Uninstall Script
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

    RustDesk Automated Uninstall Script             
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

#---------------------------------------------
# Check Root
#---------------------------------------------

if [[ ${EUID} -ne 0 ]]; then
    error "This script should be run as root." > /dev/stderr
fi

#---------------------------------------------
# Set variables
#---------------------------------------------

read -p $'⚠️ \e[33m[READ] Delete the data folder with the keys? Clients must be reconfigured if you reinstall [y/N]: \e[0m' REMOVE_DATA

#---------------------------------------------
# Stop and remove RustDesk containers
#---------------------------------------------

if [ -f "$PROJECT_DIR/$COMPOSE_FILE" ]; then
    info "Stopping and removing RustDesk containers..."
    (cd "$PROJECT_DIR" && docker-compose -f "$COMPOSE_FILE" down) || true
fi

for CONTAINER in hbbs hbbr; do
    if docker ps -a --format '{{.Names}}' | grep -qx "$CONTAINER"; then
        info "Removing container $CONTAINER..."
        docker rm -f "$CONTAINER" || true
    fi
done

#---------------------------------------------
# Remove project files
#---------------------------------------------

if [ -d "$PROJECT_DIR" ]; then
    if [[ "${REMOVE_DATA:-N}" =~ ^[Yy]$ ]]; then
        info "Removing $PROJECT_DIR folder (including keys)..."
        rm -rf "$PROJECT_DIR"
    else
        info "Keeping $PROJECT_DIR/data, removing the compose file only..."
        rm -f "$PROJECT_DIR/$COMPOSE_FILE"
    fi
fi

#---------------------------------------------
# Remove firewall rules (only if ufw is active)
#---------------------------------------------

if command -v ufw >/dev/null && ufw status | grep -q "Status: active"; then
    info "Removing RustDesk firewall rules..."
    ufw delete allow 21115:21119/tcp || true
    ufw delete allow 21116/udp || true
    ufw delete allow 21114/tcp || true
fi

info "RustDesk uninstall complete!"
