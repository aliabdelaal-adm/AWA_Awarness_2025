"""
AWA Presentation Design Platform - Web Application
منصة تصميم العروض الإحترافية AWA
"""

import os
import sys
import json
import html
import re
import time
from pathlib import Path
from flask import Flask, render_template, request, jsonify, send_file, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import yaml
import re

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from modules.pdf_processor import PDFProcessor
from modules.text_to_speech import TextToSpeech
from modules.video_generator import VideoGenerator
from modules.presentation_builder import PresentationBuilder
from modules.excel_generator import ExcelGenerator
from modules.report_generator import ReportGenerator

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'txt', 'doc', 'docx', 'xlsx', 'csv'}
# Maximum characters per chunk for clarification notes when generating video segments.
# This size is chosen to balance between readability and TTS processing efficiency.
# Smaller chunks provide better pacing in video presentations.
NOTES_CHUNK_SIZE = 300
MAX_NOTES_LENGTH = 50000  # Maximum allowed length for clarification notes

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'videos'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'presentations'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'excel'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'reports'), exist_ok=True)

# Load configuration
try:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
except:
    config = {}


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def smart_chunk_text(text, chunk_size=NOTES_CHUNK_SIZE):
    """
    Split text into chunks while trying to preserve sentence boundaries.
    Falls back to word boundaries if sentences are too long.
    Supports both English and Arabic punctuation marks.
    """
    chunks = []
    
    # Try to split by sentences first
    # Includes both English (. ! ?) and Arabic (۔ ؟ !) punctuation
    sentences = re.split(r'([.!?؟۔]\s+|[.!?؟۔]$)', text)
    current_chunk = ""
    
    for i in range(0, len(sentences), 2):
        sentence = sentences[i] if i < len(sentences) else ""
        delimiter = sentences[i + 1] if i + 1 < len(sentences) else ""
        full_sentence = sentence + delimiter
        
        # If adding this sentence would exceed chunk size
        if len(current_chunk) + len(full_sentence) > chunk_size:
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""
            
            # If single sentence is longer than chunk size, split by words
            if len(full_sentence) > chunk_size:
                words = full_sentence.split()
                for word in words:
                    if len(current_chunk) + len(word) + 1 > chunk_size:
                        if current_chunk:
                            chunks.append(current_chunk.strip())
                        current_chunk = word + " "
                    else:
                        current_chunk += word + " "
            else:
                current_chunk = full_sentence
        else:
            current_chunk += full_sentence
    
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    
    return chunks


def safe_join_path(base_dir, filename):
    """Safely join paths preventing directory traversal attacks"""
    # Remove any path separators from filename
    filename = os.path.basename(filename)
    # Remove any potentially dangerous characters
    filename = re.sub(r'[^\w\s\-\.]', '', filename)
    # Create the full path
    filepath = os.path.join(base_dir, filename)
    # Ensure the resulting path is within the base directory
    if not os.path.abspath(filepath).startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid file path")
    return filepath


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_files():
    """Handle file uploads"""
    if 'files' not in request.files:
        return jsonify({'error': 'No files provided'}), 400
    
    files = request.files.getlist('files')
    uploaded_files = []
    
    for file in files:
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            uploaded_files.append({
                'filename': filename,
                'path': filepath,
                'size': os.path.getsize(filepath),
                'type': filename.rsplit('.', 1)[1].lower()
            })
    
    return jsonify({
        'success': True,
        'files': uploaded_files,
        'count': len(uploaded_files)
    })


@app.route('/list-files', methods=['GET'])
def list_files():
    """List all uploaded files"""
    files = []
    
    if os.path.exists(UPLOAD_FOLDER):
        for filename in os.listdir(UPLOAD_FOLDER):
            if filename != '.gitkeep':
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                if os.path.isfile(filepath):
                    files.append({
                        'filename': filename,
                        'path': filepath,
                        'size': os.path.getsize(filepath),
                        'type': filename.rsplit('.', 1)[1].lower() if '.' in filename else 'unknown'
                    })
    
    return jsonify({'files': files})


@app.route('/generate-presentation', methods=['POST'])
def generate_presentation():
    """Generate professional presentation/video"""
    try:
        data = request.json
        output_type = data.get('output_type', 'video')  # 'video', 'powerpoint', 'excel', 'word', 'pdf'
        title = data.get('title', 'عرض إحترافي')
        language = data.get('language', 'ar')
        selected_files = data.get('files', [])
        clarification_notes = data.get('clarification_notes', '')  # New field for additional notes
        
        # Validate and sanitize clarification notes
        if clarification_notes:
            clarification_notes = clarification_notes.strip()
            # Check length limit
            if len(clarification_notes) > MAX_NOTES_LENGTH:
                error_msg = (
                    f'الملاحظات طويلة جداً. الحد الأقصى {MAX_NOTES_LENGTH} حرف' 
                    if language == 'ar' 
                    else f'Clarification notes too long. Maximum {MAX_NOTES_LENGTH} characters allowed.'
                )
                return jsonify({'error': error_msg}), 400
            # Sanitize HTML to prevent XSS attacks
            clarification_notes = html.escape(clarification_notes)

        max_slides = data.get('max_slides', None)  # Optional slide limit
        
        if not selected_files:
            return jsonify({'error': 'No files selected'}), 400
        
        # Process files and generate presentation based on output type
        if output_type == 'video':
            result = generate_video_presentation(selected_files, title, language, clarification_notes)
        elif output_type == 'powerpoint':
            result = generate_powerpoint_presentation(selected_files, title, language, clarification_notes, max_slides)
        elif output_type == 'excel':
            result = generate_excel_output(selected_files, title, language)
        elif output_type == 'word':
            result = generate_word_output(selected_files, title, language)
        elif output_type == 'pdf':
            result = generate_pdf_output(selected_files, title, language)
        else:
            return jsonify({'error': f'Unsupported output type: {output_type}'}), 400
        
        return jsonify(result)
    
    except Exception as e:
        # Log the error but don't expose details to user
        print(f"Error in generate_presentation: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'An error occurred during presentation generation. Please try again.'}), 500


def generate_video_presentation(files, title, language, clarification_notes=''):
    """Generate video presentation from files"""
    text_chunks = []
    
    # Add clarification notes as the first chunk if provided
    # Note: clarification_notes is already sanitized in the route handler
    if clarification_notes:
        notes_prefix = "ملاحظات توضيحية: " if language == 'ar' else "Clarification Notes: "
        notes_text = notes_prefix + clarification_notes
        
        # Use smart chunking to preserve sentence/word boundaries
        text_chunks.extend(smart_chunk_text(notes_text, NOTES_CHUNK_SIZE))
    
    # Extract content from files
    for filename in files:
        try:
            filepath = safe_join_path(UPLOAD_FOLDER, filename)
        except ValueError:
            print(f"Invalid file path: {filename}")
            continue
        
        if not os.path.exists(filepath):
            continue
        
        # Process PDF files
        if filename.lower().endswith('.pdf'):
            try:
                pdf_processor = PDFProcessor(filepath)
                chunks = pdf_processor.split_into_chunks(300)
                text_chunks.extend(chunks)
            except Exception as e:
                print(f"Error processing PDF {filename}: {e}")
        
        # Process text files
        elif filename.lower().endswith('.txt'):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Split into chunks
                    chunks = [content[i:i+300] for i in range(0, len(content), 300)]
                    text_chunks.extend(chunks)
            except Exception as e:
                print(f"Error processing text file {filename}: {e}")
    
    if not text_chunks:
        return {'error': 'No text content extracted from files'}
    
    # Generate audio from text
    tts_engine = TextToSpeech(language=language)
    audio_files = tts_engine.generate_multiple(text_chunks, prefix='presentation', use_edge=True)
    
    if not audio_files:
        return {'error': 'Failed to generate audio'}
    
    # Generate video
    video_generator = VideoGenerator(config.get('video', {}))
    output_filename = f"{title.replace(' ', '_')}_video.mp4"
    video_path = video_generator.generate_video(
        text_chunks=text_chunks,
        audio_files=audio_files,
        output_filename=output_filename,
        title=title
    )
    
    if video_path:
        return {
            'success': True,
            'output_type': 'video',
            'output_path': video_path,
            'filename': output_filename,
            'download_url': f'/download/{output_filename}'
        }
    else:
        return {'error': 'Failed to generate video'}


 copilot/add-index-html-for-awa-platform


 main
def generate_powerpoint_presentation(files, title, language, clarification_notes='', max_slides=None):
    """Generate PowerPoint presentation from files"""
    try:
        presentation_builder = PresentationBuilder()
        
        # Extract content from files
        slides_content = []
        
        # Add clarification notes as the first slide if provided
        # Note: clarification_notes is already sanitized in the route handler
        if clarification_notes:
            notes_title = 'ملاحظات توضيحية' if language == 'ar' else 'Clarification Notes'
            
            slides_content.append({
                'title': notes_title,
                'content': clarification_notes,
                'source': 'user_input'
            })
        
        for filename in files:
            try:
                filepath = safe_join_path(UPLOAD_FOLDER, filename)
            except ValueError:
                print(f"Invalid file path: {filename}")
                continue
            
            if not os.path.exists(filepath):
                continue
            
            # Process PDF files
            if filename.lower().endswith('.pdf'):
                try:
                    pdf_processor = PDFProcessor(filepath)
                    chunks = pdf_processor.split_into_chunks(500)
                    for chunk in chunks:
                        slides_content.append({
                            'title': f'القسم {len(slides_content) + 1}' if language == 'ar' else f'Section {len(slides_content) + 1}',
                            'content': chunk,
                            'source': filename
                        })
                except Exception as e:
                    print(f"Error processing PDF {filename}: {e}")
            
            # Process text files
            elif filename.lower().endswith('.txt'):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        chunks = [content[i:i+500] for i in range(0, len(content), 500)]
                        for chunk in chunks:
                            slides_content.append({
                                'title': f'القسم {len(slides_content) + 1}' if language == 'ar' else f'Section {len(slides_content) + 1}',
                                'content': chunk,
                                'source': filename
                            })
                except Exception as e:
                    print(f"Error processing text file {filename}: {e}")
            
            # Process images
            elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                slides_content.append({
                    'title': f'صورة: {filename}' if language == 'ar' else f'Image: {filename}',
                    'content': '',
                    'image_path': filepath,
                    'source': filename
                })
        
        if not slides_content:
            return {'error': 'No content extracted from files'}
        
        # Generate PowerPoint with max_slides limit
        output_filename = f"{title.replace(' ', '_')}_presentation.pptx"
        output_path = os.path.join(OUTPUT_FOLDER, 'presentations', output_filename)
        
        pptx_path = presentation_builder.create_presentation(
            title=title,
            slides=slides_content,
            output_path=output_path,
            language=language,
            max_slides=max_slides
        )
        
        if pptx_path:
            return {
                'success': True,
                'output_type': 'powerpoint',
                'output_path': pptx_path,
                'filename': output_filename,
                'slides_count': len(slides_content),
                'download_url': f'/download-pptx/{output_filename}'
            }
        else:
            return {'error': 'Failed to generate PowerPoint'}
    
    except Exception as e:
        print(f"Error in generate_powerpoint_presentation: {e}")
        import traceback
        traceback.print_exc()
        return {'error': f'Error generating PowerPoint: {str(e)}'}


def generate_excel_output(files, title, language):
    """Generate Excel spreadsheet from files"""
    try:
        excel_generator = ExcelGenerator()
        
        # Extract content from files
        text_chunks = []
        
        for filename in files:
            try:
                filepath = safe_join_path(UPLOAD_FOLDER, filename)
            except ValueError:
                print(f"Invalid file path: {filename}")
                continue
            
            if not os.path.exists(filepath):
                continue
            
            # Process PDF files
            if filename.lower().endswith('.pdf'):
                try:
                    pdf_processor = PDFProcessor(filepath)
                    chunks = pdf_processor.split_into_chunks(500)
                    text_chunks.extend(chunks)
                except Exception as e:
                    print(f"Error processing PDF {filename}: {e}")
            
            # Process text files
            elif filename.lower().endswith('.txt'):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        chunks = [content[i:i+500] for i in range(0, len(content), 500)]
                        text_chunks.extend(chunks)
                except Exception as e:
                    print(f"Error processing text file {filename}: {e}")
        
        if not text_chunks:
            return {'error': 'No content extracted from files'}
        
        # Generate Excel file
        output_filename = f"{title.replace(' ', '_')}_data.xlsx"
        output_path = os.path.join(OUTPUT_FOLDER, 'excel', output_filename)
        os.makedirs(os.path.join(OUTPUT_FOLDER, 'excel'), exist_ok=True)
        
        excel_path = excel_generator.generate_from_chunks(
            text_chunks=text_chunks,
            title=title,
            output_path=output_path
        )
        
        if excel_path:
            return {
                'success': True,
                'output_type': 'excel',
                'output_path': excel_path,
                'filename': output_filename,
                'download_url': f'/download-excel/{output_filename}'
            }
        else:
            return {'error': 'Failed to generate Excel file'}
    
    except Exception as e:
        print(f"Error in generate_excel_output: {e}")
        import traceback
        traceback.print_exc()
        return {'error': f'Error generating Excel: {str(e)}'}


def generate_word_output(files, title, language):
    """Generate Word document from files"""
    try:
        report_generator = ReportGenerator()
        
        # Extract content from files
        text_chunks = []
        
        for filename in files:
            try:
                filepath = safe_join_path(UPLOAD_FOLDER, filename)
            except ValueError:
                print(f"Invalid file path: {filename}")
                continue
            
            if not os.path.exists(filepath):
                continue
            
            # Process PDF files
            if filename.lower().endswith('.pdf'):
                try:
                    pdf_processor = PDFProcessor(filepath)
                    chunks = pdf_processor.split_into_chunks(500)
                    text_chunks.extend(chunks)
                except Exception as e:
                    print(f"Error processing PDF {filename}: {e}")
            
            # Process text files
            elif filename.lower().endswith('.txt'):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        chunks = [content[i:i+500] for i in range(0, len(content), 500)]
                        text_chunks.extend(chunks)
                except Exception as e:
                    print(f"Error processing text file {filename}: {e}")
        
        if not text_chunks:
            return {'error': 'No content extracted from files'}
        
        # Generate Word document
        output_filename = f"{title.replace(' ', '_')}_report.docx"
        output_path = os.path.join(OUTPUT_FOLDER, 'reports', output_filename)
        
        word_path = report_generator.generate_word_report(
            text_chunks=text_chunks,
            title=title,
            subtitle='تقرير إحترافي' if language == 'ar' else 'Professional Report',
            output_path=output_path
        )
        
        if word_path:
            return {
                'success': True,
                'output_type': 'word',
                'output_path': word_path,
                'filename': output_filename,
                'download_url': f'/download-word/{output_filename}'
            }
        else:
            return {'error': 'Failed to generate Word document'}
    
    except Exception as e:
        print(f"Error in generate_word_output: {e}")
        import traceback
        traceback.print_exc()
        return {'error': f'Error generating Word document: {str(e)}'}


def generate_pdf_output(files, title, language):
    """Generate PDF report from files"""
    try:
        report_generator = ReportGenerator()
        
        # Extract content from files
        text_chunks = []
        
        for filename in files:
            try:
                filepath = safe_join_path(UPLOAD_FOLDER, filename)
            except ValueError:
                print(f"Invalid file path: {filename}")
                continue
            
            if not os.path.exists(filepath):
                continue
            
            # Process PDF files
            if filename.lower().endswith('.pdf'):
                try:
                    pdf_processor = PDFProcessor(filepath)
                    chunks = pdf_processor.split_into_chunks(500)
                    text_chunks.extend(chunks)
                except Exception as e:
                    print(f"Error processing PDF {filename}: {e}")
            
            # Process text files
            elif filename.lower().endswith('.txt'):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        chunks = [content[i:i+500] for i in range(0, len(content), 500)]
                        text_chunks.extend(chunks)
                except Exception as e:
                    print(f"Error processing text file {filename}: {e}")
        
        if not text_chunks:
            return {'error': 'No content extracted from files'}
        
        # Generate PDF report
        output_filename = f"{title.replace(' ', '_')}_report.pdf"
        output_path = os.path.join(OUTPUT_FOLDER, 'reports', output_filename)
        
        pdf_path = report_generator.generate_pdf_report(
            text_chunks=text_chunks,
            title=title,
            subtitle='تقرير إحترافي' if language == 'ar' else 'Professional Report',
            output_path=output_path
        )
        
        if pdf_path:
            return {
                'success': True,
                'output_type': 'pdf',
                'output_path': pdf_path,
                'filename': output_filename,
                'download_url': f'/download-pdf/{output_filename}'
            }
        else:
            return {'error': 'Failed to generate PDF report'}
    
    except Exception as e:
        print(f"Error in generate_pdf_output: {e}")
        import traceback
        traceback.print_exc()
        return {'error': f'Error generating PDF report: {str(e)}'}


@app.route('/download/<filename>')
def download_video(filename):
    """Download generated video"""
    try:
        filepath = safe_join_path(os.path.join(OUTPUT_FOLDER, 'videos'), filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except (ValueError, Exception):
        return jsonify({'error': 'Invalid file path'}), 400


@app.route('/download-pptx/<filename>')
def download_pptx(filename):
    """Download generated PowerPoint"""
    try:
        filepath = safe_join_path(os.path.join(OUTPUT_FOLDER, 'presentations'), filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except (ValueError, Exception):
        return jsonify({'error': 'Invalid file path'}), 400


@app.route('/download-excel/<filename>')
def download_excel(filename):
    """Download generated Excel file"""
    try:
        filepath = safe_join_path(os.path.join(OUTPUT_FOLDER, 'excel'), filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except (ValueError, Exception):
        return jsonify({'error': 'Invalid file path'}), 400


@app.route('/download-word/<filename>')
def download_word(filename):
    """Download generated Word document"""
    try:
        filepath = safe_join_path(os.path.join(OUTPUT_FOLDER, 'reports'), filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except (ValueError, Exception):
        return jsonify({'error': 'Invalid file path'}), 400


@app.route('/download-pdf/<filename>')
def download_pdf(filename):
    """Download generated PDF report"""
    try:
        filepath = safe_join_path(os.path.join(OUTPUT_FOLDER, 'reports'), filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return jsonify({'error': 'File not found'}), 404
    except (ValueError, Exception):
        return jsonify({'error': 'Invalid file path'}), 400


@app.route('/admin')
def admin_dashboard():
    """Admin dashboard for developers and system owners"""
    # Get statistics
    stats = {
        'uploaded_files': 0,
        'videos': 0,
        'presentations': 0,
        'reports': 0,
        'excel_files': 0
    }
    
    # Count uploaded files
    if os.path.exists(UPLOAD_FOLDER):
        stats['uploaded_files'] = len([f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f)) and f != '.gitkeep'])
    
    # Count outputs
    videos_path = os.path.join(OUTPUT_FOLDER, 'videos')
    if os.path.exists(videos_path):
        stats['videos'] = len([f for f in os.listdir(videos_path) if os.path.isfile(os.path.join(videos_path, f)) and f != '.gitkeep'])
    
    presentations_path = os.path.join(OUTPUT_FOLDER, 'presentations')
    if os.path.exists(presentations_path):
        stats['presentations'] = len([f for f in os.listdir(presentations_path) if os.path.isfile(os.path.join(presentations_path, f)) and f != '.gitkeep'])
    
    reports_path = os.path.join(OUTPUT_FOLDER, 'reports')
    if os.path.exists(reports_path):
        stats['reports'] = len([f for f in os.listdir(reports_path) if os.path.isfile(os.path.join(reports_path, f)) and f != '.gitkeep'])
    
    excel_path = os.path.join(OUTPUT_FOLDER, 'excel')
    if os.path.exists(excel_path):
        stats['excel_files'] = len([f for f in os.listdir(excel_path) if os.path.isfile(os.path.join(excel_path, f)) and f != '.gitkeep'])
    
    return render_template('admin.html', stats=stats)


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'AWA Presentation Platform'})


@app.route('/stats')
def get_stats():
    """Get platform statistics"""
    try:
        stats = {
            'total_files': 0,
            'videos_count': 0,
            'presentations_count': 0,
            'reports_count': 0,
            'excel_count': 0,
            'total_size': 0
        }
        
        # Count uploaded files
        if os.path.exists(UPLOAD_FOLDER):
            for filename in os.listdir(UPLOAD_FOLDER):
                if filename != '.gitkeep':
                    filepath = os.path.join(UPLOAD_FOLDER, filename)
                    if os.path.isfile(filepath):
                        stats['total_files'] += 1
                        stats['total_size'] += os.path.getsize(filepath)
        
        # Count videos
        videos_dir = os.path.join(OUTPUT_FOLDER, 'videos')
        if os.path.exists(videos_dir):
            for filename in os.listdir(videos_dir):
                if filename.endswith('.mp4'):
                    stats['videos_count'] += 1
                    filepath = os.path.join(videos_dir, filename)
                    stats['total_size'] += os.path.getsize(filepath)
        
        # Count presentations
        pptx_dir = os.path.join(OUTPUT_FOLDER, 'presentations')
        if os.path.exists(pptx_dir):
            for filename in os.listdir(pptx_dir):
                if filename.endswith('.pptx'):
                    stats['presentations_count'] += 1
                    filepath = os.path.join(pptx_dir, filename)
                    stats['total_size'] += os.path.getsize(filepath)
        
        # Count reports
        reports_dir = os.path.join(OUTPUT_FOLDER, 'reports')
        if os.path.exists(reports_dir):
            for filename in os.listdir(reports_dir):
                if filename.endswith(('.docx', '.pdf')):
                    stats['reports_count'] += 1
                    filepath = os.path.join(reports_dir, filename)
                    stats['total_size'] += os.path.getsize(filepath)
        
        # Count Excel files
        excel_dir = os.path.join(OUTPUT_FOLDER, 'excel')
        if os.path.exists(excel_dir):
            for filename in os.listdir(excel_dir):
                if filename.endswith('.xlsx'):
                    stats['excel_count'] += 1
                    filepath = os.path.join(excel_dir, filename)
                    stats['total_size'] += os.path.getsize(filepath)
        
        return jsonify({'success': True, **stats})
    
    except Exception as e:
        print(f"Error getting stats: {e}")
        return jsonify({'success': False, 'error': 'Failed to retrieve statistics'}), 500


@app.route('/list-outputs')
def list_outputs():
    """List generated output files"""
    try:
        output_type = request.args.get('type', 'videos')
        output_dir = os.path.join(OUTPUT_FOLDER, output_type)
        files = []
        
        if os.path.exists(output_dir):
            for filename in os.listdir(output_dir):
                if filename != '.gitkeep':
                    filepath = os.path.join(output_dir, filename)
                    if os.path.isfile(filepath):
                        files.append({
                            'filename': filename,
                            'type': output_type,
                            'size': os.path.getsize(filepath),
                            'created': os.path.getctime(filepath)
                        })
        
        return jsonify({'success': True, 'files': files})
    
    except Exception as e:
        print(f"Error listing outputs: {e}")
        return jsonify({'success': False, 'error': 'Failed to list output files'}), 500


@app.route('/delete-file', methods=['POST'])
def delete_file():
    """Delete an uploaded file"""
    try:
        data = request.json
        filename = data.get('filename')
        
        if not filename:
            return jsonify({'error': 'No filename provided'}), 400
        
        try:
            filepath = safe_join_path(UPLOAD_FOLDER, filename)
        except ValueError:
            return jsonify({'error': 'Invalid filename'}), 400
        
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'File not found'}), 404
    
    except Exception as e:
        print(f"Error deleting file: {e}")
        return jsonify({'error': 'Failed to delete file'}), 500


@app.route('/delete-all-files', methods=['POST'])
def delete_all_files():
    """Delete all uploaded files"""
    try:
        count = 0
        if os.path.exists(UPLOAD_FOLDER):
            for filename in os.listdir(UPLOAD_FOLDER):
                if filename != '.gitkeep':
                    filepath = os.path.join(UPLOAD_FOLDER, filename)
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                        count += 1
        
        return jsonify({'success': True, 'count': count})
    
    except Exception as e:
        print(f"Error deleting all files: {e}")
        return jsonify({'error': 'Failed to delete all files'}), 500


@app.route('/delete-output', methods=['POST'])
def delete_output():
    """Delete a generated output file"""
    try:
        data = request.json
        output_type = data.get('type')
        filename = data.get('filename')
        
        if not output_type or not filename:
            return jsonify({'error': 'Missing type or filename'}), 400
        
        try:
            filepath = safe_join_path(os.path.join(OUTPUT_FOLDER, output_type), filename)
        except ValueError:
            return jsonify({'error': 'Invalid file path'}), 400
        
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({'success': True})
        else:
            return jsonify({'error': 'File not found'}), 404
    
    except Exception as e:
        print(f"Error deleting output: {e}")
        return jsonify({'error': 'Failed to delete output file'}), 500


@app.route('/delete-all-outputs', methods=['POST'])
def delete_all_outputs():
    """Delete all generated output files"""
    try:
        count = 0
        output_types = ['videos', 'presentations', 'reports', 'excel']
        
        for output_type in output_types:
            output_dir = os.path.join(OUTPUT_FOLDER, output_type)
            if os.path.exists(output_dir):
                for filename in os.listdir(output_dir):
                    if filename != '.gitkeep':
                        filepath = os.path.join(output_dir, filename)
                        if os.path.isfile(filepath):
                            os.remove(filepath)
                            count += 1
        
        return jsonify({'success': True, 'count': count})
    
    except Exception as e:
        print(f"Error deleting all outputs: {e}")
        return jsonify({'error': 'Failed to delete all outputs'}), 500


@app.route('/download-all-files')
def download_all_files():
    """Download all uploaded files as a zip archive"""
    try:
        import zipfile
        import io
        
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            if os.path.exists(UPLOAD_FOLDER):
                for filename in os.listdir(UPLOAD_FOLDER):
                    if filename != '.gitkeep':
                        filepath = os.path.join(UPLOAD_FOLDER, filename)
                        if os.path.isfile(filepath):
                            zip_file.write(filepath, filename)
        
        zip_buffer.seek(0)
        
        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f'awa_uploads_{int(time.time())}.zip'
        )
    
    except Exception as e:
        print(f"Error creating zip: {e}")
        return jsonify({'error': 'Failed to create archive'}), 500


@app.route('/download-all-outputs')
def download_all_outputs():
    """Download all output files as a zip archive"""
    try:
        import zipfile
        import io
        
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            output_types = ['videos', 'presentations', 'reports', 'excel']
            
            for output_type in output_types:
                output_dir = os.path.join(OUTPUT_FOLDER, output_type)
                if os.path.exists(output_dir):
                    for filename in os.listdir(output_dir):
                        if filename != '.gitkeep':
                            filepath = os.path.join(output_dir, filename)
                            if os.path.isfile(filepath):
                                zip_file.write(filepath, f'{output_type}/{filename}')
        
        zip_buffer.seek(0)
        
        return send_file(
            zip_buffer,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f'awa_outputs_{int(time.time())}.zip'
        )
    
    except Exception as e:
        print(f"Error creating zip: {e}")
        return jsonify({'error': 'Failed to create archive'}), 500


@app.route('/save-config', methods=['POST'])
def save_config():
    """Save platform configuration"""
    try:
        new_config = request.json
        
        # Merge with existing config
        if os.path.exists('config.yaml'):
            with open('config.yaml', 'r', encoding='utf-8') as f:
                existing_config = yaml.safe_load(f) or {}
        else:
            existing_config = {}
        
        # Update config
        if 'video' in new_config:
            if 'video' not in existing_config:
                existing_config['video'] = {}
            existing_config['video'].update(new_config['video'])
        
        if 'tts' in new_config:
            if 'tts' not in existing_config:
                existing_config['tts'] = {}
            existing_config['tts'].update(new_config['tts'])
        
        if 'processing' in new_config:
            if 'processing' not in existing_config:
                existing_config['processing'] = {}
            existing_config['processing'].update(new_config['processing'])
        
        # Save to file
        with open('config.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(existing_config, f, default_flow_style=False, allow_unicode=True)
        
        return jsonify({'success': True})
    
    except Exception as e:
        print(f"Error saving config: {e}")
        return jsonify({'error': 'Failed to save configuration'}), 500


if __name__ == '__main__':
    print("="*60)
    print("  AWA Presentation Design Platform")
    print("  منصة تصميم العروض الإحترافية AWA")
    print("="*60)
    print("\nStarting server on http://localhost:5000")
    print("Open your browser and navigate to the URL above")
    print("\nPress Ctrl+C to stop the server")
    print("="*60)
    
    # Get debug mode from environment variable, default to False for security
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    if debug_mode:
        print("\n⚠️  WARNING: Running in DEBUG mode. Do NOT use in production!")
    
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
