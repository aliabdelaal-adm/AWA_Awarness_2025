"""
AWA Presentation Design Platform - Web Application
منصة تصميم العروض الإحترافية AWA
"""

import os
import sys
import json
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

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif', 'txt', 'doc', 'docx', 'xlsx', 'csv'}
NOTES_CHUNK_SIZE = 300  # Maximum characters per chunk for clarification notes

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'videos'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'presentations'), exist_ok=True)

# Load configuration
try:
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
except:
    config = {}


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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
        output_type = data.get('output_type', 'video')  # 'video' or 'powerpoint'
        title = data.get('title', 'عرض إحترافي')
        language = data.get('language', 'ar')
        selected_files = data.get('files', [])
        clarification_notes = data.get('clarification_notes', '')  # New field for additional notes
        
        if not selected_files:
            return jsonify({'error': 'No files selected'}), 400
        
        # Process files and generate presentation
        if output_type == 'video':
            result = generate_video_presentation(selected_files, title, language, clarification_notes)
        else:
            result = generate_powerpoint_presentation(selected_files, title, language, clarification_notes)
        
        return jsonify(result)
    
    except Exception as e:
        # Log the error but don't expose details to user
        print(f"Error in generate_presentation: {e}")
        return jsonify({'error': 'An error occurred during presentation generation. Please try again.'}), 500


def generate_video_presentation(files, title, language, clarification_notes=''):
    """Generate video presentation from files"""
    text_chunks = []
    
    # Add clarification notes as the first chunk if provided
    if clarification_notes and clarification_notes.strip():
        # Sanitize and prepare clarification notes text
        clarification_notes = clarification_notes.strip()
        notes_prefix = "ملاحظات توضيحية: " if language == 'ar' else "Clarification Notes: "
        notes_text = notes_prefix + clarification_notes
        
        # Split into manageable chunks using the configured chunk size
        for i in range(0, len(notes_text), NOTES_CHUNK_SIZE):
            text_chunks.append(notes_text[i:i+NOTES_CHUNK_SIZE])
    
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


def generate_powerpoint_presentation(files, title, language, clarification_notes=''):
    """Generate PowerPoint presentation from files"""
    try:
        presentation_builder = PresentationBuilder()
        
        # Extract content from files
        slides_content = []
        
        # Add clarification notes as the first slide if provided
        if clarification_notes and clarification_notes.strip():
            # Sanitize the notes
            clarification_notes = clarification_notes.strip()
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
                            'title': f'Slide {len(slides_content) + 1}',
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
                                'title': f'Slide {len(slides_content) + 1}',
                                'content': chunk,
                                'source': filename
                            })
                except Exception as e:
                    print(f"Error processing text file {filename}: {e}")
            
            # Process images
            elif filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                slides_content.append({
                    'title': f'Image: {filename}',
                    'content': '',
                    'image_path': filepath,
                    'source': filename
                })
        
        if not slides_content:
            return {'error': 'No content extracted from files'}
        
        # Generate PowerPoint
        output_filename = f"{title.replace(' ', '_')}_presentation.pptx"
        output_path = os.path.join(OUTPUT_FOLDER, 'presentations', output_filename)
        
        pptx_path = presentation_builder.create_presentation(
            title=title,
            slides=slides_content,
            output_path=output_path,
            language=language
        )
        
        if pptx_path:
            return {
                'success': True,
                'output_type': 'powerpoint',
                'output_path': pptx_path,
                'filename': output_filename,
                'download_url': f'/download-pptx/{output_filename}'
            }
        else:
            return {'error': 'Failed to generate PowerPoint'}
    
    except Exception as e:
        return {'error': f'Error generating PowerPoint: {str(e)}'}


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


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'service': 'AWA Presentation Platform'})


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
