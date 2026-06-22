@echo off
REM Double-click me to wake BRIM.
chcp 65001 >nul
python octopus.py
if errorlevel 1 python3 octopus.py
echo.
pause
