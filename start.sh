#!/usr/bin/env sh
# Uso: ./start.sh [docker|python]   (sem argumento: usa Docker se estiver disponível, senão Python)
cd "$(dirname "$0")" || exit 1
mode="$1"
if [ -z "$mode" ]; then
  if docker info >/dev/null 2>&1; then mode=docker; else mode=python; fi
fi
echo "Iniciando via $mode -> http://localhost:${PORT:-8765}"
if [ "$mode" = docker ]; then
  exec docker compose up --build
else
  exec "$(command -v python3 || command -v python)" app.py
fi
