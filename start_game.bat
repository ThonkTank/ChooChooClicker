@echo off
setlocal
where py >nul 2>nul
if %errorlevel%==0 (
    py src\main.py %*
    exit /b %errorlevel%
)
where python >nul 2>nul
if %errorlevel%==0 (
    python src\main.py %*
    exit /b %errorlevel%
)
echo Fehler: Es konnte kein Python-Interpreter gefunden werden. Bitte installiere Python 3.10 oder neuer mit Tkinter-Unterstuetzung.
exit /b 1
