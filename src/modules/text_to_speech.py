"""
Text-to-Speech Module
Converts text to speech using AI TTS engines
"""

from gtts import gTTS
import os
from typing import Optional
import edge_tts
import asyncio


class TextToSpeech:
    """Convert text to speech using various TTS engines"""
    
    def __init__(self, language: str = 'ar', voice_rate: float = 1.0):
        """
        Initialize TTS engine
        
        Args:
            language: Language code (ar for Arabic, en for English)
            voice_rate: Speech rate multiplier
        """
        self.language = language
        self.voice_rate = voice_rate
        self.output_dir = "output/audio"
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def generate_speech_gtts(self, text: str, output_filename: str) -> str:
        """
        Generate speech using Google TTS
        
        Args:
            text: Text to convert to speech
            output_filename: Output filename (without extension)
            
        Returns:
            Path to generated audio file
        """
        try:
            output_path = os.path.join(self.output_dir, f"{output_filename}.mp3")
            
            tts = gTTS(text=text, lang=self.language, slow=False)
            tts.save(output_path)
            
            print(f"✓ Generated audio: {output_path}")
            return output_path
        
        except Exception as e:
            print(f"Error generating speech with gTTS: {e}")
            return None
    
    async def generate_speech_edge(self, text: str, output_filename: str) -> str:
        """
        Generate speech using Edge TTS (better quality for Arabic)
        
        Args:
            text: Text to convert to speech
            output_filename: Output filename (without extension)
            
        Returns:
            Path to generated audio file
        """
        try:
            output_path = os.path.join(self.output_dir, f"{output_filename}.mp3")
            
            # Select voice based on language
            if self.language == 'ar':
                voice = "ar-EG-SalmaNeural"  # Egyptian Arabic female voice
            else:
                voice = "en-US-JennyNeural"  # US English female voice
            
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(output_path)
            
            print(f"✓ Generated audio: {output_path}")
            return output_path
        
        except Exception as e:
            print(f"Error generating speech with Edge TTS: {e}")
            return None
    
    def generate_speech(self, text: str, output_filename: str, 
                       use_edge: bool = True) -> str:
        """
        Generate speech using preferred TTS engine
        
        Args:
            text: Text to convert to speech
            output_filename: Output filename (without extension)
            use_edge: Use Edge TTS if True, otherwise use gTTS
            
        Returns:
            Path to generated audio file
        """
        if use_edge:
            try:
                return asyncio.run(self.generate_speech_edge(text, output_filename))
            except Exception as e:
                print(f"Edge TTS failed, falling back to gTTS: {e}")
                return self.generate_speech_gtts(text, output_filename)
        else:
            return self.generate_speech_gtts(text, output_filename)
    
    def generate_multiple(self, texts: list, prefix: str = "audio",
                         use_edge: bool = True) -> list:
        """
        Generate multiple audio files from list of texts
        
        Args:
            texts: List of text strings
            prefix: Prefix for output filenames
            use_edge: Use Edge TTS if True, otherwise use gTTS
            
        Returns:
            List of paths to generated audio files
        """
        audio_files = []
        
        for i, text in enumerate(texts):
            filename = f"{prefix}_{i+1:03d}"
            audio_path = self.generate_speech(text, filename, use_edge)
            
            if audio_path:
                audio_files.append(audio_path)
        
        return audio_files
    
    @staticmethod
    def get_audio_duration(audio_path: str) -> float:
        """
        Get duration of audio file in seconds
        
        Args:
            audio_path: Path to audio file
            
        Returns:
            Duration in seconds
        """
        try:
            from pydub import AudioSegment
            audio = AudioSegment.from_file(audio_path)
            return len(audio) / 1000.0  # Convert to seconds
        except Exception as e:
            print(f"Error getting audio duration: {e}")
            return 5.0  # Default duration
