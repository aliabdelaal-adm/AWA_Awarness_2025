"""
Test script for the AWA Presentation Design Platform
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_platform_imports():
    """Test that all platform modules can be imported"""
    print("Testing platform imports...")
    
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))
        from modules.pdf_processor import PDFProcessor
        print("✓ pdf_processor imported successfully")
    except Exception as e:
        print(f"✗ pdf_processor import failed: {e}")
        return False
    
    try:
        from modules.text_to_speech import TextToSpeech
        print("✓ text_to_speech imported successfully")
    except Exception as e:
        print(f"✗ text_to_speech import failed: {e}")
        return False
    
    try:
        from modules.video_generator import VideoGenerator
        print("✓ video_generator imported successfully")
    except Exception as e:
        print(f"✗ video_generator import failed: {e}")
        return False
    
    try:
        from modules.presentation_builder import PresentationBuilder
        print("✓ presentation_builder imported successfully")
    except Exception as e:
        print(f"✗ presentation_builder import failed: {e}")
        return False
    
    return True


def test_web_app_imports():
    """Test that web application can be imported"""
    print("\nTesting web application imports...")
    
    try:
        import flask
        print("✓ Flask imported successfully")
    except Exception as e:
        print(f"✗ Flask import failed: {e}")
        return False
    
    try:
        from pptx import Presentation
        print("✓ python-pptx imported successfully")
    except Exception as e:
        print(f"✗ python-pptx import failed: {e}")
        return False
    
    return True


def test_directory_structure():
    """Test that all required directories exist"""
    print("\nTesting directory structure...")
    
    required_dirs = [
        'src/modules',
        'uploads',
        'output/videos',
        'output/presentations',
        'output/audio',
        'templates',
        'examples'
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"✓ {dir_path} exists")
        else:
            print(f"✗ {dir_path} missing")
            all_exist = False
    
    return all_exist


def test_required_files():
    """Test that required files exist"""
    print("\nTesting required files...")
    
    required_files = [
        'app.py',
        'main.py',
        'config.yaml',
        'requirements.txt',
        'start_platform.sh',
        'start_platform.bat',
        'templates/index.html',
        'src/modules/presentation_builder.py'
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path} exists")
        else:
            print(f"✗ {file_path} missing")
            all_exist = False
    
    return all_exist


def test_presentation_builder():
    """Test basic functionality of presentation builder"""
    print("\nTesting presentation builder functionality...")
    
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))
        from modules.presentation_builder import PresentationBuilder
        
        builder = PresentationBuilder()
        print("✓ PresentationBuilder instantiated successfully")
        
        # Test with minimal data
        test_slides = [
            {'title': 'Test Slide 1', 'content': 'This is a test slide'},
            {'title': 'Test Slide 2', 'content': 'This is another test slide'}
        ]
        
        test_output = '/tmp/test_presentation.pptx'
        result = builder.create_presentation(
            title='Test Presentation',
            slides=test_slides,
            output_path=test_output,
            language='en'
        )
        
        if result and os.path.exists(test_output):
            print("✓ Test presentation created successfully")
            os.remove(test_output)  # Clean up
            return True
        else:
            print("✗ Failed to create test presentation")
            return False
    
    except Exception as e:
        print(f"✗ Presentation builder test failed: {e}")
        return False


def run_tests():
    """Run all tests"""
    print("="*60)
    print("  AWA Presentation Design Platform - Tests")
    print("="*60)
    print()
    
    results = []
    
    results.append(("Platform Imports", test_platform_imports()))
    results.append(("Web App Imports", test_web_app_imports()))
    results.append(("Directory Structure", test_directory_structure()))
    results.append(("Required Files", test_required_files()))
    results.append(("Presentation Builder", test_presentation_builder()))
    
    print("\n" + "="*60)
    print("Test Results:")
    print("="*60)
    
    all_passed = True
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {test_name}")
        if not result:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("✓ All tests passed!")
        print("\nYou can now start the platform with:")
        print("  ./start_platform.sh (Linux/Mac)")
        print("  start_platform.bat (Windows)")
        print("  or: python app.py")
        return 0
    else:
        print("✗ Some tests failed")
        return 1


if __name__ == '__main__':
    sys.exit(run_tests())
