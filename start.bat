@echo off
rem Uso: start.bat [docker|python]   (sem argumento: Docker se disponivel, senao Python)
cd /d "%~dp0"
set MODE=%1
if "%PORT%"=="" set PORT=8765
if "%MODE%"=="" (
  docker info >nul 2>&1 && (set MODE=docker) || (set MODE=python)
)
echo Iniciando via %MODE% -^> http://localhost:%PORT%
if "%MODE%"=="docker" (
  docker compose up --build
) else (
  where py >nul 2>&1 && (py -3 app.py) || (python app.py)
)
