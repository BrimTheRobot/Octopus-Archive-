@echo off
REM Double-click me to wake BRIM.
chcp 65001 >nul
setlocal

set "PYEXE="
REM Prefer a real Python install over the Microsoft Store stub.
if exist "%LOCALAPPDATA%\Python\bin\python.exe" set "PYEXE=%LOCALAPPDATA%\Python\bin\python.exe"
if not defined PYEXE for %%P in (python.exe python3.exe py.exe) do if not defined PYEXE where %%P >nul 2>nul && set "PYEXE=%%P"

if not defined PYEXE (
  echo BRIM could not find Python on this machine.
  echo Install it from https://www.python.org/downloads/ and tick "Add Python to PATH".
  echo.
  pause
  exit /b 1
)

"%PYEXE%" octopus.py
echo.
pause
