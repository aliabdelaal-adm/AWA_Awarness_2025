#!/usr/bin/env python3
"""
Professional Pet Shop Standards Awareness Video Generator
Creates a world-class, intelligent awareness video from PDF content
"""

import os
import sys
from pathlib import Path
import pdfplumber
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import subprocess
import shutil

# Configuration
VIDEO_SIZE = (1920, 1080)
FPS = 30
OUTPUT_PATH = "output/videos/pet_shop_awareness_professional.mp4"
PDF_PATH = "20230915_PetShopStandards_V1_AR_FINAL.pdf"
FRAMES_DIR = "output/frames"
AUDIO_DIR = "output/audio"

class ProfessionalVideoGenerator:
    """Generate professional awareness videos with AI"""
    
    def __init__(self):
        self.video_size = VIDEO_SIZE
        self.fps = FPS
        self.frames_dir = FRAMES_DIR
        self.audio_dir = AUDIO_DIR
        
        # Create directories
        os.makedirs(self.frames_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)
        
    def extract_key_content(self, pdf_path):
        """Extract the most important content from PDF"""
        print("📄 Extracting key content from PDF...")
        
        key_sections = []
        
        with pdfplumber.open(pdf_path) as pdf:
            # Extract title from first page
            page1_text = pdf.pages[0].extract_text()
            
            # Extract table of contents
            page2_text = pdf.pages[2].extract_text()
            
            # Parse important sections
            sections = [
                {
                    "title": "معايير محلات بيع الحيوانات الأليفة",
                    "subtitle": "والطيور وأسماك الزينة",
                    "duration": 4
                },
                {
                    "title": "دائرة البلديات والنقل",
                    "content": "تعمل على توفير أعلى المعايير العالمية لرعاية الحيوانات",
                    "duration": 5
                },
                {
                    "title": "الأهداف الرئيسية",
                    "content": "• ضمان صحة وسلامة الحيوانات\n• حماية المستهلك\n• تطبيق المعايير العالمية",
                    "duration": 6
                },
                {
                    "title": "مسؤوليات صاحب المحل",
                    "content": "• توفير بيئة آمنة ونظيفة\n• الرعاية الصحية المستمرة\n• التدريب المناسب للموظفين",
                    "duration": 7
                },
                {
                    "title": "معايير النظافة والتطهير",
                    "content": "• التنظيف الفوري اليومي\n• التنظيف العميق الأسبوعي\n• إجراءات التطهير الدورية",
                    "duration": 7
                },
                {
                    "title": "الصحة والسلامة",
                    "content": "• فحوصات بيطرية منتظمة\n• سجلات طبية محدثة\n• بيئة مناسبة لكل نوع",
                    "duration": 6
                },
                {
                    "title": "متطلبات الأقفاص والمساحات",
                    "content": "• مساحات كافية للحركة\n• تهوية مناسبة\n• إضاءة طبيعية",
                    "duration": 6
                },
                {
                    "title": "التغذية والرعاية",
                    "content": "• غذاء متوازن ومياه نظيفة\n• جداول تغذية منتظمة\n• رعاية خاصة حسب النوع",
                    "duration": 6
                },
                {
                    "title": "معايير عالمية لحياة أفضل",
                    "content": "لحماية الحيوانات وضمان رفاهيتها",
                    "duration": 5
                }
            ]
        
        return sections
    
    def generate_voiceover(self, text, output_file):
        """Generate Arabic voiceover using gTTS"""
        print(f"🎤 Generating voiceover: {text[:50]}...")
        
        from gtts import gTTS
        
        # Generate speech using gTTS
        tts = gTTS(text=text, lang='ar', slow=False)
        tts.save(output_file)
        
        return output_file
    
    def create_gradient_background(self, color1, color2, size=VIDEO_SIZE):
        """Create a beautiful gradient background"""
        width, height = size
        img = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(img)
        
        for i in range(height):
            ratio = i / height
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        
        return img
    
    def create_title_frame(self, title, subtitle=""):
        """Create a professional title frame"""
        print(f"🎬 Creating title: {title[:30]}...")
        
        # Gradient background (teal to blue)
        img = self.create_gradient_background((0, 120, 150), (0, 60, 100))
        draw = ImageDraw.Draw(img)
        
        # Add decorative elements
        # Top bar
        draw.rectangle([0, 0, VIDEO_SIZE[0], 8], fill=(255, 255, 255))
        # Bottom bar
        draw.rectangle([0, VIDEO_SIZE[1]-8, VIDEO_SIZE[0], VIDEO_SIZE[1]], fill=(255, 255, 255))
        
        # Try to load a font, fallback to default
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 85)
            subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 55)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
        
        # Draw title (centered)
        # Get text bounding box
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]
        title_x = (VIDEO_SIZE[0] - title_width) // 2
        title_y = VIDEO_SIZE[1] // 2 - title_height // 2 - 50
        
        # Draw text with shadow for better visibility
        shadow_offset = 3
        draw.text((title_x + shadow_offset, title_y + shadow_offset), title, fill=(0, 0, 0, 128), font=title_font)
        draw.text((title_x, title_y), title, fill=(255, 255, 255), font=title_font)
        
        # Draw subtitle if provided
        if subtitle:
            subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
            subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
            subtitle_x = (VIDEO_SIZE[0] - subtitle_width) // 2
            subtitle_y = title_y + title_height + 40
            
            draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle, fill=(0, 0, 0, 128), font=subtitle_font)
            draw.text((subtitle_x, subtitle_y), subtitle, fill=(255, 255, 255), font=subtitle_font)
        
        return img
    
    def create_content_frame(self, title, content):
        """Create a content frame with title and bullet points"""
        print(f"📝 Creating content: {title[:30]}...")
        
        # Gradient background (lighter)
        img = self.create_gradient_background((240, 250, 255), (200, 230, 245))
        draw = ImageDraw.Draw(img)
        
        # Add decorative corner elements
        corner_size = 40
        corner_color = (0, 120, 150)
        # Top left corner
        draw.line([0, corner_size, 0, 0, corner_size, 0], fill=corner_color, width=6)
        # Top right corner  
        draw.line([VIDEO_SIZE[0]-corner_size, 0, VIDEO_SIZE[0], 0, VIDEO_SIZE[0], corner_size], 
                  fill=corner_color, width=6)
        # Bottom left corner
        draw.line([0, VIDEO_SIZE[1]-corner_size, 0, VIDEO_SIZE[1], corner_size, VIDEO_SIZE[1]], 
                  fill=corner_color, width=6)
        # Bottom right corner
        draw.line([VIDEO_SIZE[0]-corner_size, VIDEO_SIZE[1], VIDEO_SIZE[0], VIDEO_SIZE[1], 
                  VIDEO_SIZE[0], VIDEO_SIZE[1]-corner_size], fill=corner_color, width=6)
        
        # Load fonts
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
            content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 45)
        except:
            title_font = ImageFont.load_default()
            content_font = ImageFont.load_default()
        
        # Draw title
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = (VIDEO_SIZE[0] - title_width) // 2
        title_y = 120
        
        draw.text((title_x + 2, title_y + 2), title, fill=(0, 0, 0, 100), font=title_font)
        draw.text((title_x, title_y), title, fill=(0, 88, 122), font=title_font)
        
        # Draw content (bullet points)
        if content:
            y_offset = 350
            lines = content.split('\n')
            for line in lines:
                if line.strip():
                    # Calculate x position for right-to-left text (Arabic)
                    line_bbox = draw.textbbox((0, 0), line, font=content_font)
                    line_width = line_bbox[2] - line_bbox[0]
                    line_x = (VIDEO_SIZE[0] - line_width) // 2
                    
                    draw.text((line_x, y_offset), line, fill=(51, 51, 51), font=content_font)
                    y_offset += 80
        
        return img
    
    def generate_video(self):
        """Generate the complete professional video"""
        print("\n" + "="*60)
        print("🎬 CREATING WORLD-CLASS AWARENESS VIDEO")
        print("="*60 + "\n")
        
        # Extract content
        sections = self.extract_key_content(PDF_PATH)
        
        # Create output directories
        os.makedirs("output/videos", exist_ok=True)
        
        frame_files = []
        audio_files = []
        segment_info = []
        
        # Process each section
        for idx, section in enumerate(sections):
            print(f"\n📽️  Processing section {idx + 1}/{len(sections)}...")
            
            # Create frame image
            if "subtitle" in section:
                frame_img = self.create_title_frame(
                    section["title"],
                    section.get("subtitle", "")
                )
            elif "content" in section:
                frame_img = self.create_content_frame(
                    section["title"],
                    section.get("content", "")
                )
            else:
                frame_img = self.create_title_frame(section["title"])
            
            # Save frame
            frame_path = os.path.join(self.frames_dir, f"frame_{idx:03d}.png")
            frame_img.save(frame_path)
            frame_files.append(frame_path)
            
            # Generate voiceover
            audio_path = os.path.join(self.audio_dir, f"section_{idx:03d}.mp3")
            text_to_speak = section["title"]
            
            if "subtitle" in section:
                text_to_speak += ". " + section["subtitle"]
            
            if "content" in section:
                # Clean content for speech
                content_clean = section["content"].replace("•", "").replace("\n", " ")
                text_to_speak += ". " + content_clean
            
            self.generate_voiceover(text_to_speak, audio_path)
            audio_files.append(audio_path)
            
            # Get audio duration using ffprobe
            try:
                result = subprocess.run(
                    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', 
                     '-of', 'default=noprint_wrappers=1:nokey=1', audio_path],
                    capture_output=True, text=True, check=True
                )
                duration = float(result.stdout.strip())
            except:
                duration = section.get("duration", 5)
            
            segment_info.append({
                'frame': frame_path,
                'audio': audio_path,
                'duration': duration
            })
        
        # Create video using FFmpeg
        print("\n🎞️  Assembling final video with FFmpeg...")
        self.assemble_video_ffmpeg(segment_info, OUTPUT_PATH)
        
        print("\n" + "="*60)
        print("✅ VIDEO GENERATION COMPLETE!")
        print(f"📹 Output: {OUTPUT_PATH}")
        print("="*60 + "\n")
        
        return OUTPUT_PATH
    
    def assemble_video_ffmpeg(self, segments, output_path):
        """Assemble video using FFmpeg directly"""
        print("🔧 Using FFmpeg to create video...")
        
        # Create temporary video segments
        temp_videos = []
        
        for idx, seg in enumerate(segments):
            temp_video = os.path.join(self.frames_dir, f"segment_{idx:03d}.mp4")
            
            # Create video from single frame with audio
            cmd = [
                'ffmpeg', '-y',
                '-loop', '1',
                '-i', seg['frame'],
                '-i', seg['audio'],
                '-c:v', 'libx264',
                '-tune', 'stillimage',
                '-c:a', 'aac',
                '-b:a', '192k',
                '-pix_fmt', 'yuv420p',
                '-shortest',
                '-t', str(seg['duration']),
                temp_video
            ]
            
            print(f"  Creating segment {idx + 1}/{len(segments)}...")
            subprocess.run(cmd, check=True, capture_output=True)
            temp_videos.append(temp_video)
        
        # Create concat file for FFmpeg
        concat_file = os.path.join(self.frames_dir, 'concat_list.txt')
        with open(concat_file, 'w') as f:
            for video in temp_videos:
                f.write(f"file '{os.path.abspath(video)}'\n")
        
        # Concatenate all segments
        print("  Concatenating segments...")
        cmd = [
            'ffmpeg', '-y',
            '-f', 'concat',
            '-safe', '0',
            '-i', concat_file,
            '-c', 'copy',
            output_path
        ]
        
        subprocess.run(cmd, check=True, capture_output=True)
        
        print("✅ Video assembly complete!")


def main():
    """Main execution function"""
    generator = ProfessionalVideoGenerator()
    output_path = generator.generate_video()
    print(f"\n🎉 Professional awareness video created successfully!")
    print(f"📁 Location: {output_path}")
    return output_path


if __name__ == "__main__":
    main()
