#!/bin/bash
# Installation script for AWA AI Video Generation Tool

echo "================================================"
echo "  AWA AI Video Generation Tool - Installation"
echo "  أداة AWA لتوليد الفيديوهات - التثبيت"
echo "================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $python_version"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is not installed. Please install pip3 first."
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Python dependencies installed successfully"
else
    echo "✗ Failed to install Python dependencies"
    exit 1
fi

echo ""

# Check FFmpeg
echo "Checking for FFmpeg..."
if command -v ffmpeg &> /dev/null; then
    ffmpeg_version=$(ffmpeg -version 2>&1 | head -n 1)
    echo "✓ FFmpeg is installed: $ffmpeg_version"
else
    echo "⚠ Warning: FFmpeg is not installed"
    echo "Please install FFmpeg:"
    echo "  - Ubuntu/Debian: sudo apt-get install ffmpeg"
    echo "  - macOS: brew install ffmpeg"
    echo "  - Windows: Download from https://ffmpeg.org/download.html"
fi

echo ""
echo "================================================"
echo "✓ Installation completed!"
echo "✓ اكتمل التثبيت!"
echo "================================================"
echo ""
echo "Usage example / مثال الاستخدام:"
echo "  python3 main.py your_document.pdf"
echo ""
