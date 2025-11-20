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
docker-compose down
docker-compose pull
docker image prune -f
docker-compose up -d
