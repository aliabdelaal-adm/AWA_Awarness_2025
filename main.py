"""
AI Video Generation Tool - Main Application
Converts PDF documents into professional awareness and promotional videos
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from colorama import init, Fore, Style

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from modules.pdf_processor import PDFProcessor
from modules.text_to_speech import TextToSpeech
from modules.video_generator import VideoGenerator

# Initialize colorama
init(autoreset=True)


class VideoGenerationApp:
    """Main application for AI-powered video generation"""
    
    def __init__(self, config_path: str = 'config.yaml'):
        """
        Initialize the application
        
        Args:
            config_path: Path to configuration file
        """
        self.config = self.load_config(config_path)
        self.pdf_processor = None
        self.tts_engine = None
        self.video_generator = None
    
    def load_config(self, config_path: str) -> dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"{Fore.YELLOW}Warning: Could not load config file. Using defaults. {e}")
            return self.get_default_config()
    
    def get_default_config(self) -> dict:
        """Get default configuration"""
        return {
            'video': {
                'fps': 30,
                'resolution': [1920, 1080],
                'default_duration': 5,
                'transition_duration': 1,
                'background_color': [255, 255, 255],
                'text_color': [0, 0, 0]
            },
            'tts': {
                'default_language': 'ar',
                'voice_rate': 1.0
            },
            'pdf': {
                'max_chars_per_slide': 300
            }
        }
    
    def process_pdf(self, pdf_path: str) -> list:
        """
        Process PDF and extract text chunks
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            List of text chunks
        """
        print(f"{Fore.CYAN}📄 Processing PDF: {pdf_path}")
        
        self.pdf_processor = PDFProcessor(pdf_path)
        
        # Get metadata
        metadata = self.pdf_processor.get_metadata()
        print(f"{Fore.GREEN}✓ PDF loaded: {metadata['filename']}")
        print(f"  Pages: {metadata['total_pages']}")
        
        # Extract and split text
        max_chars = self.config['pdf'].get('max_chars_per_slide', 300)
        text_chunks = self.pdf_processor.split_into_chunks(max_chars)
        
        print(f"{Fore.GREEN}✓ Extracted {len(text_chunks)} text segments")
        
        return text_chunks
    
    def generate_audio(self, text_chunks: list, language: str = None) -> list:
        """
        Generate audio files from text chunks
        
        Args:
            text_chunks: List of text strings
            language: Language code (ar or en)
            
        Returns:
            List of audio file paths
        """
        print(f"\n{Fore.CYAN}🎤 Generating speech...")
        
        if language is None:
            language = self.config['tts'].get('default_language', 'ar')
        
        self.tts_engine = TextToSpeech(
            language=language,
            voice_rate=self.config['tts'].get('voice_rate', 1.0)
        )
        
        # Generate audio for each chunk
        audio_files = self.tts_engine.generate_multiple(
            text_chunks,
            prefix='segment',
            use_edge=True
        )
        
        print(f"{Fore.GREEN}✓ Generated {len(audio_files)} audio files")
        
        return audio_files
    
    def create_video(self, text_chunks: list, audio_files: list, 
                    output_name: str, title: str = None) -> str:
        """
        Create video from text and audio
        
        Args:
            text_chunks: List of text strings
            audio_files: List of audio file paths
            output_name: Output video filename
            title: Video title
            
        Returns:
            Path to generated video
        """
        print(f"\n{Fore.CYAN}🎬 Creating video...")
        
        self.video_generator = VideoGenerator(self.config['video'])
        
        if title is None:
            title = "فيديو توعوي وتعليمي"  # Default Arabic title
        
        video_path = self.video_generator.generate_video(
            text_chunks=text_chunks,
            audio_files=audio_files,
            output_filename=output_name,
            title=title
        )
        
        return video_path
    
    def run(self, pdf_path: str, output_name: str = None, 
           title: str = None, language: str = None):
        """
        Run the complete video generation pipeline
        
        Args:
            pdf_path: Path to PDF file
            output_name: Output video filename
            title: Video title
            language: Language for TTS
        """
        print(f"{Fore.MAGENTA}{'='*60}")
        print(f"{Fore.MAGENTA}  AI Video Generation Tool")
        print(f"{Fore.MAGENTA}  أداة توليد الفيديوهات بالذكاء الاصطناعي")
        print(f"{Fore.MAGENTA}{'='*60}\n")
        
        try:
            # Step 1: Process PDF
            text_chunks = self.process_pdf(pdf_path)
            
            if not text_chunks:
                print(f"{Fore.RED}Error: No text extracted from PDF")
                return
            
            # Step 2: Generate audio
            audio_files = self.generate_audio(text_chunks, language)
            
            if not audio_files:
                print(f"{Fore.RED}Error: No audio files generated")
                return
            
            # Step 3: Create video
            if output_name is None:
                pdf_name = Path(pdf_path).stem
                output_name = f"{pdf_name}_video.mp4"
            
            video_path = self.create_video(text_chunks, audio_files, 
                                          output_name, title)
            
            if video_path:
                print(f"\n{Fore.GREEN}{'='*60}")
                print(f"{Fore.GREEN}✓ SUCCESS! Video created successfully!")
                print(f"{Fore.GREEN}✓ نجح! تم إنشاء الفيديو بنجاح!")
                print(f"{Fore.GREEN}{'='*60}")
                print(f"\n{Fore.CYAN}📹 Output: {video_path}")
            else:
                print(f"{Fore.RED}Error: Video generation failed")
        
        except Exception as e:
            print(f"{Fore.RED}Error during processing: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='AI Video Generation Tool - Convert PDF to Professional Videos',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py input.pdf
  python main.py input.pdf --output my_video.mp4
  python main.py input.pdf --title "My Awareness Video" --language en
  python main.py input.pdf --title "فيديو توعوي" --language ar

Supported languages: ar (Arabic), en (English)
        """
    )
    
    parser.add_argument('pdf_path', help='Path to PDF file')
    parser.add_argument('-o', '--output', help='Output video filename')
    parser.add_argument('-t', '--title', help='Video title')
    parser.add_argument('-l', '--language', choices=['ar', 'en'], 
                       help='Language for text-to-speech (ar=Arabic, en=English)')
    parser.add_argument('-c', '--config', default='config.yaml',
                       help='Path to configuration file')
    
    args = parser.parse_args()
    
    # Check if PDF exists
    if not os.path.exists(args.pdf_path):
        print(f"{Fore.RED}Error: PDF file not found: {args.pdf_path}")
        sys.exit(1)
    
    # Create and run app
    app = VideoGenerationApp(args.config)
    app.run(
        pdf_path=args.pdf_path,
        output_name=args.output,
        title=args.title,
        language=args.language
    )


if __name__ == '__main__':
    main()
