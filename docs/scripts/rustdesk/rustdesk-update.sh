#!/bin/bash

set -euo pipefail

#---------------------------------------------
# RustDesk Update Script
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

    RustDesk Automated Update Script             
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
# Update RustDesk
#---------------------------------------------

cd "$PROJECT_DIR" || error "Project directory not found!"

if [ ! -f "$COMPOSE_FILE" ]; then
    error "$PROJECT_DIR/$COMPOSE_FILE not found!"
fi

info "Updating RustDesk server..."

# The ./data volume (keys) is preserved
docker-compose -f "$COMPOSE_FILE" pull
docker-compose -f "$COMPOSE_FILE" up -d --force-recreate
docker image prune -f
docker-compose -f "$COMPOSE_FILE" ps

info "RustDesk update complete!"

if [ -s "$KEY_FILE" ]; then
    echo -e "Key: \e[32m$(cat "$KEY_FILE")\e[0m"
fi
