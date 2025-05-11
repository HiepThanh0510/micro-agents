#!/bin/bash
set -euxo pipefail

docker compose --file docker-compose.yaml --file docker-compose-dev.yaml --file docker-compose-gpu.yaml up --build "$@"
