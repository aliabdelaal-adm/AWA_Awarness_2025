#!/bin/bash
# AWA Presentation Design Platform - Startup Script
# منصة تصميم العروض الإحترافية AWA - سكريبت البدء

echo "=========================================="
echo "  AWA Presentation Design Platform"
echo "  منصة تصميم العروض الإحترافية AWA"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "Creating necessary directories..."
mkdir -p uploads
mkdir -p output/videos
mkdir -p output/presentations
mkdir -p output/audio

# Start the web application
echo ""
echo "=========================================="
echo "Starting AWA Presentation Platform..."
echo "يتم تشغيل منصة AWA للعروض..."
echo "=========================================="
echo ""
echo "The platform will be available at:"
echo "المنصة ستكون متاحة على:"
echo "http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "اضغط Ctrl+C لإيقاف الخادم"
echo ""

python app.py
