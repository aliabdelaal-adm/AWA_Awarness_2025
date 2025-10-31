#!/usr/bin/env python3
"""
Installation Verification Script for AWA Platform
Checks if all required dependencies are installed and working
"""

import sys
import importlib

def check_module(module_name, package_name=None, optional=False):
    """Check if a module can be imported"""
    if package_name is None:
        package_name = module_name
    
    try:
        importlib.import_module(module_name)
        status = "✓"
        message = f"OK - {package_name}"
        return True, f"{status} {message}"
    except ImportError as e:
        status = "⚠" if optional else "✗"
        message = f"MISSING - {package_name}"
        if optional:
            message += " (optional)"
        return optional, f"{status} {message}"

def main():
    """Run installation verification"""
    print("=" * 60)
    print("AWA Platform - Installation Verification")
    print("=" * 60)
    print()
    
    # Core dependencies
    print("Core Dependencies:")
    print("-" * 60)
    
    modules = [
        ("flask", "Flask"),
        ("flask_cors", "Flask-CORS"),
        ("yaml", "PyYAML"),
        ("PIL", "Pillow"),
        ("numpy", "NumPy"),
    ]
    
    all_ok = True
    for module, package in modules:
        ok, msg = check_module(module, package)
        print(msg)
        all_ok = all_ok and ok
    
    print()
    
    # PDF Processing
    print("PDF Processing:")
    print("-" * 60)
    
    modules = [
        ("PyPDF2", "PyPDF2"),
        ("pdfplumber", "pdfplumber"),
    ]
    
    for module, package in modules:
        ok, msg = check_module(module, package)
        print(msg)
        all_ok = all_ok and ok
    
    print()
    
    # Text-to-Speech
    print("Text-to-Speech:")
    print("-" * 60)
    
    modules = [
        ("gtts", "gTTS"),
        ("edge_tts", "edge-tts"),
        ("pydub", "pydub"),
    ]
    
    for module, package in modules:
        ok, msg = check_module(module, package)
        print(msg)
        all_ok = all_ok and ok
    
    print()
    
    # Video Processing
    print("Video Processing:")
    print("-" * 60)
    
    modules = [
        ("moviepy", "moviepy"),
        ("cv2", "opencv-python"),
    ]
    
    for module, package in modules:
        ok, msg = check_module(module, package)
        print(msg)
        all_ok = all_ok and ok
    
    print()
    
    # Document Generation
    print("Document Generation:")
    print("-" * 60)
    
    modules = [
        ("pptx", "python-pptx"),
        ("docx", "python-docx"),
        ("openpyxl", "openpyxl"),
        ("reportlab", "reportlab"),
    ]
    
    for module, package in modules:
        ok, msg = check_module(module, package)
        print(msg)
        all_ok = all_ok and ok
    
    print()
    
    # Arabic Text Support (Optional but recommended)
    print("Arabic Text Support (Optional but recommended):")
    print("-" * 60)
    
    modules = [
        ("arabic_reshaper", "arabic-reshaper", True),
        ("bidi", "python-bidi", True),
    ]
    
    for module, package, optional in modules:
        ok, msg = check_module(module, package, optional)
        print(msg)
        # Don't fail if optional modules missing
    
    print()
    
    # AI Services (Optional)
    print("AI Services (Optional):")
    print("-" * 60)
    
    modules = [
        ("openai", "openai", True),
        ("anthropic", "anthropic", True),
    ]
    
    for module, package, optional in modules:
        ok, msg = check_module(module, package, optional)
        print(msg)
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✓ All required dependencies are installed!")
        print()
        print("Next steps:")
        print("1. Run the platform: python app.py")
        print("2. Run tests: python test_all_formats.py")
        print("3. Open browser: http://localhost:5000")
        return 0
    else:
        print("✗ Some required dependencies are missing!")
        print()
        print("To install all dependencies, run:")
        print("  pip install -r requirements.txt")
        print()
        print("Or install missing packages individually using pip.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
