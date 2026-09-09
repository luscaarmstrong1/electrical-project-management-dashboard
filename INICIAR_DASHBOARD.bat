@echo off
setlocal
cd /d "%~dp0web"
echo Abrindo dashboard em http://localhost:8000
start "Dashboard Projetos Eletricos" /min python -m http.server 8000
timeout /t 2 /nobreak >nul
start "" "http://localhost:8000"
