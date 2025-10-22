"""
PDF Processor Module
Extracts text and images from PDF documents
"""

import PyPDF2
import pdfplumber
from typing import List, Dict, Optional
import os


class PDFProcessor:
    """Process PDF files and extract content"""
    
    def __init__(self, pdf_path: str):
        """
        Initialize PDF processor
        
        Args:
            pdf_path: Path to PDF file
        """
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        self.pdf_path = pdf_path
        self.pages_content = []
        
    def extract_text(self) -> List[Dict[str, any]]:
        """
        Extract text from PDF pages
        
        Returns:
            List of dictionaries containing page content
        """
        pages = []
        
        try:
            with pdfplumber.open(self.pdf_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    
                    if text:
                        pages.append({
                            'page_number': i + 1,
                            'text': text.strip(),
                            'has_images': self._check_for_images(page)
                        })
        except Exception as e:
            print(f"Error extracting text with pdfplumber: {e}")
            # Fallback to PyPDF2
            pages = self._extract_with_pypdf2()
        
        self.pages_content = pages
        return pages
    
    def _extract_with_pypdf2(self) -> List[Dict[str, any]]:
        """Fallback extraction using PyPDF2"""
        pages = []
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                for i, page in enumerate(pdf_reader.pages):
                    text = page.extract_text()
                    
                    if text:
                        pages.append({
                            'page_number': i + 1,
                            'text': text.strip(),
                            'has_images': False
                        })
        except Exception as e:
            print(f"Error extracting text with PyPDF2: {e}")
        
        return pages
    
    def _check_for_images(self, page) -> bool:
        """Check if page contains images"""
        try:
            return len(page.images) > 0
        except:
            return False
    
    def split_into_chunks(self, max_chars: int = 300) -> List[str]:
        """
        Split extracted text into chunks suitable for video slides
        
        Args:
            max_chars: Maximum characters per chunk
            
        Returns:
            List of text chunks
        """
        if not self.pages_content:
            self.extract_text()
        
        chunks = []
        
        for page in self.pages_content:
            text = page['text']
            
            # Split by paragraphs first
            paragraphs = text.split('\n\n')
            
            current_chunk = ""
            
            for para in paragraphs:
                # If adding this paragraph exceeds max_chars, save current chunk
                if len(current_chunk) + len(para) > max_chars and current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = para
                else:
                    current_chunk += "\n\n" + para if current_chunk else para
            
            # Add remaining chunk
            if current_chunk:
                chunks.append(current_chunk.strip())
        
        return chunks
    
    def get_metadata(self) -> Dict[str, any]:
        """
        Get PDF metadata
        
        Returns:
            Dictionary containing PDF metadata
        """
        metadata = {
            'filename': os.path.basename(self.pdf_path),
            'total_pages': 0,
            'total_text': ''
        }
        
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                metadata['total_pages'] = len(pdf_reader.pages)
                
                if pdf_reader.metadata:
                    metadata['title'] = pdf_reader.metadata.get('/Title', '')
                    metadata['author'] = pdf_reader.metadata.get('/Author', '')
                    metadata['subject'] = pdf_reader.metadata.get('/Subject', '')
        except Exception as e:
            print(f"Error extracting metadata: {e}")
        
        return metadata
