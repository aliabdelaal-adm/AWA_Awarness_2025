# 🎬 AWA AI Video Generation Tool
# أداة AWA لتوليد الفيديوهات بالذكاء الاصطناعي

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📖 English Documentation

### Overview

The AWA AI Video Generation Tool is a professional, intelligent AI-powered application that automatically generates high-quality promotional, educational, and awareness videos from PDF documents. The tool leverages cutting-edge AI technologies for text-to-speech conversion and creates cinematic presentations perfect for marketing, advertising, and educational purposes.

### ✨ Key Features

- 📄 **PDF Processing**: Automatically extract and structure content from PDF documents
- 🎤 **AI Text-to-Speech**: Convert text to natural-sounding speech in Arabic and English
- 🎬 **Professional Video Generation**: Create polished video presentations with smooth transitions
- 🌍 **Multi-language Support**: Full support for Arabic and English content
- 🎨 **Customizable Templates**: Adjust video style, colors, fonts, and layouts
- ⚡ **Automated Pipeline**: One-command video generation from PDF to final video
- 🔊 **High-Quality Audio**: Natural-sounding voices using Edge TTS technology
- 📊 **Smart Content Segmentation**: Automatically split content into digestible segments

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

**Generate a video from PDF**:
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
├── main.py                 # Main application entry point
├── config.yaml            # Configuration file
├── requirements.txt       # Python dependencies
├── src/
│   └── modules/
│       ├── pdf_processor.py      # PDF text extraction
│       ├── text_to_speech.py     # TTS engine
│       └── video_generator.py    # Video creation
├── uploads/               # Place your PDF files here
├── output/
│   ├── videos/           # Generated videos
│   └── audio/            # Generated audio files
├── templates/
│   └── video_templates/  # Video templates
└── examples/             # Example files and documentation
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

- **Marketing Videos**: Convert product brochures to engaging video presentations
- **Educational Content**: Transform study materials into video lessons
- **Awareness Campaigns**: Create public awareness videos from informational PDFs
- **Training Materials**: Convert training documents to video tutorials
- **Advertising**: Generate promotional videos from marketing content

### 🎯 Examples

#### Example 1: Arabic Awareness Video
```bash
python main.py awareness_guide.pdf --title "دليل التوعية الصحية" --language ar
```

#### Example 2: English Marketing Video
```bash
python main.py product_brochure.pdf --title "Product Overview" --language en --output marketing_video.mp4
```

### 🔧 Advanced Features

- **Custom Templates**: Modify video templates in `templates/video_templates/`
- **Batch Processing**: Process multiple PDFs using a script
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

أداة AWA لتوليد الفيديوهات بالذكاء الاصطناعي هي تطبيق احترافي وذكي يعمل على توليد فيديوهات دعائية وتعليمية وتوعوية عالية الجودة تلقائياً من مستندات PDF. تستخدم الأداة أحدث تقنيات الذكاء الاصطناعي لتحويل النص إلى كلام وإنشاء عروض سينمائية احترافية مثالية للتسويق والإعلان والأغراض التعليمية.

### ✨ المميزات الرئيسية

- 📄 **معالجة PDF**: استخراج وهيكلة المحتوى تلقائياً من مستندات PDF
- 🎤 **تحويل النص إلى كلام بالذكاء الاصطناعي**: تحويل النص إلى صوت طبيعي بالعربية والإنجليزية
- 🎬 **توليد فيديو احترافي**: إنشاء عروض فيديو مصقولة مع انتقالات سلسة
- 🌍 **دعم متعدد اللغات**: دعم كامل للمحتوى العربي والإنجليزي
- 🎨 **قوالب قابلة للتخصيص**: ضبط نمط الفيديو والألوان والخطوط والتخطيطات
- ⚡ **مسار عمل آلي**: توليد الفيديو بأمر واحد من PDF إلى الفيديو النهائي
- 🔊 **صوت عالي الجودة**: أصوات طبيعية باستخدام تقنية Edge TTS
- 📊 **تقسيم ذكي للمحتوى**: تقسيم المحتوى تلقائياً إلى أجزاء سهلة الفهم

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

**توليد فيديو من PDF**:
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

- **فيديوهات تسويقية**: تحويل كتيبات المنتجات إلى عروض فيديو جذابة
- **محتوى تعليمي**: تحويل المواد الدراسية إلى دروس فيديو
- **حملات توعية**: إنشاء فيديوهات توعية عامة من ملفات PDF معلوماتية
- **مواد تدريبية**: تحويل وثائق التدريب إلى دروس فيديو تعليمية
- **إعلانات**: توليد فيديوهات ترويجية من محتوى تسويقي

### 🎯 أمثلة

#### مثال 1: فيديو توعوي بالعربية
```bash
python main.py دليل_التوعية.pdf --title "دليل التوعية الصحية" --language ar
```

#### مثال 2: فيديو تسويقي بالإنجليزية
```bash
python main.py product_brochure.pdf --title "Product Overview" --language en --output marketing_video.mp4
```

### 🔧 الميزات المتقدمة

- **قوالب مخصصة**: تعديل قوالب الفيديو في `templates/video_templates/`
- **معالجة جماعية**: معالجة عدة ملفات PDF باستخدام سكريبت
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