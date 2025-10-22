"""
Video Generator Module
Creates professional videos from text and audio
"""

from moviepy.editor import (
    VideoClip, TextClip, CompositeVideoClip, 
    AudioFileClip, concatenate_videoclips, ImageClip
)
from moviepy.video.fx import fadein, fadeout
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
from typing import List, Tuple, Optional


class VideoGenerator:
    """Generate professional videos from content"""
    
    def __init__(self, config: dict = None):
        """
        Initialize video generator
        
        Args:
            config: Configuration dictionary
        """
        self.config = config or {}
        self.fps = self.config.get('fps', 30)
        self.resolution = tuple(self.config.get('resolution', [1920, 1080]))
        self.bg_color = self.config.get('background_color', [255, 255, 255])
        self.text_color = self.config.get('text_color', [0, 0, 0])
        self.transition_duration = self.config.get('transition_duration', 1)
        
        self.output_dir = "output/videos"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_text_slide(self, text: str, duration: float, 
                         title: Optional[str] = None) -> VideoClip:
        """
        Create a video slide with text
        
        Args:
            text: Main text content
            duration: Duration in seconds
            title: Optional title text
            
        Returns:
            VideoClip object
        """
        width, height = self.resolution
        
        # Create background
        bg_array = np.zeros((height, width, 3), dtype=np.uint8)
        bg_array[:] = self.bg_color
        
        # Create background clip
        bg_clip = ImageClip(bg_array).set_duration(duration)
        
        clips = [bg_clip]
        
        # Add title if provided
        if title:
            try:
                title_clip = TextClip(
                    title,
                    fontsize=self.config.get('title_font_size', 72),
                    color='black',
                    font='Arial-Bold',
                    method='caption',
                    size=(width - 200, None)
                ).set_position(('center', 100)).set_duration(duration)
                
                clips.append(title_clip)
            except Exception as e:
                print(f"Error creating title clip: {e}")
        
        # Add main text
        try:
            # Split text into smaller chunks if too long
            max_chars_per_line = 60
            words = text.split()
            lines = []
            current_line = []
            current_length = 0
            
            for word in words:
                if current_length + len(word) + 1 <= max_chars_per_line:
                    current_line.append(word)
                    current_length += len(word) + 1
                else:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                    current_length = len(word)
            
            if current_line:
                lines.append(' '.join(current_line))
            
            formatted_text = '\n'.join(lines)
            
            text_clip = TextClip(
                formatted_text,
                fontsize=self.config.get('font_size', 48),
                color='black',
                font='Arial',
                method='caption',
                size=(width - 200, None),
                align='center'
            ).set_position('center').set_duration(duration)
            
            clips.append(text_clip)
        except Exception as e:
            print(f"Error creating text clip: {e}")
        
        # Composite all clips
        video = CompositeVideoClip(clips, size=self.resolution)
        
        # Add fade in/out effects
        video = fadein(video, self.transition_duration)
        video = fadeout(video, self.transition_duration)
        
        return video
    
    def create_gradient_background(self, duration: float, 
                                  color1: Tuple[int, int, int] = (41, 128, 185),
                                  color2: Tuple[int, int, int] = (52, 152, 219)) -> VideoClip:
        """
        Create a video clip with gradient background
        
        Args:
            duration: Duration in seconds
            color1: Starting color (RGB)
            color2: Ending color (RGB)
            
        Returns:
            VideoClip with gradient background
        """
        width, height = self.resolution
        
        # Create gradient
        gradient = np.zeros((height, width, 3), dtype=np.uint8)
        for i in range(height):
            ratio = i / height
            gradient[i] = [
                int(color1[0] * (1 - ratio) + color2[0] * ratio),
                int(color1[1] * (1 - ratio) + color2[1] * ratio),
                int(color1[2] * (1 - ratio) + color2[2] * ratio)
            ]
        
        return ImageClip(gradient).set_duration(duration)
    
    def generate_video(self, text_chunks: List[str], audio_files: List[str],
                      output_filename: str, title: str = "عرض توعوي") -> str:
        """
        Generate complete video from text chunks and audio
        
        Args:
            text_chunks: List of text content for each slide
            audio_files: List of audio file paths
            output_filename: Output video filename
            title: Video title
            
        Returns:
            Path to generated video file
        """
        clips = []
        
        # Create title slide
        title_duration = 3
        title_slide = self.create_text_slide(title, title_duration, title)
        clips.append(title_slide)
        
        # Create slides for each text chunk with corresponding audio
        for i, (text, audio_path) in enumerate(zip(text_chunks, audio_files)):
            if os.path.exists(audio_path):
                # Get audio duration
                audio_clip = AudioFileClip(audio_path)
                duration = audio_clip.duration + 1  # Add 1 second padding
                
                # Create video slide
                slide = self.create_text_slide(text, duration)
                
                # Add audio to slide
                slide = slide.set_audio(audio_clip)
                
                clips.append(slide)
            else:
                print(f"Warning: Audio file not found: {audio_path}")
                # Create slide without audio
                slide = self.create_text_slide(text, 5)
                clips.append(slide)
        
        # Concatenate all clips
        final_video = concatenate_videoclips(clips, method="compose")
        
        # Write video file
        output_path = os.path.join(self.output_dir, output_filename)
        
        try:
            final_video.write_videofile(
                output_path,
                fps=self.fps,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                threads=4
            )
            
            print(f"\n✓ Video generated successfully: {output_path}")
            return output_path
        
        except Exception as e:
            print(f"Error generating video: {e}")
            return None
        finally:
            # Clean up
            final_video.close()
            for clip in clips:
                clip.close()
    
    def add_logo(self, video_path: str, logo_path: str, 
                position: str = 'top-right') -> str:
        """
        Add logo watermark to video
        
        Args:
            video_path: Path to video file
            logo_path: Path to logo image
            position: Logo position ('top-right', 'top-left', 'bottom-right', 'bottom-left')
            
        Returns:
            Path to video with logo
        """
        # This is a placeholder for logo functionality
        # Can be implemented if logo file is provided
        return video_path
