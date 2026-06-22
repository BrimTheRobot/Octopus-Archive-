@echo off
REM Double-click me to wake BRIM. No Python required.
REM PowerShell is built into every Windows PC, so this just works.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0octopus.ps1"
echo.
pause
