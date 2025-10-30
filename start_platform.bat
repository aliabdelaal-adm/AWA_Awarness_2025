@echo off
REM AWA Presentation Design Platform - Windows Startup Script
REM منصة تصميم العروض الإحترافية AWA - سكريبت البدء لويندوز

echo ==========================================
echo   AWA Presentation Design Platform
echo   منصة تصميم العروض الإحترافية AWA
echo ==========================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create necessary directories
echo Creating necessary directories...
if not exist "uploads" mkdir uploads
if not exist "output\videos" mkdir output\videos
if not exist "output\presentations" mkdir output\presentations
if not exist "output\audio" mkdir output\audio

REM Start the web application
echo.
echo ==========================================
echo Starting AWA Presentation Platform...
echo يتم تشغيل منصة AWA للعروض...
echo ==========================================
echo.
echo The platform will be available at:
echo المنصة ستكون متاحة على:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo اضغط Ctrl+C لإيقاف الخادم
echo.

python app.py
pause
