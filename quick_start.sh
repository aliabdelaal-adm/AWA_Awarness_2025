#!/bin/bash
# Quick Start Script for AWA AI Video Generation Tool

echo "================================================"
echo "  AWA AI Video Generation Tool - Quick Start"
echo "  أداة AWA لتوليد الفيديوهات - بداية سريعة"
echo "================================================"
echo ""

# Check if a PDF file is provided
if [ $# -eq 0 ]; then
    echo "Usage: ./quick_start.sh <path_to_pdf>"
    echo "استخدام: ./quick_start.sh <مسار_ملف_pdf>"
    echo ""
    echo "Example: ./quick_start.sh uploads/my_document.pdf"
    exit 1
fi

PDF_FILE="$1"

# Check if PDF exists
if [ ! -f "$PDF_FILE" ]; then
    echo "Error: PDF file not found: $PDF_FILE"
    echo "خطأ: ملف PDF غير موجود: $PDF_FILE"
    exit 1
fi

echo "Processing: $PDF_FILE"
echo "معالجة: $PDF_FILE"
echo ""

# Check if dependencies are installed
echo "Checking dependencies..."
if ! python3 -c "import PyPDF2" 2>/dev/null; then
    echo "⚠ Dependencies not installed. Installing..."
    echo "⚠ المكتبات غير مثبتة. جاري التثبيت..."
    pip3 install -r requirements.txt
fi

echo ""
echo "Starting video generation..."
echo "بدء توليد الفيديو..."
echo ""

# Run the main script
python3 main.py "$PDF_FILE" --language ar

echo ""
echo "================================================"
echo "Done! Check output/videos/ for your video."
echo "انتهى! تحقق من output/videos/ للفيديو الخاص بك."
echo "================================================"
