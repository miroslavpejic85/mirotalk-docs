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

PROJECT_DIR="/root/mirotalkbro"

cd "$PROJECT_DIR" || error "Project directory not found!"

git pull

# Create the user-editable UI config if missing (introduced in v1.4.69)
if [[ ! -f public/js/config.js ]]; then
    info "Creating public/js/config.js from template..."
    cp public/js/config.template.js public/js/config.js
fi

docker-compose down
docker-compose pull
docker image prune -f
docker-compose up -d
