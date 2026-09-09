@echo off
setlocal
cd /d "%~dp0"
call ATUALIZAR_TUDO.bat
git init
git branch -M main
git add .
git commit -m "Finaliza dashboard de gestao de projetos eletricos" || echo Nada novo para commit.
gh repo view renovera1/electrical-project-management-dashboard >nul 2>&1 || gh repo create renovera1/electrical-project-management-dashboard --public --source=. --remote=origin
git remote get-url origin >nul 2>&1 || git remote add origin https://github.com/renovera1/electrical-project-management-dashboard.git
git push -u origin main
gh pages deploy web --repo renovera1/electrical-project-management-dashboard --branch gh-pages
echo.
echo Repositorio: https://github.com/renovera1/electrical-project-management-dashboard
echo Dashboard: https://renovera1.github.io/electrical-project-management-dashboard/
pause
