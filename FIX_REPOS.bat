@echo off
echo SolarPunk Auto-Fix Tool
echo.
echo Available fixes:
echo 1. Initialize missing git repositories
echo 2. Create missing README files
echo 3. Check for large files
echo.
choice /C 123 /M "Select fix to apply: "

if errorlevel 3 goto CHECK_LARGE_FILES
if errorlevel 2 goto CREATE_README
if errorlevel 1 goto INIT_GIT

:INIT_GIT
echo Initializing git repositories...
for /d %%i in (connected\*) do (
    if not exist "%%i\.git" (
        echo Initializing git in %%i
        cd "%%i"
        git init
        cd..
    )
)
echo Done.
pause
exit

:CREATE_README
echo Creating missing README files...
for /d %%i in (connected\*) do (
    if not exist "%%i\README.md" (
        echo Creating README in %%i
        echo # %%i > "%%i\README.md"
        echo. >> "%%i\README.md"
        echo This repository is managed by SolarPunk Autonomous System. >> "%%i\README.md"
    )
)
echo Done.
pause
exit

:CHECK_LARGE_FILES
echo Checking for large files...
for /r connected %%i in (*.exe,*.zip,*.tar,*.gz) do (
    echo Found: %%i
)
echo.
echo Large files can be removed manually.
pause
exit
