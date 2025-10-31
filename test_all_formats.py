#!/usr/bin/env python3
"""
Test script for all output formats in AWA platform
Tests video, PowerPoint, Excel, Word, and PDF generation
"""

import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from modules.presentation_builder import PresentationBuilder
from modules.excel_generator import ExcelGenerator
from modules.report_generator import ReportGenerator
from modules.text_to_speech import TextToSpeech
from modules.video_generator import VideoGenerator


def test_powerpoint_generation():
    """Test PowerPoint generation with Arabic support and max_slides"""
    print("\n" + "="*60)
    print("Testing PowerPoint Generation")
    print("="*60)
    
    builder = PresentationBuilder()
    
    # Test data
    slides = [
        {
            'title': 'مقدمة',
            'content': 'هذا اختبار للعرض التقديمي باللغة العربية.\nيجب أن يظهر النص بشكل صحيح.'
        },
        {
            'title': 'القسم الأول',
            'content': 'محتوى القسم الأول\nمعلومات إضافية\nنقاط مهمة'
        },
        {
            'title': 'القسم الثاني',
            'content': 'محتوى القسم الثاني\nمزيد من المعلومات'
        },
        {
            'title': 'القسم الثالث',
            'content': 'محتوى القسم الثالث\nتفاصيل إضافية'
        },
        {
            'title': 'الخاتمة',
            'content': 'خاتمة العرض التقديمي\nشكراً للمشاهدة'
        }
    ]
    
    # Test without max_slides
    print("\n1. Testing without slide limit...")
    output_path_full = 'output/presentations/test_full_ar.pptx'
    result = builder.create_presentation(
        title='عرض تجريبي كامل',
        slides=slides,
        output_path=output_path_full,
        language='ar',
        max_slides=None
    )
    
    if result and os.path.exists(result):
        print(f"✓ Full presentation created: {result}")
        print(f"  File size: {os.path.getsize(result) / 1024:.2f} KB")
    else:
        print("✗ Failed to create full presentation")
    
    # Test with max_slides
    print("\n2. Testing with max_slides=3...")
    output_path_limited = 'output/presentations/test_limited_ar.pptx'
    result = builder.create_presentation(
        title='عرض تجريبي مختصر',
        slides=slides,
        output_path=output_path_limited,
        language='ar',
        max_slides=3
    )
    
    if result and os.path.exists(result):
        print(f"✓ Limited presentation created: {result}")
        print(f"  File size: {os.path.getsize(result) / 1024:.2f} KB")
    else:
        print("✗ Failed to create limited presentation")
    
    # Test English version
    print("\n3. Testing English version...")
    slides_en = [
        {
            'title': 'Introduction',
            'content': 'This is a test presentation in English.\nThe text should display correctly.'
        },
        {
            'title': 'Section One',
            'content': 'Content of section one\nAdditional information\nImportant points'
        }
    ]
    
    output_path_en = 'output/presentations/test_english.pptx'
    result = builder.create_presentation(
        title='Test Presentation',
        slides=slides_en,
        output_path=output_path_en,
        language='en',
        max_slides=None
    )
    
    if result and os.path.exists(result):
        print(f"✓ English presentation created: {result}")
        print(f"  File size: {os.path.getsize(result) / 1024:.2f} KB")
    else:
        print("✗ Failed to create English presentation")


def test_excel_generation():
    """Test Excel spreadsheet generation"""
    print("\n" + "="*60)
    print("Testing Excel Generation")
    print("="*60)
    
    generator = ExcelGenerator()
    
    # Test data
    text_chunks = [
        'القسم الأول: معلومات عن المنتج\nالمنتج عالي الجودة\nالسعر مناسب',
        'القسم الثاني: المميزات\nمميزات عديدة\nجودة ممتازة',
        'القسم الثالث: الخلاصة\nمنتج موصى به\nيستحق الشراء'
    ]
    
    output_path = 'output/excel/test_data_ar.xlsx'
    result = generator.generate_from_chunks(
        text_chunks=text_chunks,
        title='بيانات اختبارية',
        output_path=output_path
    )
    
    if result and os.path.exists(result):
        print(f"✓ Excel file created: {result}")
        print(f"  File size: {os.path.getsize(result) / 1024:.2f} KB")
    else:
        print("✗ Failed to create Excel file")


def test_word_generation():
    """Test Word document generation"""
    print("\n" + "="*60)
    print("Testing Word Document Generation")
    print("="*60)
    
    generator = ReportGenerator()
    
    # Test data
    text_chunks = [
        'المقدمة\nهذا تقرير اختباري باللغة العربية.\nيحتوي على معلومات مهمة.',
        'القسم الأول\nمحتوى القسم الأول\nمعلومات تفصيلية عن الموضوع.',
        'القسم الثاني\nمحتوى القسم الثاني\nمزيد من التفاصيل والشرح.',
        'الخاتمة\nخاتمة التقرير\nشكراً للقراءة.'
    ]
    
    output_path = 'output/reports/test_report_ar.docx'
    result = generator.generate_word_report(
        text_chunks=text_chunks,
        title='تقرير اختباري',
        subtitle='تقرير إحترافي باللغة العربية',
        output_path=output_path
    )
    
    if result and os.path.exists(result):
        print(f"✓ Word document created: {result}")
        print(f"  File size: {os.path.getsize(result) / 1024:.2f} KB")
    else:
        print("✗ Failed to create Word document")


def test_pdf_generation():
    """Test PDF report generation"""
    print("\n" + "="*60)
    print("Testing PDF Report Generation")
    print("="*60)
    
    generator = ReportGenerator()
    
    # Test data
    text_chunks = [
        'Introduction\nThis is a test PDF report in English.\nIt contains important information.',
        'Section One\nContent of section one\nDetailed information about the topic.',
        'Section Two\nContent of section two\nMore details and explanation.',
        'Conclusion\nConclusion of the report\nThank you for reading.'
    ]
    
    output_path = 'output/reports/test_report_en.pdf'
    result = generator.generate_pdf_report(
        text_chunks=text_chunks,
        title='Test Report',
        subtitle='Professional Report in English',
        output_path=output_path
    )
    
    if result and os.path.exists(result):
        print(f"✓ PDF report created: {result}")
        print(f"  File size: {os.path.getsize(result) / 1024:.2f} KB")
    else:
        print("✗ Failed to create PDF report")


def test_tts_generation():
    """Test Text-to-Speech audio generation"""
    print("\n" + "="*60)
    print("Testing Text-to-Speech Generation")
    print("="*60)
    
    tts = TextToSpeech(language='ar')
    
    # Test data
    texts = [
        'مرحباً بكم في منصة AWA',
        'هذا اختبار للنطق باللغة العربية',
        'شكراً لاستخدام المنصة'
    ]
    
    print("\n1. Testing Arabic TTS...")
    audio_files = tts.generate_multiple(texts, prefix='test_ar', use_edge=True)
    
    if audio_files:
        print(f"✓ Generated {len(audio_files)} audio files:")
        for audio_file in audio_files:
            if os.path.exists(audio_file):
                print(f"  - {audio_file} ({os.path.getsize(audio_file) / 1024:.2f} KB)")
            else:
                print(f"  - {audio_file} (FILE NOT FOUND)")
    else:
        print("✗ Failed to generate audio files")
    
    # Test English
    print("\n2. Testing English TTS...")
    tts_en = TextToSpeech(language='en')
    texts_en = [
        'Welcome to AWA platform',
        'This is a test of English speech'
    ]
    
    audio_files_en = tts_en.generate_multiple(texts_en, prefix='test_en', use_edge=True)
    
    if audio_files_en:
        print(f"✓ Generated {len(audio_files_en)} English audio files")
    else:
        print("✗ Failed to generate English audio files")


def test_video_generation():
    """Test video generation with audio"""
    print("\n" + "="*60)
    print("Testing Video Generation")
    print("="*60)
    
    # First generate audio
    tts = TextToSpeech(language='ar')
    texts = [
        'مرحباً بكم',
        'هذا فيديو اختباري'
    ]
    
    print("\n1. Generating audio for video...")
    audio_files = tts.generate_multiple(texts, prefix='video_test', use_edge=True)
    
    if not audio_files:
        print("✗ Failed to generate audio files, skipping video test")
        return
    
    print(f"✓ Generated {len(audio_files)} audio files")
    
    # Now generate video
    print("\n2. Generating video...")
    config = {
        'fps': 30,
        'resolution': [1280, 720],
        'background_color': [255, 255, 255],
        'text_color': [0, 0, 0]
    }
    
    video_gen = VideoGenerator(config)
    
    video_path = video_gen.generate_video(
        text_chunks=texts,
        audio_files=audio_files,
        output_filename='test_video_ar.mp4',
        title='فيديو اختباري'
    )
    
    if video_path and os.path.exists(video_path):
        print(f"✓ Video created: {video_path}")
        print(f"  File size: {os.path.getsize(video_path) / 1024:.2f} KB")
    else:
        print("✗ Failed to create video")


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("AWA Platform - Comprehensive Output Format Tests")
    print("="*60)
    
    # Ensure output directories exist
    os.makedirs('output/presentations', exist_ok=True)
    os.makedirs('output/excel', exist_ok=True)
    os.makedirs('output/reports', exist_ok=True)
    os.makedirs('output/videos', exist_ok=True)
    os.makedirs('output/audio', exist_ok=True)
    
    try:
        # Run tests
        test_powerpoint_generation()
        test_excel_generation()
        test_word_generation()
        test_pdf_generation()
        test_tts_generation()
        test_video_generation()
        
        print("\n" + "="*60)
        print("All tests completed!")
        print("="*60)
        print("\nGenerated files:")
        print("  PowerPoint: output/presentations/")
        print("  Excel:      output/excel/")
        print("  Word/PDF:   output/reports/")
        print("  Video:      output/videos/")
        print("  Audio:      output/audio/")
        
    except Exception as e:
        print(f"\n✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
