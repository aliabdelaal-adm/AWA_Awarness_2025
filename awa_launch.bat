@echo off
REM AWA Content Generation Platform - Easy Launcher
REM منصة AWA لتوليد المحتوى - أداة الإطلاق السريع

REM Enable UTF-8 for Arabic characters
chcp 65001 >nul 2>&1

REM Change to script directory
cd /d "%~dp0"

echo ============================================================
echo    AWA Content Generation Platform / منصة AWA لتوليد المحتوى
echo ============================================================
echo.

REM Check if Python is installed
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo [خطأ] Python غير مثبت أو غير موجود في PATH
    echo.
    echo Please install Python 3.8+ from: https://www.python.org/downloads/
    echo تثبيت Python 3.8+ من: https://www.python.org/downloads/
    echo.
    echo For detailed installation guide, see: WINDOWS_SETUP_GUIDE.md
    echo للحصول على دليل التثبيت الكامل، راجع: WINDOWS_SETUP_GUIDE.md
    echo.
    pause
    exit /b 1
)
python --version
echo [OK] Python is installed / Python مثبت
echo.

REM Check if requirements are installed
echo [2/4] Checking required Python libraries...
python -c "import colorama" >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Required libraries not installed
    echo [تحذير] المكتبات المطلوبة غير مثبتة
    echo.
    echo Installing required libraries...
    echo جاري تثبيت المكتبات المطلوبة...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to install libraries
        echo [خطأ] فشل تثبيت المكتبات
        echo.
        pause
        exit /b 1
    )
)
echo [OK] Required libraries are installed / المكتبات المطلوبة مثبتة
echo.

REM Check FFmpeg (optional but recommended)
echo [3/4] Checking FFmpeg (required for video generation)...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] FFmpeg is not installed or not in PATH
    echo [تحذير] FFmpeg غير مثبت أو غير موجود في PATH
    echo.
    echo FFmpeg is required for video generation
    echo FFmpeg مطلوب لتوليد الفيديو
    echo.
    echo Download from: https://www.gyan.dev/ffmpeg/builds/
    echo تحميل من: https://www.gyan.dev/ffmpeg/builds/
    echo.
    echo For installation guide, see: WINDOWS_SETUP_GUIDE.md
    echo لدليل التثبيت، راجع: WINDOWS_SETUP_GUIDE.md
    echo.
    echo You can still use other features (PowerPoint, Word, Excel)
    echo يمكنك استخدام الميزات الأخرى (PowerPoint, Word, Excel)
    echo.
) else (
    echo [OK] FFmpeg is installed / FFmpeg مثبت
    echo.
)

REM Create output directories if they don't exist
echo [4/4] Setting up output directories...
if not exist "output" mkdir output
if not exist "output\videos" mkdir output\videos
if not exist "output\presentations" mkdir output\presentations
if not exist "output\reports" mkdir output\reports
if not exist "output\excel" mkdir output\excel
if not exist "uploads" mkdir uploads
echo [OK] Output directories ready / مجلدات الإخراج جاهزة
echo.

echo ============================================================
echo    Starting AWA Platform... / جاري تشغيل منصة AWA...
echo ============================================================
echo.

REM Launch the platform
python launcher.py %*

REM Keep window open if there was an error
if %errorlevel% neq 0 (
    echo.
    echo ============================================================
    echo [ERROR] Platform exited with an error
    echo [خطأ] المنصة توقفت بسبب خطأ
    echo.
    echo For help, see: WINDOWS_SETUP_GUIDE.md
    echo للمساعدة، راجع: WINDOWS_SETUP_GUIDE.md
    echo ============================================================
    echo.
    pause
)
