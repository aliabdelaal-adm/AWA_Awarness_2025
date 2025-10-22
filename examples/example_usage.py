"""
Example Script: Generate Video from Sample PDF
This demonstrates how to use the AWA Video Generation Tool programmatically
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import VideoGenerationApp


def create_sample_video():
    """Create a sample video demonstration"""
    
    print("="*60)
    print("  AWA Video Generation Tool - Example")
    print("  مثال على أداة توليد الفيديوهات")
    print("="*60)
    print()
    
    # Initialize the app
    app = VideoGenerationApp('config.yaml')
    
    # Example: Create video from a hypothetical PDF
    # Replace with your actual PDF path
    sample_pdf = "uploads/sample_document.pdf"
    
    if not os.path.exists(sample_pdf):
        print(f"Note: Sample PDF not found at {sample_pdf}")
        print("Please place a PDF file in the uploads/ folder")
        print()
        print("Example usage:")
        print('  app.run("path/to/your/document.pdf", ')
        print('          output_name="my_video.mp4", ')
        print('          title="My Video Title", ')
        print('          language="ar")')
        return
    
    # Generate the video
    app.run(
        pdf_path=sample_pdf,
        output_name="example_video.mp4",
        title="فيديو توعوي تجريبي",
        language="ar"
    )


if __name__ == '__main__':
    create_sample_video()
