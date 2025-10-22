"""
Test script to validate the video generation pipeline
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
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
    
    return True


def test_config():
    """Test configuration loading"""
    print("\nTesting configuration...")
    
    try:
        import yaml
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        print("✓ Configuration loaded successfully")
        print(f"  Default language: {config['tts']['default_language']}")
        print(f"  Video FPS: {config['video']['fps']}")
        return True
    except Exception as e:
        print(f"✗ Configuration loading failed: {e}")
        return False


def test_directory_structure():
    """Test that all required directories exist"""
    print("\nTesting directory structure...")
    
    required_dirs = [
        'src/modules',
        'uploads',
        'output/videos',
        'templates/video_templates',
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


def run_tests():
    """Run all tests"""
    print("="*60)
    print("  AWA Video Generation Tool - Tests")
    print("="*60)
    print()
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Configuration", test_config()))
    results.append(("Directory Structure", test_directory_structure()))
    
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
        return 0
    else:
        print("✗ Some tests failed")
        return 1


if __name__ == '__main__':
    sys.exit(run_tests())
