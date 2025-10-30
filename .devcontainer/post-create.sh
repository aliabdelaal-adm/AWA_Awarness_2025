#!/bin/bash

# AWA Platform Post-Create Setup Script
# This script runs after the container is created

echo "🚀 Setting up AWA Platform..."

# Update package lists
echo "📦 Updating package lists..."
apt-get update -qq

# Install FFmpeg (required for video generation)
echo "🎬 Installing FFmpeg..."
apt-get install -y ffmpeg > /dev/null 2>&1

# Verify FFmpeg installation
if command -v ffmpeg &> /dev/null; then
    echo "✅ FFmpeg installed successfully: $(ffmpeg -version | head -n1)"
else
    echo "❌ FFmpeg installation failed"
fi

# Upgrade pip
echo "🐍 Upgrading pip..."
python -m pip install --upgrade pip --quiet

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt --quiet

# Create necessary directories
echo "📁 Creating output directories..."
mkdir -p uploads
mkdir -p output/videos
mkdir -p output/presentations
mkdir -p output/reports
mkdir -p output/excel
mkdir -p output/audio

# Make shell scripts executable
echo "🔧 Setting script permissions..."
chmod +x awa_launch.sh
chmod +x install.sh
chmod +x start_platform.sh
chmod +x quick_start.sh
chmod +x launcher.py

# Display welcome message
echo ""
echo "✨ AWA Platform is ready to use!"
echo ""
echo "🌐 To start the web platform, run:"
echo "   python app.py"
echo ""
echo "🚀 Or use the launcher:"
echo "   python launcher.py"
echo ""
echo "📖 For help, see:"
echo "   - README.md"
echo "   - CODESPACES_GUIDE.md"
echo ""
