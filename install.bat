@echo off
REM Installation script for AWA Content Generation Platform (Windows)

REM Enable UTF-8 for Arabic characters
chcp 65001 >nul 2>&1

echo ================================================================
echo   AWA Content Generation Platform - Installation
echo   منصة AWA لتوليد المحتوى - التثبيت
echo ================================================================
echo.
echo This script will install all required Python libraries
echo سيقوم هذا النص البرمجي بتثبيت جميع مكتبات Python المطلوبة
echo.
echo ----------------------------------------------------------------
echo.

REM Check Python
echo [1/3] Checking Python installation...
echo [1/3] فحص تثبيت Python...
python --version
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Python is not installed or not in PATH
    echo [خطأ] Python غير مثبت أو غير موجود في PATH
    echo.
    echo Please install Python 3.8+ from: https://www.python.org/downloads/
    echo يرجى تثبيت Python 3.8+ من: https://www.python.org/downloads/
    echo.
    echo IMPORTANT: Make sure to check "Add Python to PATH" during installation!
    echo مهم: تأكد من وضع علامة في "Add Python to PATH" أثناء التثبيت!
    echo.
    echo For detailed installation guide, see: WINDOWS_SETUP_GUIDE.md
    echo للحصول على دليل التثبيت الكامل، راجع: WINDOWS_SETUP_GUIDE.md
    echo.
    pause
    exit /b 1
)
echo [OK] Python is installed / Python مثبت
echo.

REM Install dependencies
echo [2/3] Installing Python dependencies...
echo [2/3] تثبيت مكتبات Python...
echo.
echo This may take several minutes, please wait...
echo قد يستغرق هذا عدة دقائق، يرجى الانتظار...
echo.
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to install dependencies
    echo [خطأ] فشل تثبيت المكتبات
    echo.
    echo Please check your internet connection and try again
    echo يرجى التحقق من اتصال الإنترنت والمحاولة مرة أخرى
    echo.
    pause
    exit /b 1
)
echo.
echo [OK] All Python libraries installed successfully!
echo [OK] تم تثبيت جميع مكتبات Python بنجاح!
echo.

REM Check FFmpeg
echo [3/3] Checking for FFmpeg...
echo [3/3] فحص FFmpeg...
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] FFmpeg is not installed or not in PATH
    echo [تحذير] FFmpeg غير مثبت أو غير موجود في PATH
    echo.
    echo FFmpeg is required for video generation features
    echo FFmpeg مطلوب لميزات توليد الفيديو
    echo.
    echo Download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/
    echo تحميل FFmpeg من: https://www.gyan.dev/ffmpeg/builds/
    echo.
    echo For installation instructions, see: WINDOWS_SETUP_GUIDE.md
    echo لتعليمات التثبيت، راجع: WINDOWS_SETUP_GUIDE.md
    echo.
    echo Note: You can still use other features (PowerPoint, Word, Excel, PDF)
    echo ملاحظة: يمكنك استخدام الميزات الأخرى (PowerPoint, Word, Excel, PDF)
    echo.
) else (
    echo [OK] FFmpeg is installed / FFmpeg مثبت
    echo.
)

REM Create necessary directories
echo Creating output directories...
echo إنشاء مجلدات الإخراج...
if not exist "output" mkdir output
if not exist "output\videos" mkdir output\videos
if not exist "output\presentations" mkdir output\presentations
if not exist "output\reports" mkdir output\reports
if not exist "output\excel" mkdir output\excel
if not exist "uploads" mkdir uploads
echo [OK] Directories created / تم إنشاء المجلدات
echo.

echo ================================================================
echo Installation completed successfully!
echo اكتمل التثبيت بنجاح!
echo ================================================================
echo.
echo Next steps / الخطوات التالية:
echo.
echo 1. To launch the platform, run:
echo    لتشغيل المنصة، نفذ:
echo    - Double-click: awa_launch.bat
echo    - Or run: python launcher.py
echo.
echo 2. For usage instructions, see:
echo    لتعليمات الاستخدام، راجع:
echo    - QUICK_START.md
echo    - WINDOWS_SETUP_GUIDE.md
echo    - README.md
echo.
echo 3. Examples:
echo    أمثلة:
echo    - python launcher.py                    (Interactive menu)
echo    - python launcher.py file.pdf --format powerpoint
echo    - python launcher.py file.pdf --format video --language ar
echo    - python launcher.py file.pdf --format all
echo.
echo ================================================================
echo.
pause
