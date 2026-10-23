#!/bin/bash

set -euo pipefail

#---------------------------------------------
# Logging
#---------------------------------------------

info()    { echo -e "✅ \e[32m[INFO]\e[0m $*"; }
warning() { echo -e "⚠️ \e[33m[WARNING]\e[0m $*"; }
error()   { echo -e "❌ \e[31m[ERROR]\e[0m $*"; exit 1; }

#---------------------------------------------
# Update MiroTalk
#---------------------------------------------

PROJECT_DIR="/root/mirotalkc2c"

cd "$PROJECT_DIR" || error "Project directory not found!"

git pull

# Create the user-editable UI config if missing (introduced in v1.4.83)
if [[ ! -f frontend/js/config.js ]]; then
    info "Creating frontend/js/config.js from template..."
    cp frontend/js/config.template.js frontend/js/config.js
fi

docker-compose down
docker-compose pull
docker image prune -f
docker-compose up -d
