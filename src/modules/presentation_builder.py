"""
Presentation Builder Module
Creates professional PowerPoint presentations
"""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os
from typing import List, Dict, Optional


class PresentationBuilder:
    """Build professional PowerPoint presentations"""
    
    def __init__(self):
        """Initialize presentation builder"""
        self.presentation = None
        
    def create_presentation(self, title: str, slides: List[Dict], 
                          output_path: str, language: str = 'ar') -> str:
        """
        Create a PowerPoint presentation
        
        Args:
            title: Presentation title
            slides: List of slide dictionaries with 'title' and 'content' keys
            output_path: Path to save the presentation
            language: Language code ('ar' or 'en')
            
        Returns:
            Path to created presentation file
        """
        try:
            # Create presentation
            self.presentation = Presentation()
            
            # Set slide size to 16:9
            self.presentation.slide_width = Inches(13.333)
            self.presentation.slide_height = Inches(7.5)
            
            # Create title slide
            self._create_title_slide(title, language)
            
            # Create content slides
            for slide_data in slides:
                if 'image_path' in slide_data:
                    self._create_image_slide(
                        slide_data.get('title', ''),
                        slide_data.get('image_path', ''),
                        slide_data.get('content', '')
                    )
                else:
                    self._create_content_slide(
                        slide_data.get('title', ''),
                        slide_data.get('content', ''),
                        language
                    )
            
            # Save presentation
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            self.presentation.save(output_path)
            
            print(f"✓ PowerPoint presentation created: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"Error creating presentation: {e}")
            return None
    
    def _create_title_slide(self, title: str, language: str = 'ar'):
        """Create title slide"""
        slide_layout = self.presentation.slide_layouts[0]  # Title slide layout
        slide = self.presentation.slides.add_slide(slide_layout)
        
        # Set title
        title_shape = slide.shapes.title
        title_shape.text = title
        
        # Format title
        title_frame = title_shape.text_frame
        title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        title_frame.paragraphs[0].font.size = Pt(54)
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)
        
        # Add subtitle if Arabic
        if language == 'ar' and slide.placeholders:
            try:
                subtitle = slide.placeholders[1]
                subtitle.text = "عرض إحترافي مبتكر"
                subtitle.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
                subtitle.text_frame.paragraphs[0].font.size = Pt(32)
            except:
                pass
        
        # Set background color
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(240, 248, 255)  # Light blue
    
    def _create_content_slide(self, slide_title: str, content: str, language: str = 'ar'):
        """Create content slide with title and text"""
        slide_layout = self.presentation.slide_layouts[1]  # Title and Content layout
        slide = self.presentation.slides.add_slide(slide_layout)
        
        # Set title
        title_shape = slide.shapes.title
        title_shape.text = slide_title
        
        # Format title
        title_frame = title_shape.text_frame
        title_frame.paragraphs[0].font.size = Pt(40)
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].font.color.rgb = RGBColor(0, 51, 102)
        
        if language == 'ar':
            title_frame.paragraphs[0].alignment = PP_ALIGN.RIGHT
        
        # Add content
        if slide.placeholders:
            try:
                content_placeholder = slide.placeholders[1]
                text_frame = content_placeholder.text_frame
                text_frame.clear()
                
                # Split content into paragraphs
                paragraphs = content.split('\n')
                
                for i, para_text in enumerate(paragraphs):
                    if para_text.strip():
                        if i > 0:
                            text_frame.add_paragraph()
                        
                        p = text_frame.paragraphs[-1] if i > 0 else text_frame.paragraphs[0]
                        p.text = para_text.strip()
                        p.font.size = Pt(24)
                        p.level = 0
                        
                        if language == 'ar':
                            p.alignment = PP_ALIGN.RIGHT
                        else:
                            p.alignment = PP_ALIGN.LEFT
            except Exception as e:
                print(f"Error adding content to slide: {e}")
        
        # Set background color
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(255, 255, 255)  # White
    
    def _create_image_slide(self, slide_title: str, image_path: str, caption: str = ''):
        """Create slide with image"""
        slide_layout = self.presentation.slide_layouts[6]  # Blank layout
        slide = self.presentation.slides.add_slide(slide_layout)
        
        # Add title at top
        left = Inches(0.5)
        top = Inches(0.5)
        width = Inches(12.333)
        height = Inches(1)
        
        title_box = slide.shapes.add_textbox(left, top, width, height)
        text_frame = title_box.text_frame
        text_frame.text = slide_title
        
        p = text_frame.paragraphs[0]
        p.font.size = Pt(40)
        p.font.bold = True
        p.font.color.rgb = RGBColor(0, 51, 102)
        p.alignment = PP_ALIGN.CENTER
        
        # Add image
        if os.path.exists(image_path):
            try:
                # Calculate image position and size
                img_left = Inches(1.5)
                img_top = Inches(2)
                img_width = Inches(10.333)
                
                slide.shapes.add_picture(
                    image_path,
                    img_left,
                    img_top,
                    width=img_width
                )
            except Exception as e:
                print(f"Error adding image to slide: {e}")
        
        # Add caption if provided
        if caption:
            caption_left = Inches(0.5)
            caption_top = Inches(6.5)
            caption_width = Inches(12.333)
            caption_height = Inches(0.8)
            
            caption_box = slide.shapes.add_textbox(
                caption_left, caption_top, caption_width, caption_height
            )
            caption_frame = caption_box.text_frame
            caption_frame.text = caption
            
            p = caption_frame.paragraphs[0]
            p.font.size = Pt(18)
            p.alignment = PP_ALIGN.CENTER
        
        # Set background color
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(255, 255, 255)  # White
    
    def add_custom_template(self, template_path: str) -> bool:
        """
        Load a custom PowerPoint template
        
        Args:
            template_path: Path to .pptx template file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if os.path.exists(template_path):
                self.presentation = Presentation(template_path)
                return True
            else:
                print(f"Template not found: {template_path}")
                return False
        except Exception as e:
            print(f"Error loading template: {e}")
            return False
