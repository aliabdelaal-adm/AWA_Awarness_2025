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
- 📊 **PowerPoint Presentations**: Generate professional PowerPoint slides automatically
- 📄 **Word & PDF Reports**: Create formatted professional reports
- 📊 **Excel Spreadsheets**: Generate structured data tables
- 🌍 **Multi-language Support**: Full support for Arabic and English content
- 🎨 **Customizable Templates**: Adjust video style, colors, fonts, and layouts
- ⚡ **Automated Pipeline**: One-command generation from PDF to multiple output formats
- 🔊 **High-Quality Audio**: Natural-sounding voices using Edge TTS technology
- 📊 **Smart Content Segmentation**: Automatically split content into digestible segments
- 🚀 **Easy Launcher**: User-friendly interface to access all features

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

**Launch the Interactive Platform**:
```bash
# Windows
awa_launch.bat

# macOS/Linux
./awa_launch.sh

# Or using Python
python launcher.py
```

**Quick Start - Generate Specific Format**:
```bash
# Generate PowerPoint presentation
python launcher.py input.pdf --format powerpoint --title "My Presentation"

# Generate Word report
python launcher.py input.pdf --format word --title "Professional Report"

# Generate PDF report
python launcher.py input.pdf --format pdf --title "Annual Report"

# Generate Excel file
python launcher.py input.pdf --format excel --title "Data Analysis"

# Generate video
python launcher.py input.pdf --format video --title "Awareness Video" --language ar

# Generate ALL formats at once
python launcher.py input.pdf --format all --title "Complete Package"
```

**Original Video-Only Mode (Still Available)**:
```bash
python main.py path/to/your/document.pdf
```

**With custom options**:
```bash
python main.py input.pdf --output my_video.mp4 --title "My Awareness Video" --language ar
```

**Command-line options**:
- `-f, --format`: Choose output format (powerpoint, word, pdf, excel, video, all)
- `-o, --output`: Specify output video filename (for video mode)
- `-t, --title`: Set content title
- `-l, --language`: Choose language (ar for Arabic, en for English)
- `-c, --config`: Use custom configuration file

### 📁 Project Structure

```
AWA_Awarness_2025/
├── launcher.py              # Main platform launcher (NEW!)
├── awa_launch.sh           # Quick launch script for macOS/Linux (NEW!)
├── awa_launch.bat          # Quick launch script for Windows (NEW!)
├── main.py                 # Video generation entry point
├── config.yaml            # Configuration file
├── requirements.txt       # Python dependencies
├── src/
│   └── modules/
│       ├── pdf_processor.py           # PDF text extraction
│       ├── text_to_speech.py          # TTS engine
│       ├── video_generator.py         # Video creation
│       ├── presentation_generator.py  # PowerPoint generation (NEW!)
│       ├── report_generator.py        # Word/PDF reports (NEW!)
│       └── excel_generator.py         # Excel generation (NEW!)
├── uploads/               # Place your PDF files here
├── output/
│   ├── videos/           # Generated videos
│   ├── presentations/    # PowerPoint files (NEW!)
│   ├── reports/          # Word and PDF reports (NEW!)
│   └── excel/            # Excel files (NEW!)
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

- **Marketing Videos & Presentations**: Convert product brochures to engaging video presentations and PowerPoint slides
- **Educational Content**: Transform study materials into video lessons, presentations, and reports
- **Awareness Campaigns**: Create public awareness videos and professional reports from informational PDFs
- **Training Materials**: Convert training documents to video tutorials, presentations, and reference materials
- **Advertising**: Generate promotional videos, presentations, and marketing reports from content
- **Business Reports**: Create professional Word and PDF reports with Excel data tables
- **Data Analysis**: Generate Excel spreadsheets with structured data from PDF documents

### 🎯 Examples

#### Example 1: Generate Complete Package
```bash
python launcher.py awareness_guide.pdf --format all --title "Health Awareness 2025" --language ar
```
This creates video, PowerPoint, Word report, PDF report, and Excel file!

#### Example 2: PowerPoint Presentation
```bash
python launcher.py product_catalog.pdf --format powerpoint --title "Product Showcase"
```

#### Example 3: Professional Report
```bash
python launcher.py annual_data.pdf --format word --title "Annual Report 2024"
```

#### Example 4: Arabic Awareness Video
```bash
python launcher.py awareness_guide.pdf --format video --title "دليل التوعية الصحية" --language ar
```

#### Example 5: English Marketing Video
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
- 📊 **عروض PowerPoint**: توليد شرائح PowerPoint احترافية تلقائياً
- 📄 **تقارير Word و PDF**: إنشاء تقارير احترافية منسقة
- 📊 **جداول Excel**: توليد جداول بيانات منظمة
- 🌍 **دعم متعدد اللغات**: دعم كامل للمحتوى العربي والإنجليزي
- 🎨 **قوالب قابلة للتخصيص**: ضبط نمط الفيديو والألوان والخطوط والتخطيطات
- ⚡ **مسار عمل آلي**: توليد بأمر واحد من PDF إلى صيغ متعددة
- 🔊 **صوت عالي الجودة**: أصوات طبيعية باستخدام تقنية Edge TTS
- 📊 **تقسيم ذكي للمحتوى**: تقسيم المحتوى تلقائياً إلى أجزاء سهلة الفهم
- 🚀 **أداة إطلاق سهلة**: واجهة سهلة الاستخدام للوصول إلى جميع الميزات

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

**تشغيل المنصة التفاعلية**:
```bash
# ويندوز
awa_launch.bat

# ماك/لينكس
./awa_launch.sh

# أو باستخدام Python
python launcher.py
```

**بدء سريع - توليد صيغة محددة**:
```bash
# توليد عرض PowerPoint
python launcher.py input.pdf --format powerpoint --title "عرضي التقديمي"

# توليد تقرير Word
python launcher.py input.pdf --format word --title "تقرير احترافي"

# توليد تقرير PDF
python launcher.py input.pdf --format pdf --title "التقرير السنوي"

# توليد ملف Excel
python launcher.py input.pdf --format excel --title "تحليل البيانات"

# توليد فيديو
python launcher.py input.pdf --format video --title "فيديو توعوي" --language ar

# توليد جميع الصيغ مرة واحدة
python launcher.py input.pdf --format all --title "الحزمة الكاملة"
```

**وضع الفيديو الأصلي (لا يزال متاحاً)**:
```bash
python main.py path/to/your/document.pdf
```

**مع خيارات مخصصة**:
```bash
python main.py input.pdf --output my_video.mp4 --title "فيديو توعوي" --language ar
```

**خيارات سطر الأوامر**:
- `-f, --format`: اختر صيغة الناتج (powerpoint, word, pdf, excel, video, all)
- `-o, --output`: تحديد اسم ملف الفيديو الناتج (لوضع الفيديو)
- `-t, --title`: تعيين عنوان المحتوى
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

- **فيديوهات وعروض تسويقية**: تحويل كتيبات المنتجات إلى عروض فيديو جذابة وشرائح PowerPoint
- **محتوى تعليمي**: تحويل المواد الدراسية إلى دروس فيديو وعروض تقديمية وتقارير
- **حملات توعية**: إنشاء فيديوهات توعية عامة وتقارير احترافية من ملفات PDF معلوماتية
- **مواد تدريبية**: تحويل وثائق التدريب إلى دروس فيديو تعليمية وعروض تقديمية ومواد مرجعية
- **إعلانات**: توليد فيديوهات ترويجية وعروض تقديمية وتقارير تسويقية من المحتوى
- **تقارير الأعمال**: إنشاء تقارير Word و PDF احترافية مع جداول بيانات Excel
- **تحليل البيانات**: توليد جداول Excel بيانات منظمة من مستندات PDF

### 🎯 أمثلة

#### مثال 1: توليد حزمة كاملة
```bash
python launcher.py دليل_التوعية.pdf --format all --title "التوعية الصحية 2025" --language ar
```
هذا ينشئ فيديو، PowerPoint، تقرير Word، تقرير PDF، وملف Excel!

#### مثال 2: عرض PowerPoint
```bash
python launcher.py كتالوج_المنتجات.pdf --format powerpoint --title "عرض المنتجات"
```

#### مثال 3: تقرير احترافي
```bash
python launcher.py البيانات_السنوية.pdf --format word --title "التقرير السنوي 2024"
```

#### مثال 4: فيديو توعوي بالعربية
```bash
python launcher.py دليل_التوعية.pdf --format video --title "دليل التوعية الصحية" --language ar
```

#### مثال 5: فيديو تسويقي بالإنجليزية
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