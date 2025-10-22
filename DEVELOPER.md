# Developer Guide / دليل المطورين

## English

### Architecture Overview

The AWA Video Generation Tool is structured in a modular architecture:

```
AWA_Awarness_2025/
├── main.py                          # Application entry point and CLI
├── src/
│   └── modules/
│       ├── pdf_processor.py         # PDF text extraction logic
│       ├── text_to_speech.py        # TTS conversion engines
│       └── video_generator.py       # Video creation with MoviePy
├── config.yaml                      # Configuration management
├── templates/video_templates/       # Video style templates
└── output/                          # Generated files
```

### Core Modules

#### 1. PDFProcessor (`pdf_processor.py`)

**Purpose**: Extract and structure text content from PDF documents

**Key Classes**:
- `PDFProcessor`: Main class for PDF operations

**Key Methods**:
- `extract_text()`: Extract text from all pages
- `split_into_chunks(max_chars)`: Split text into video segments
- `get_metadata()`: Get PDF metadata

**Usage Example**:
```python
from modules.pdf_processor import PDFProcessor

processor = PDFProcessor("document.pdf")
chunks = processor.split_into_chunks(300)
```

#### 2. TextToSpeech (`text_to_speech.py`)

**Purpose**: Convert text to speech using AI TTS engines

**Key Classes**:
- `TextToSpeech`: TTS engine manager

**Supported Engines**:
- Google TTS (gTTS): Fast, works offline after initial download
- Edge TTS: Higher quality, better Arabic support, requires internet

**Key Methods**:
- `generate_speech(text, filename, use_edge)`: Generate single audio
- `generate_multiple(texts, prefix)`: Batch audio generation
- `get_audio_duration(audio_path)`: Get audio length

**Usage Example**:
```python
from modules.text_to_speech import TextToSpeech

tts = TextToSpeech(language='ar')
audio_path = tts.generate_speech("مرحبا", "greeting")
```

#### 3. VideoGenerator (`video_generator.py`)

**Purpose**: Create professional video presentations

**Key Classes**:
- `VideoGenerator`: Video creation manager

**Key Methods**:
- `create_text_slide(text, duration)`: Create single slide
- `create_gradient_background(duration)`: Create gradient backgrounds
- `generate_video(text_chunks, audio_files, output_filename)`: Complete video

**Usage Example**:
```python
from modules.video_generator import VideoGenerator

generator = VideoGenerator(config)
video = generator.generate_video(texts, audios, "output.mp4", "Title")
```

### Pipeline Flow

1. **PDF Processing**:
   - Load PDF file
   - Extract text from all pages
   - Split into manageable chunks (300 chars default)

2. **Audio Generation**:
   - For each text chunk:
     - Convert to speech using Edge TTS or gTTS
     - Save as MP3 file
     - Calculate duration

3. **Video Creation**:
   - Create title slide
   - For each text chunk:
     - Create visual slide with text
     - Synchronize with audio
     - Add transitions
   - Concatenate all slides
   - Encode final video

### Configuration System

Edit `config.yaml` to customize behavior:

```yaml
video:
  fps: 30                      # Frame rate
  resolution: [1920, 1080]     # Width x Height
  default_duration: 5          # Seconds per slide
  transition_duration: 1       # Fade duration
  background_color: [255, 255, 255]
  text_color: [0, 0, 0]

tts:
  default_language: "ar"       # ar or en
  voice_rate: 1.0             # Speed multiplier

pdf:
  max_chars_per_slide: 300    # Text per segment
```

### Adding New Features

#### Adding a New TTS Engine

1. Edit `src/modules/text_to_speech.py`
2. Add new method:
```python
def generate_speech_custom(self, text: str, output_filename: str) -> str:
    # Your TTS implementation
    pass
```
3. Update `generate_speech()` to support new engine

#### Adding a New Video Template

1. Edit `templates/video_templates/templates.yaml`
2. Add new template:
```yaml
my_template:
  background:
    type: gradient
    color1: [R, G, B]
    color2: [R, G, B]
  text:
    font: Arial
    size: 48
    color: [R, G, B]
```
3. Update `video_generator.py` to use templates

#### Adding New Transition Effects

In `video_generator.py`, import additional effects:
```python
from moviepy.video.fx import fadein, fadeout, slide_in, slide_out
```

### Testing

Run basic structure tests:
```bash
python3 tests/test_basic.py
```

Create custom tests for your features:
```python
# tests/test_custom.py
import sys
sys.path.insert(0, 'src')

from modules.pdf_processor import PDFProcessor

def test_my_feature():
    # Your test code
    pass
```

### Dependencies

Core dependencies from `requirements.txt`:

- **PDF**: PyPDF2, pdfplumber
- **TTS**: gTTS, edge-tts
- **Video**: moviepy, opencv-python
- **Audio**: pydub
- **Config**: pyyaml

### Troubleshooting Development Issues

**Import errors**:
```python
# Add to script:
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
```

**Video encoding issues**:
- Ensure FFmpeg is installed
- Check codec support: `ffmpeg -codecs | grep h264`

**Audio quality issues**:
- Try different TTS engines
- Adjust voice_rate in config
- Check audio bitrate settings

---

## العربية

### نظرة عامة على البنية

أداة AWA لتوليد الفيديوهات مبنية بهيكل معماري معياري:

### الوحدات الأساسية

#### 1. معالج PDF (`pdf_processor.py`)

**الغرض**: استخراج وهيكلة محتوى النص من مستندات PDF

**الفئات الرئيسية**:
- `PDFProcessor`: الفئة الرئيسية لعمليات PDF

**الوظائف الرئيسية**:
- `extract_text()`: استخراج النص من جميع الصفحات
- `split_into_chunks(max_chars)`: تقسيم النص إلى أجزاء فيديو
- `get_metadata()`: الحصول على بيانات PDF الوصفية

#### 2. تحويل النص لكلام (`text_to_speech.py`)

**الغرض**: تحويل النص إلى كلام باستخدام محركات TTS بالذكاء الاصطناعي

**المحركات المدعومة**:
- Google TTS (gTTS): سريع، يعمل بدون إنترنت بعد التحميل الأولي
- Edge TTS: جودة أعلى، دعم أفضل للعربية، يتطلب إنترنت

#### 3. مولد الفيديو (`video_generator.py`)

**الغرض**: إنشاء عروض فيديو احترافية

### تدفق العمل

1. **معالجة PDF**:
   - تحميل ملف PDF
   - استخراج النص من جميع الصفحات
   - التقسيم إلى أجزاء قابلة للإدارة (300 حرف افتراضياً)

2. **توليد الصوت**:
   - لكل جزء نص:
     - التحويل إلى كلام باستخدام Edge TTS أو gTTS
     - الحفظ كملف MP3
     - حساب المدة

3. **إنشاء الفيديو**:
   - إنشاء شريحة العنوان
   - لكل جزء نص:
     - إنشاء شريحة مرئية مع النص
     - المزامنة مع الصوت
     - إضافة الانتقالات
   - دمج جميع الشرائح
   - ترميز الفيديو النهائي

### إضافة ميزات جديدة

#### إضافة محرك TTS جديد

1. عدّل `src/modules/text_to_speech.py`
2. أضف وظيفة جديدة:
```python
def generate_speech_custom(self, text: str, output_filename: str) -> str:
    # تطبيق TTS الخاص بك
    pass
```

### الاختبار

تشغيل اختبارات البنية الأساسية:
```bash
python3 tests/test_basic.py
```

---

## API Reference

### VideoGenerationApp Class

Main application class that orchestrates the entire pipeline.

**Methods**:

```python
app = VideoGenerationApp(config_path='config.yaml')

# Process PDF
text_chunks = app.process_pdf(pdf_path)

# Generate audio
audio_files = app.generate_audio(text_chunks, language='ar')

# Create video
video_path = app.create_video(text_chunks, audio_files, 
                              'output.mp4', title='Video Title')

# Run complete pipeline
app.run(pdf_path, output_name, title, language)
```

### Command Line Interface

```bash
# Basic usage
python main.py input.pdf

# Advanced usage
python main.py input.pdf \
  --output custom_name.mp4 \
  --title "Video Title" \
  --language ar \
  --config custom_config.yaml
```

---

## Best Practices

1. **PDF Preparation**:
   - Use high-quality PDFs with clear text
   - Avoid scanned PDFs without OCR
   - Keep text well-structured

2. **Performance**:
   - Process large PDFs in batches
   - Use GPU acceleration when available
   - Adjust video resolution for faster processing

3. **Quality**:
   - Use Edge TTS for Arabic content
   - Adjust max_chars_per_slide for better flow
   - Test with different templates

4. **Error Handling**:
   - Always check return values
   - Use try-except blocks
   - Log errors for debugging

---

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

---

## Support

For issues and questions:
- GitHub Issues: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues
- Documentation: See README.md and USAGE.md

