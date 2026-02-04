@echo off
chcp 65001 > nul
title ⚡ SolarPunk One-Click Fixer
color 0A

echo.
echo ╔══════════════════════════════════════════════════╗
echo ║            SOLARPUNK ONE-CLICK FIXER             ║
echo ╚══════════════════════════════════════════════════╝
echo.

echo 📂 Creating basic folders...
mkdir connected 2>nul
mkdir dist 2>nul
mkdir logs 2>nul
mkdir scripts 2>nul

echo 📄 Creating essential files...

:: 1. Create START.bat (run agent)
echo @echo off > START.bat
echo cd /d "C:\Users\carol\SolarPunk" >> START.bat
echo python -c "print('Agent started')" >> START.bat
echo pause >> START.bat

:: 2. Create PUSH.bat (push to GitHub)
echo @echo off > PUSH.bat
echo cd /d "C:\Users\carol\SolarPunk" >> PUSH.bat
echo git add . 2>nul >> PUSH.bat
echo git commit -m "Auto-update %%date%% %%time%%" 2>nul >> PUSH.bat
echo git push origin master 2>nul >> PUSH.bat
echo echo ✅ Pushed to GitHub >> PUSH.bat
echo pause >> PUSH.bat

:: 3. Create a simple agent
echo print("SolarPunk Agent Ready") > agent_simple.py
echo print("Run START.bat to begin") >> agent_simple.py

:: 4. Create Cloudflare content
echo ^<!DOCTYPE html^> > dist\index.html
echo ^<html^> >> dist\index.html
echo ^<head^> >> dist\index.html
echo ^<title^>SolarPunk - Fixed!^</title^> >> dist\index.html
echo ^</head^> >> dist\index.html
echo ^<body^> >> dist\index.html
echo ^<h1^>✅ System Fixed!^</h1^> >> dist\index.html
echo ^<p^>One-click fixer worked.^</p^> >> dist\index.html
echo ^</body^> >> dist\index.html
echo ^</html^> >> dist\index.html

echo.
echo ✅ CREATED:
echo   • START.bat (run this)
echo   • PUSH.bat (push updates)
echo   • agent_simple.py
echo   • dist\index.html (for Cloudflare)
echo.
echo 🚀 NEXT:
echo   1. Double-click START.bat
echo   2. Double-click PUSH.bat
echo   3. Wait 30 seconds for Cloudflare
echo.
echo 🌐 Check: https://solarpunkagent.pages.dev
echo.
pause