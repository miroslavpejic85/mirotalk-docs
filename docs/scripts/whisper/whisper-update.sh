#!/bin/bash

set -euo pipefail

#---------------------------------------------
# Logging
#---------------------------------------------

info()    { echo -e "✅ \e[32m[INFO]\e[0m $*"; }
warning() { echo -e "⚠️ \e[33m[WARNING]\e[0m $*"; }
error()   { echo -e "❌ \e[31m[ERROR]\e[0m $*"; exit 1; }

#---------------------------------------------
# Update MiroTalk Whisper
#---------------------------------------------

PROJECT_DIR="/root/whisper"
COMPOSE_FILE="docker-compose-whisper.yml"

cd "$PROJECT_DIR" || error "Project directory not found!"

# Detect the profile (cpu/gpu) from the compose file
if grep -q "profiles: \['gpu'\]" "$COMPOSE_FILE"; then
    PROFILE="gpu"
else
    PROFILE="cpu"
fi

info "Updating MiroTalk Whisper (profile: $PROFILE)..."

docker-compose -f "$COMPOSE_FILE" --profile "$PROFILE" down
docker-compose -f "$COMPOSE_FILE" --profile "$PROFILE" pull
docker image prune -f
docker-compose -f "$COMPOSE_FILE" --profile "$PROFILE" up -d --force-recreate

info "MiroTalk Whisper update complete!"
