# Project Summary / ملخص المشروع

## AWA AI Video Generation Tool

### Overview / نظرة عامة

This repository contains a complete, professional AI-powered video generation tool that converts PDF documents into high-quality promotional, educational, and awareness videos with AI-generated voiceovers.

هذا المستودع يحتوي على أداة احترافية وكاملة لتوليد الفيديوهات بالذكاء الاصطناعي تحول مستندات PDF إلى فيديوهات ترويجية وتعليمية وتوعوية عالية الجودة مع تعليق صوتي مُولد بالذكاء الاصطناعي.

---

## Key Features / المميزات الرئيسية

### ✅ Implemented Features / الميزات المُنفذة

1. **PDF Processing** / معالجة PDF
   - Automatic text extraction from PDF documents
   - Smart content segmentation
   - Multi-page support
   - Metadata extraction

2. **AI Text-to-Speech** / تحويل النص لكلام بالذكاء الاصطناعي
   - Multiple TTS engines (gTTS, Edge TTS)
   - Arabic and English language support
   - Natural-sounding voices
   - Adjustable speech rate

3. **Professional Video Generation** / توليد فيديو احترافي
   - HD video output (1920x1080)
   - Smooth transitions and effects
   - Customizable templates
   - Text overlay with proper formatting
   - Audio synchronization

4. **User-Friendly Interface** / واجهة سهلة الاستخدام
   - Command-line interface (CLI)
   - Python library API
   - Configuration via YAML
   - Progress tracking with colored output

5. **Comprehensive Documentation** / توثيق شامل
   - Bilingual documentation (Arabic/English)
   - Usage guide with examples
   - Developer documentation
   - FAQ and troubleshooting
   - Contributing guidelines

---

## Project Structure / هيكل المشروع

```
AWA_Awarness_2025/
├── main.py                          # Main application entry point
├── requirements.txt                 # Python dependencies
├── config.yaml                      # Configuration file
├── .gitignore                       # Git ignore rules
├── LICENSE                          # MIT License
│
├── src/                            # Source code
│   └── modules/
│       ├── pdf_processor.py        # PDF text extraction
│       ├── text_to_speech.py       # TTS engine
│       └── video_generator.py      # Video creation
│
├── uploads/                        # Input PDF files
├── output/                         # Generated files
│   ├── videos/                     # Output videos
│   └── audio/                      # Generated audio
│
├── templates/                      # Video templates
│   └── video_templates/
│       └── templates.yaml          # Template configurations
│
├── examples/                       # Usage examples
│   ├── example_usage.py           # Basic usage
│   └── advanced_usage.py          # Advanced examples
│
├── tests/                          # Test files
│   └── test_basic.py              # Basic structure tests
│
└── docs/                           # Documentation
    ├── README.md                   # Main documentation
    ├── USAGE.md                    # Usage guide
    ├── DEVELOPER.md                # Developer guide
    ├── FAQ.md                      # Frequently asked questions
    └── CONTRIBUTING.md             # Contribution guidelines
```

---

## Technologies Used / التقنيات المستخدمة

### Core Technologies
- **Python 3.8+**: Main programming language
- **MoviePy**: Video editing and generation
- **FFmpeg**: Video encoding
- **gTTS & Edge TTS**: Text-to-speech conversion
- **PyPDF2 & pdfplumber**: PDF processing
- **OpenCV**: Image processing
- **Pillow**: Image manipulation

### Supporting Libraries
- **PyYAML**: Configuration management
- **Colorama**: Terminal colors
- **tqdm**: Progress bars
- **pydub**: Audio processing

---

## Installation / التثبيت

### Quick Install / تثبيت سريع

```bash
# Clone repository
git clone https://github.com/aliabdelaal-adm/AWA_Awarness_2025.git
cd AWA_Awarness_2025

# Install dependencies
pip install -r requirements.txt

# Install FFmpeg (Ubuntu/Debian)
sudo apt-get install ffmpeg
```

### Using Installation Scripts / استخدام سكريبتات التثبيت

**Linux/macOS**:
```bash
./install.sh
```

**Windows**:
```cmd
install.bat
```

---

## Usage / الاستخدام

### Basic Usage / الاستخدام الأساسي

```bash
python main.py input.pdf
```

### Advanced Usage / الاستخدام المتقدم

```bash
python main.py document.pdf \
  --output my_video.mp4 \
  --title "فيديو توعوي" \
  --language ar
```

### Quick Start / بداية سريعة

```bash
./quick_start.sh uploads/your_document.pdf
```

---

## Configuration / التكوين

Edit `config.yaml` to customize:

```yaml
video:
  fps: 30
  resolution: [1920, 1080]
  default_duration: 5
  transition_duration: 1

tts:
  default_language: "ar"
  voice_rate: 1.0

pdf:
  max_chars_per_slide: 300
```

---

## Use Cases / حالات الاستخدام

1. **Marketing & Advertising** / التسويق والإعلان
   - Product presentations
   - Service advertisements
   - Brand awareness campaigns

2. **Education** / التعليم
   - Educational videos
   - Training materials
   - Tutorial content

3. **Public Awareness** / التوعية العامة
   - Health awareness campaigns
   - Safety instructions
   - Public service announcements

4. **Corporate Communication** / الاتصالات المؤسسية
   - Internal training
   - Policy announcements
   - Company updates

---

## Documentation / التوثيق

- **README.md**: Main documentation with installation and usage
- **USAGE.md**: Detailed usage guide with examples
- **DEVELOPER.md**: Technical documentation for developers
- **FAQ.md**: Frequently asked questions and troubleshooting
- **CONTRIBUTING.md**: Guidelines for contributing to the project

---

## Security / الأمان

- ✅ Dependencies checked for vulnerabilities
- ✅ Secure by default configuration
- ✅ No hardcoded credentials
- ✅ Input validation implemented
- ✅ MIT License for open source use

**Security Note**: Pillow updated from 10.1.0 to 10.2.0 to address CVE vulnerability.

---

## Future Enhancements / التحسينات المستقبلية

### Planned Features / الميزات المخططة

- [ ] GUI interface for easier use
- [ ] OCR support for scanned PDFs
- [ ] More video templates and styles
- [ ] Support for additional TTS engines
- [ ] Batch processing interface
- [ ] Cloud deployment support
- [ ] Docker containerization
- [ ] Subtitle/caption generation
- [ ] Background music support
- [ ] Advanced video effects

---

## Contributing / المساهمة

We welcome contributions! See `CONTRIBUTING.md` for guidelines.

Areas for contribution:
- Bug fixes
- New features
- Documentation improvements
- Translation to other languages
- Performance optimizations
- Test coverage

---

## License / الترخيص

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Acknowledgments / الشكر والتقدير

- gTTS and Edge TTS for text-to-speech capabilities
- MoviePy for video processing
- PyPDF2 and pdfplumber for PDF handling
- All open-source contributors

---

## Support / الدعم

- **GitHub Issues**: Report bugs and request features
- **Documentation**: Comprehensive guides in Arabic and English
- **Examples**: Multiple usage examples provided

---

## Project Status / حالة المشروع

✅ **Complete and Ready to Use** / مكتمل وجاهز للاستخدام

The tool is fully functional with:
- Core features implemented
- Comprehensive documentation
- Security vulnerabilities addressed
- Examples and usage guides
- Bilingual support (Arabic/English)

---

**Version**: 1.0.0
**Last Updated**: 2025-10-22
**Maintained By**: AWA Awareness Team
