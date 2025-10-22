"""
Advanced Example: Programmatic Video Generation
Shows how to use the tool as a library in your own Python code
"""

import sys
import os

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import VideoGenerationApp


def example_basic():
    """Basic example: Generate video from PDF"""
    print("Example 1: Basic Video Generation")
    print("=" * 60)
    
    app = VideoGenerationApp()
    
    # Generate video from PDF
    app.run(
        pdf_path="uploads/sample.pdf",
        output_name="basic_video.mp4",
        title="Sample Video",
        language="ar"
    )
    
    print("\n✓ Basic example completed\n")


def example_custom_config():
    """Example with custom configuration"""
    print("Example 2: Custom Configuration")
    print("=" * 60)
    
    # Create custom config
    custom_config = {
        'video': {
            'fps': 25,
            'resolution': [1280, 720],
            'default_duration': 4,
            'transition_duration': 0.5,
            'background_color': [240, 240, 240],
            'text_color': [0, 0, 0]
        },
        'tts': {
            'default_language': 'en',
            'voice_rate': 1.2
        },
        'pdf': {
            'max_chars_per_slide': 250
        }
    }
    
    app = VideoGenerationApp()
    app.config = custom_config
    
    # Generate video with custom settings
    app.run(
        pdf_path="uploads/english_doc.pdf",
        output_name="custom_video.mp4",
        title="Custom Video",
        language="en"
    )
    
    print("\n✓ Custom config example completed\n")


def example_step_by_step():
    """Example: Step-by-step processing"""
    print("Example 3: Step-by-Step Processing")
    print("=" * 60)
    
    app = VideoGenerationApp()
    
    # Step 1: Process PDF
    print("\nStep 1: Processing PDF...")
    text_chunks = app.process_pdf("uploads/document.pdf")
    print(f"Extracted {len(text_chunks)} text segments")
    
    # Step 2: Generate audio
    print("\nStep 2: Generating audio...")
    audio_files = app.generate_audio(text_chunks, language="ar")
    print(f"Created {len(audio_files)} audio files")
    
    # Step 3: Create video
    print("\nStep 3: Creating video...")
    video_path = app.create_video(
        text_chunks=text_chunks,
        audio_files=audio_files,
        output_name="step_by_step_video.mp4",
        title="فيديو تفصيلي"
    )
    
    if video_path:
        print(f"\n✓ Video created: {video_path}")
    
    print("\n✓ Step-by-step example completed\n")


def example_batch_processing():
    """Example: Batch process multiple PDFs"""
    print("Example 4: Batch Processing")
    print("=" * 60)
    
    app = VideoGenerationApp()
    
    # List of PDFs to process
    pdf_files = [
        ("uploads/doc1.pdf", "video1.mp4", "Video 1"),
        ("uploads/doc2.pdf", "video2.mp4", "Video 2"),
        ("uploads/doc3.pdf", "video3.mp4", "Video 3"),
    ]
    
    for pdf_path, output_name, title in pdf_files:
        if os.path.exists(pdf_path):
            print(f"\nProcessing: {pdf_path}")
            app.run(
                pdf_path=pdf_path,
                output_name=output_name,
                title=title,
                language="ar"
            )
        else:
            print(f"Skipping {pdf_path} (not found)")
    
    print("\n✓ Batch processing completed\n")


def example_with_custom_processing():
    """Example: Custom text processing before video generation"""
    print("Example 5: Custom Text Processing")
    print("=" * 60)
    
    from src.modules.pdf_processor import PDFProcessor
    from src.modules.text_to_speech import TextToSpeech
    from src.modules.video_generator import VideoGenerator
    
    # Initialize components
    pdf_processor = PDFProcessor("uploads/document.pdf")
    tts_engine = TextToSpeech(language='ar')
    video_gen = VideoGenerator()
    
    # Extract text
    text_chunks = pdf_processor.split_into_chunks(max_chars=200)
    
    # Custom processing: Add intro and outro
    text_chunks.insert(0, "مرحباً بكم في هذا العرض التقديمي")
    text_chunks.append("شكراً لمشاهدتكم")
    
    # Generate audio
    audio_files = tts_engine.generate_multiple(text_chunks, prefix="custom")
    
    # Create video
    video_path = video_gen.generate_video(
        text_chunks=text_chunks,
        audio_files=audio_files,
        output_filename="custom_processed_video.mp4",
        title="عرض مخصص"
    )
    
    print(f"\n✓ Custom processing completed: {video_path}\n")


def main():
    """Run all examples"""
    print("\n" + "=" * 60)
    print("  AWA Video Generation - Advanced Examples")
    print("  أمثلة متقدمة - أداة توليد الفيديوهات")
    print("=" * 60 + "\n")
    
    # Note: These examples assume PDF files exist
    # You can uncomment and run individual examples
    
    # example_basic()
    # example_custom_config()
    # example_step_by_step()
    # example_batch_processing()
    # example_with_custom_processing()
    
    print("\nTo run examples:")
    print("1. Place PDF files in uploads/ folder")
    print("2. Uncomment the desired example in this script")
    print("3. Run: python examples/advanced_usage.py")
    print("\nلتشغيل الأمثلة:")
    print("1. ضع ملفات PDF في مجلد uploads/")
    print("2. قم بإلغاء التعليق على المثال المطلوب في هذا السكريبت")
    print("3. شغّل: python examples/advanced_usage.py")


if __name__ == '__main__':
    main()
