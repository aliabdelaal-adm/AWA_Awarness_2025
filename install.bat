@echo off
REM Installation script for AWA AI Video Generation Tool (Windows)

echo ================================================
echo   AWA AI Video Generation Tool - Installation
echo   أداة AWA لتوليد الفيديوهات - التثبيت
echo ================================================
echo.

REM Check Python
echo Checking Python version...
python --version
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)
echo.

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Check FFmpeg
echo Checking for FFmpeg...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo Warning: FFmpeg is not installed or not in PATH
    echo Please install FFmpeg from https://ffmpeg.org/download.html
    echo and add it to your system PATH
) else (
    echo FFmpeg is installed
)
echo.

echo ================================================
echo Installation completed!
echo اكتمل التثبيت!
echo ================================================
echo.
echo Usage example:
echo   python main.py your_document.pdf
echo.
pause
