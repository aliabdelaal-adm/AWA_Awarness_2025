# 🎬 AWA Presentation Design Platform
# منصة AWA لتصميم العروض الإحترافية

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Flask](https://img.shields.io/badge/flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)

---

## 📖 English Documentation

### Overview

The AWA Presentation Design Platform is a professional, intelligent web-based application that allows you to design, prepare, and create innovative professional presentations in both video and PowerPoint formats. Upload your images, PDFs, documents, and data files, then generate stunning presentations with a single click. The platform combines cutting-edge AI technologies for text-to-speech conversion with professional presentation design capabilities.

### ✨ Key Features

- 🌐 **Web-Based Interface**: Modern, easy-to-use web platform accessible from any browser
- 📁 **Multi-File Upload**: Upload PDFs, images, text files, and documents
- 🎬 **Dual Output Formats**: Generate both video presentations and PowerPoint files
- 📄 **PDF Processing**: Automatically extract and structure content from PDF documents
- 🎤 **AI Text-to-Speech**: Convert text to natural-sounding speech in Arabic and English
- 🎥 **Professional Video Generation**: Create polished video presentations with smooth transitions
- 📊 **PowerPoint Creation**: Generate professional .pptx presentations with custom layouts
- 🌍 **Multi-language Support**: Full support for Arabic and English content
- 🎨 **Customizable Templates**: Adjust presentation style, colors, fonts, and layouts
- ⚡ **One-Click Generation**: Generate professional presentations with a single button click
- 🔊 **High-Quality Audio**: Natural-sounding voices using Edge TTS technology
- 📷 **Image Support**: Include images in your presentations seamlessly

### 🚀 Quick Start

#### Prerequisites

- Python 3.8 or higher
- pip package manager
- FFmpeg (for video processing)

#### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/aliabdelaal-adm/AWA_Awarness_2025.git
cd AWA_Awarness_2025
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install FFmpeg** (if not already installed):
   - **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)

#### Basic Usage

**Start the Web Platform** (Recommended):
```bash
# Linux/Mac
./start_platform.sh

# Windows
start_platform.bat

# Or directly with Python
python app.py
```

Then open your browser and navigate to: **http://localhost:5000**

**Command-Line Usage** (Alternative):
```bash
python main.py path/to/your/document.pdf
```

**With custom options**:
```bash
python main.py input.pdf --output my_video.mp4 --title "My Awareness Video" --language ar
```

**Command-line options**:
- `-o, --output`: Specify output video filename
- `-t, --title`: Set video title
- `-l, --language`: Choose language (ar for Arabic, en for English)
- `-c, --config`: Use custom configuration file

### 📁 Project Structure

```
AWA_Awarness_2025/
├── app.py                   # Web application entry point
├── main.py                  # Command-line application entry point
├── config.yaml             # Configuration file
├── requirements.txt        # Python dependencies
├── start_platform.sh       # Linux/Mac startup script
├── start_platform.bat      # Windows startup script
├── src/
│   └── modules/
│       ├── pdf_processor.py          # PDF text extraction
│       ├── text_to_speech.py         # TTS engine
│       ├── video_generator.py        # Video creation
│       └── presentation_builder.py   # PowerPoint generation
├── templates/
│   └── index.html          # Web interface
├── uploads/                # Place your files here
├── output/
│   ├── videos/            # Generated videos
│   ├── presentations/     # Generated PowerPoint files
│   └── audio/             # Generated audio files
├── templates/
│   └── video_templates/   # Video templates
└── examples/              # Example files and documentation
```

### ⚙️ Configuration

Edit `config.yaml` to customize:

```yaml
video:
  fps: 30                    # Video frame rate
  resolution: [1920, 1080]   # Video resolution
  default_duration: 5        # Seconds per slide
  transition_duration: 1     # Transition effect duration

tts:
  default_language: "ar"     # Default language (ar/en)
  voice_rate: 1.0           # Speech speed

pdf:
  max_chars_per_slide: 300  # Characters per video segment
```

### 💡 Use Cases

- **Web-Based Presentations**: Create presentations through an easy-to-use web interface
- **Marketing Videos**: Convert product brochures to engaging video presentations
- **PowerPoint Presentations**: Generate professional PowerPoint files from your content
- **Educational Content**: Transform study materials into video lessons or slide presentations
- **Awareness Campaigns**: Create public awareness videos from informational PDFs
- **Training Materials**: Convert training documents to video tutorials or presentation slides
- **Advertising**: Generate promotional videos from marketing content
- **Multi-format Output**: Choose between video or PowerPoint based on your needs

### 🎯 Examples

#### Example 1: Using the Web Platform
1. Run `./start_platform.sh` (or `start_platform.bat` on Windows)
2. Open http://localhost:5000 in your browser
3. Upload your files (PDFs, images, documents)
4. Enter your presentation title
5. Select output type (Video or PowerPoint)
6. Click "إعداد العرض الإحترافي" (Generate Professional Presentation)
7. Download your generated presentation

#### Example 2: Arabic Video via Command Line
```bash
python main.py awareness_guide.pdf --title "دليل التوعية الصحية" --language ar
```

#### Example 3: English Marketing Video via Command Line
```bash
python main.py product_brochure.pdf --title "Product Overview" --language en --output marketing_video.mp4
```

### 🔧 Advanced Features

- **Web Interface**: Modern responsive web UI for easy presentation creation
- **Custom Templates**: Modify video and PowerPoint templates
- **Batch Processing**: Process multiple files in a single presentation
- **Dual Format Output**: Generate both video and PowerPoint presentations
- **Image Integration**: Seamlessly include images in presentations
- **API Integration**: Extend with OpenAI or other AI services for enhanced content

### 📊 System Requirements

- **CPU**: Multi-core processor recommended
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 1GB free space for temporary files
- **Internet**: Required for Edge TTS (can work offline with gTTS)

### 🐛 Troubleshooting

**Issue: Audio generation fails**
- Solution: Check internet connection for Edge TTS, or disable Edge TTS in the code

**Issue: Video encoding errors**
- Solution: Ensure FFmpeg is properly installed and in PATH

**Issue: PDF extraction problems**
- Solution: Ensure PDF is not password-protected and contains extractable text

---

## 📖 التوثيق العربي

### نظرة عامة

منصة AWA لتصميم العروض الإحترافية هي تطبيق ويب احترافي وذكي يتيح لك تصميم وإعداد وإنشاء عروض تقديمية مبتكرة واحترافية بصيغة فيديو أو باور بوينت. قم برفع صورك، ملفات PDF، الوثائق والبيانات، ثم أنشئ عروض تقديمية مذهلة بنقرة واحدة. تجمع المنصة بين أحدث تقنيات الذكاء الاصطناعي لتحويل النص إلى كلام مع قدرات تصميم العروض الاحترافية.

### ✨ المميزات الرئيسية

- 🌐 **واجهة ويب حديثة**: منصة ويب سهلة الاستخدام يمكن الوصول إليها من أي متصفح
- 📁 **رفع ملفات متعددة**: رفع ملفات PDF، صور، نصوص، ووثائق
- 🎬 **صيغتا إخراج**: توليد عروض فيديو وملفات باور بوينت
- 📄 **معالجة PDF**: استخراج وهيكلة المحتوى تلقائياً من مستندات PDF
- 🎤 **تحويل النص إلى كلام بالذكاء الاصطناعي**: تحويل النص إلى صوت طبيعي بالعربية والإنجليزية
- 🎥 **توليد فيديو احترافي**: إنشاء عروض فيديو مصقولة مع انتقالات سلسة
- 📊 **إنشاء عروض باور بوينت**: توليد عروض .pptx احترافية بتخطيطات مخصصة
- 🌍 **دعم متعدد اللغات**: دعم كامل للمحتوى العربي والإنجليزي
- 🎨 **قوالب قابلة للتخصيص**: ضبط نمط العرض والألوان والخطوط والتخطيطات
- ⚡ **توليد بنقرة واحدة**: إنشاء عروض احترافية بضغطة زر واحدة
- 🔊 **صوت عالي الجودة**: أصوات طبيعية باستخدام تقنية Edge TTS
- 📷 **دعم الصور**: إدراج الصور في عروضك بسلاسة

### 🚀 البدء السريع

#### المتطلبات الأساسية

- Python 3.8 أو أحدث
- مدير الحزم pip
- FFmpeg (لمعالجة الفيديو)

#### التثبيت

1. **استنساخ المستودع**:
```bash
git clone https://github.com/aliabdelaal-adm/AWA_Awarness_2025.git
cd AWA_Awarness_2025
```

2. **تثبيت المكتبات المطلوبة**:
```bash
pip install -r requirements.txt
```

3. **تثبيت FFmpeg** (إذا لم يكن مثبتاً):
   - **Ubuntu/Debian**: `sudo apt-get install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Windows**: تحميل من [ffmpeg.org](https://ffmpeg.org/download.html)

#### الاستخدام الأساسي

**بدء منصة الويب** (مستحسن):
```bash
# Linux/Mac
./start_platform.sh

# Windows
start_platform.bat

# أو مباشرة مع Python
python app.py
```

ثم افتح متصفحك وانتقل إلى: **http://localhost:5000**

**الاستخدام من سطر الأوامر** (بديل):
```bash
python main.py path/to/your/document.pdf
```

**مع خيارات مخصصة**:
```bash
python main.py input.pdf --output my_video.mp4 --title "فيديو توعوي" --language ar
```

**خيارات سطر الأوامر**:
- `-o, --output`: تحديد اسم ملف الفيديو الناتج
- `-t, --title`: تعيين عنوان الفيديو
- `-l, --language`: اختيار اللغة (ar للعربية، en للإنجليزية)
- `-c, --config`: استخدام ملف تكوين مخصص

### 📁 هيكل المشروع

```
AWA_Awarness_2025/
├── main.py                 # نقطة الدخول الرئيسية للتطبيق
├── config.yaml            # ملف التكوين
├── requirements.txt       # مكتبات Python المطلوبة
├── src/
│   └── modules/
│       ├── pdf_processor.py      # استخراج النص من PDF
│       ├── text_to_speech.py     # محرك تحويل النص لكلام
│       └── video_generator.py    # إنشاء الفيديو
├── uploads/               # ضع ملفات PDF هنا
├── output/
│   ├── videos/           # الفيديوهات المولدة
│   └── audio/            # ملفات الصوت المولدة
├── templates/
│   └── video_templates/  # قوالب الفيديو
└── examples/             # ملفات الأمثلة والتوثيق
```

### ⚙️ التكوين

عدّل `config.yaml` للتخصيص:

```yaml
video:
  fps: 30                    # معدل إطارات الفيديو
  resolution: [1920, 1080]   # دقة الفيديو
  default_duration: 5        # ثواني لكل شريحة
  transition_duration: 1     # مدة تأثير الانتقال

tts:
  default_language: "ar"     # اللغة الافتراضية (ar/en)
  voice_rate: 1.0           # سرعة الكلام

pdf:
  max_chars_per_slide: 300  # عدد الأحرف لكل جزء فيديو
```

### 💡 حالات الاستخدام

- **عروض تقديمية عبر الويب**: إنشاء عروض من خلال واجهة ويب سهلة الاستخدام
- **فيديوهات تسويقية**: تحويل كتيبات المنتجات إلى عروض فيديو جذابة
- **عروض باور بوينت**: توليد ملفات PowerPoint احترافية من محتواك
- **محتوى تعليمي**: تحويل المواد الدراسية إلى دروس فيديو أو عروض شرائح
- **حملات توعية**: إنشاء فيديوهات توعية عامة من ملفات PDF معلوماتية
- **مواد تدريبية**: تحويل وثائق التدريب إلى دروس فيديو أو شرائح عرض
- **إعلانات**: توليد فيديوهات ترويجية من محتوى تسويقي
- **إخراج متعدد الصيغ**: اختيار بين الفيديو أو باور بوينت حسب احتياجاتك

### 🎯 أمثلة

#### مثال 1: استخدام منصة الويب
1. شغّل `./start_platform.sh` (أو `start_platform.bat` على Windows)
2. افتح http://localhost:5000 في المتصفح
3. ارفع ملفاتك (PDFs، صور، وثائق)
4. أدخل عنوان العرض
5. اختر نوع الإخراج (فيديو أو باور بوينت)
6. انقر "إعداد العرض الإحترافي"
7. حمّل عرضك المُنشأ

#### مثال 2: فيديو توعوي بالعربية عبر سطر الأوامر
```bash
python main.py دليل_التوعية.pdf --title "دليل التوعية الصحية" --language ar
```

#### مثال 3: فيديو تسويقي بالإنجليزية عبر سطر الأوامر
```bash
python main.py product_brochure.pdf --title "Product Overview" --language en --output marketing_video.mp4
```

### 🔧 الميزات المتقدمة

- **واجهة ويب**: واجهة ويب حديثة ومتجاوبة لإنشاء العروض بسهولة
- **قوالب مخصصة**: تعديل قوالب الفيديو وباور بوينت
- **معالجة جماعية**: معالجة عدة ملفات في عرض واحد
- **إخراج مزدوج الصيغة**: توليد عروض فيديو وباور بوينت
- **دمج الصور**: إدراج الصور في العروض بسلاسة
- **تكامل API**: التوسع مع OpenAI أو خدمات AI أخرى لتحسين المحتوى

### 📊 متطلبات النظام

- **المعالج**: يُنصح بمعالج متعدد الأنوية
- **الذاكرة**: 4GB كحد أدنى، 8GB مستحسن
- **التخزين**: 1GB مساحة حرة للملفات المؤقتة
- **الإنترنت**: مطلوب لـ Edge TTS (يمكن العمل بدون إنترنت مع gTTS)

### 🐛 حل المشاكل

**مشكلة: فشل توليد الصوت**
- الحل: تحقق من اتصال الإنترنت لـ Edge TTS، أو قم بتعطيل Edge TTS في الكود

**مشكلة: أخطاء ترميز الفيديو**
- الحل: تأكد من تثبيت FFmpeg بشكل صحيح وإضافته لـ PATH

**مشكلة: مشاكل استخراج PDF**
- الحل: تأكد من أن PDF غير محمي بكلمة مرور ويحتوي على نص قابل للاستخراج

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions and support, please open an issue on GitHub.

---

**Made with ❤️ by AWA Awareness Team**