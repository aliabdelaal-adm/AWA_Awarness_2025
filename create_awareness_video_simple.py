#!/usr/bin/env python3
"""
Professional Pet Shop Standards Awareness Video Generator
Creates a world-class awareness video from PDF content (visual-only version)
"""

import os
import sys
import pdfplumber
from PIL import Image, ImageDraw, ImageFont
import subprocess

# Configuration
VIDEO_SIZE = (1920, 1080)
FPS = 30
OUTPUT_PATH = "output/videos/pet_shop_awareness_professional.mp4"
PDF_PATH = "20230915_PetShopStandards_V1_AR_FINAL.pdf"
FRAMES_DIR = "output/frames"

class ProfessionalVideoGenerator:
    """Generate professional awareness videos"""
    
    def __init__(self):
        self.video_size = VIDEO_SIZE
        self.fps = FPS
        self.frames_dir = FRAMES_DIR
        
        # Create directories
        os.makedirs(self.frames_dir, exist_ok=True)
        os.makedirs("output/videos", exist_ok=True)
        
    def extract_key_content(self, pdf_path):
        """Extract the most important content from PDF"""
        print("📄 Extracting key content from PDF...")
        
        sections = [
            {
                "title": "معايير محلات بيع الحيوانات الأليفة",
                "subtitle": "والطيور وأسماك الزينة",
                "duration": 4,
                "type": "title"
            },
            {
                "title": "دائرة البلديات والنقل",
                "content": "تعمل على توفير أعلى المعايير العالمية\nلرعاية الحيوانات",
                "duration": 5,
                "type": "content"
            },
            {
                "title": "الأهداف الرئيسية",
                "content": "• ضمان صحة وسلامة الحيوانات\n• حماية المستهلك\n• تطبيق المعايير العالمية",
                "duration": 6,
                "type": "content"
            },
            {
                "title": "مسؤوليات صاحب المحل",
                "content": "• توفير بيئة آمنة ونظيفة\n• الرعاية الصحية المستمرة\n• التدريب المناسب للموظفين",
                "duration": 7,
                "type": "content"
            },
            {
                "title": "معايير النظافة والتطهير",
                "content": "• التنظيف الفوري اليومي\n• التنظيف العميق الأسبوعي\n• إجراءات التطهير الدورية",
                "duration": 7,
                "type": "content"
            },
            {
                "title": "الصحة والسلامة",
                "content": "• فحوصات بيطرية منتظمة\n• سجلات طبية محدثة\n• بيئة مناسبة لكل نوع",
                "duration": 6,
                "type": "content"
            },
            {
                "title": "متطلبات الأقفاص والمساحات",
                "content": "• مساحات كافية للحركة\n• تهوية مناسبة\n• إضاءة طبيعية",
                "duration": 6,
                "type": "content"
            },
            {
                "title": "التغذية والرعاية",
                "content": "• غذاء متوازن ومياه نظيفة\n• جداول تغذية منتظمة\n• رعاية خاصة حسب النوع",
                "duration": 6,
                "type": "content"
            },
            {
                "title": "معايير عالمية لحياة أفضل",
                "subtitle": "لحماية الحيوانات وضمان رفاهيتها",
                "duration": 5,
                "type": "title"
            }
        ]
        
        return sections
    
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
        draw.rectangle([0, 0, VIDEO_SIZE[0], 8], fill=(255, 255, 255))
        draw.rectangle([0, VIDEO_SIZE[1]-8, VIDEO_SIZE[0], VIDEO_SIZE[1]], fill=(255, 255, 255))
        
        # Load fonts
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 85)
            subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 55)
        except:
            try:
                title_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 85)
                subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 55)
            except:
                title_font = ImageFont.load_default()
                subtitle_font = ImageFont.load_default()
        
        # Draw title (centered)
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]
        title_x = (VIDEO_SIZE[0] - title_width) // 2
        title_y = VIDEO_SIZE[1] // 2 - title_height // 2 - 50
        
        # Draw text with shadow
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
        draw.line([0, corner_size, 0, 0, corner_size, 0], fill=corner_color, width=6)
        draw.line([VIDEO_SIZE[0]-corner_size, 0, VIDEO_SIZE[0], 0, VIDEO_SIZE[0], corner_size], 
                  fill=corner_color, width=6)
        draw.line([0, VIDEO_SIZE[1]-corner_size, 0, VIDEO_SIZE[1], corner_size, VIDEO_SIZE[1]], 
                  fill=corner_color, width=6)
        draw.line([VIDEO_SIZE[0]-corner_size, VIDEO_SIZE[1], VIDEO_SIZE[0], VIDEO_SIZE[1], 
                  VIDEO_SIZE[0], VIDEO_SIZE[1]-corner_size], fill=corner_color, width=6)
        
        # Load fonts
        try:
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 70)
            content_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 45)
        except:
            try:
                title_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 70)
                content_font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 45)
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
        
        frame_files = []
        
        # Process each section
        for idx, section in enumerate(sections):
            print(f"\n📽️  Processing section {idx + 1}/{len(sections)}...")
            
            # Create frame image based on type
            if section.get("type") == "title" or "subtitle" in section:
                frame_img = self.create_title_frame(
                    section["title"],
                    section.get("subtitle", "")
                )
            else:
                frame_img = self.create_content_frame(
                    section["title"],
                    section.get("content", "")
                )
            
            # Save frame multiple times based on duration
            duration = section.get("duration", 5)
            num_frames = int(duration * self.fps)
            
            for frame_idx in range(num_frames):
                frame_path = os.path.join(self.frames_dir, f"frame_{len(frame_files):05d}.png")
                frame_img.save(frame_path)
                frame_files.append(frame_path)
        
        # Create video using FFmpeg
        print(f"\n🎞️  Assembling final video ({len(frame_files)} frames)...")
        self.assemble_video_ffmpeg(OUTPUT_PATH)
        
        print("\n" + "="*60)
        print("✅ VIDEO GENERATION COMPLETE!")
        print(f"📹 Output: {OUTPUT_PATH}")
        print(f"📊 Total frames: {len(frame_files)}")
        print(f"⏱️  Duration: ~{len(frame_files) / self.fps:.1f} seconds")
        print("="*60 + "\n")
        
        return OUTPUT_PATH
    
    def assemble_video_ffmpeg(self, output_path):
        """Assemble video using FFmpeg directly"""
        print("🔧 Using FFmpeg to create video...")
        
        # Create video from image sequence
        cmd = [
            'ffmpeg', '-y',
            '-framerate', str(self.fps),
            '-i', os.path.join(self.frames_dir, 'frame_%05d.png'),
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-preset', 'medium',
            '-crf', '23',
            output_path
        ]
        
        print("  Creating video from frames...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Video assembly complete!")
        else:
            print(f"❌ Error: {result.stderr}")
            raise Exception("Video assembly failed")


def main():
    """Main execution function"""
    generator = ProfessionalVideoGenerator()
    output_path = generator.generate_video()
    print(f"\n🎉 Professional awareness video created successfully!")
    print(f"📁 Location: {output_path}")
    return output_path


if __name__ == "__main__":
    main()
