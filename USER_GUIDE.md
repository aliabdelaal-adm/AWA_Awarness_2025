# AWA Presentation Design Platform - User Guide
# دليل المستخدم - منصة AWA لتصميم العروض الإحترافية

---

## English Guide

### Introduction

Welcome to the AWA Presentation Design Platform! This powerful web-based tool allows you to create professional presentations in both video and PowerPoint formats from your uploaded files. Simply upload your content, configure your preferences, and generate stunning presentations with a single click.

### Getting Started

#### Step 1: Start the Platform

**On Linux/Mac:**
```bash
./start_platform.sh
```

**On Windows:**
```bash
start_platform.bat
```

**Or directly with Python:**
```bash
python app.py
```

The platform will start and be available at: **http://localhost:5000**

#### Step 2: Access the Platform

Open your web browser and navigate to:
```
http://localhost:5000
```

You'll see the main interface with three sections:
1. Upload Files
2. Presentation Settings
3. Generate Presentation

### Using the Platform

#### Uploading Files

1. **Drag and Drop**: Simply drag your files onto the upload area
2. **Click to Browse**: Click the upload area to open a file browser

**Supported File Types:**
- PDF documents (.pdf)
- Images (.png, .jpg, .jpeg, .gif)
- Text files (.txt)
- Documents (.doc, .docx)
- Spreadsheets (.xlsx, .csv)

**File Size Limit:** Up to 50MB per file

#### Configuring Presentation Settings

1. **Presentation Title**: Enter a descriptive title for your presentation
   - Default: "عرض إحترافي مبتكر" (Arabic) or "Professional Presentation" (English)

2. **Language**: Select the language for text-to-speech (for videos)
   - Arabic (العربية)
   - English (الإنجليزية)

3. **Output Type**: Choose your desired output format
   - **Professional Video**: Generates an MP4 video with AI-powered narration
   - **PowerPoint Presentation**: Generates a .pptx file with professional slides

#### Generating Your Presentation

1. Click the **"Generate Professional Presentation"** button (إعداد العرض الإحترافي)
2. Wait while the platform processes your files (this may take a few minutes)
3. Once complete, a download link will appear
4. Click the download link to save your presentation

### Features

#### Bilingual Interface
- Switch between Arabic and English by clicking the language toggle button (🌐)
- Interface direction automatically adjusts for RTL (Arabic) and LTR (English)

#### Video Generation
- Automatic text extraction from PDFs and documents
- AI-powered text-to-speech conversion
- Professional video slides with smooth transitions
- Natural-sounding Arabic and English voices

#### PowerPoint Generation
- Automatic slide creation from your content
- Professional templates and layouts
- Image integration
- Custom formatting for Arabic and English text

### Tips for Best Results

1. **For Video Presentations:**
   - Use PDFs with clear, extractable text
   - Keep text concise for better narration
   - Combine with images for visual appeal

2. **For PowerPoint Presentations:**
   - Upload multiple files to create comprehensive presentations
   - Mix PDFs, text files, and images for variety
   - Use descriptive titles

3. **General Tips:**
   - Upload files before configuring settings
   - Choose appropriate language for your content
   - Be patient during generation - quality takes time!

### Troubleshooting

**Problem: Files not uploading**
- Check file size (must be under 50MB)
- Verify file type is supported
- Try refreshing the page

**Problem: Generation taking too long**
- Video generation can take 2-5 minutes depending on content length
- PowerPoint generation is usually faster (30-60 seconds)
- Check your internet connection (required for AI text-to-speech)

**Problem: Download link not appearing**
- Check browser console for errors
- Try generating with fewer/smaller files
- Ensure all required dependencies are installed

### Command-Line Alternative

You can also use the command-line interface:

```bash
# Generate video from PDF
python main.py document.pdf --title "My Presentation" --language ar

# Generate with custom output name
python main.py input.pdf --output my_video.mp4 --language en
```

---

## الدليل العربي

### المقدمة

مرحباً بك في منصة AWA لتصميم العروض الإحترافية! هذه الأداة القوية المبنية على الويب تتيح لك إنشاء عروض تقديمية احترافية بصيغة فيديو أو باور بوينت من ملفاتك المرفوعة. ببساطة قم برفع محتواك، اضبط تفضيلاتك، وأنشئ عروضاً مذهلة بنقرة واحدة.

### البدء

#### الخطوة 1: تشغيل المنصة

**على Linux/Mac:**
```bash
./start_platform.sh
```

**على Windows:**
```bash
start_platform.bat
```

**أو مباشرة مع Python:**
```bash
python app.py
```

ستبدأ المنصة وستكون متاحة على: **http://localhost:5000**

#### الخطوة 2: الدخول إلى المنصة

افتح متصفح الويب وانتقل إلى:
```
http://localhost:5000
```

سترى الواجهة الرئيسية مع ثلاثة أقسام:
1. تحميل الملفات
2. إعدادات العرض
3. إنشاء العرض

### استخدام المنصة

#### رفع الملفات

1. **السحب والإفلات**: ببساطة اسحب ملفاتك إلى منطقة الرفع
2. **النقر للتصفح**: انقر على منطقة الرفع لفتح متصفح الملفات

**أنواع الملفات المدعومة:**
- مستندات PDF (.pdf)
- صور (.png, .jpg, .jpeg, .gif)
- ملفات نصية (.txt)
- وثائق (.doc, .docx)
- جداول بيانات (.xlsx, .csv)

**حد حجم الملف:** حتى 50 ميجابايت لكل ملف

#### ضبط إعدادات العرض

1. **عنوان العرض**: أدخل عنواناً وصفياً لعرضك
   - الافتراضي: "عرض إحترافي مبتكر" (العربية) أو "Professional Presentation" (الإنجليزية)

2. **اللغة**: اختر اللغة لتحويل النص إلى كلام (للفيديوهات)
   - العربية
   - الإنجليزية

3. **نوع الإخراج**: اختر صيغة الإخراج المطلوبة
   - **فيديو احترافي**: ينشئ ملف MP4 مع تعليق صوتي بالذكاء الاصطناعي
   - **عرض باور بوينت**: ينشئ ملف .pptx مع شرائح احترافية

#### إنشاء عرضك

1. انقر على زر **"إعداد العرض الإحترافي"**
2. انتظر بينما تعالج المنصة ملفاتك (قد يستغرق هذا بضع دقائق)
3. بمجرد الانتهاء، سيظهر رابط التحميل
4. انقر على رابط التحميل لحفظ عرضك

### المميزات

#### واجهة ثنائية اللغة
- التبديل بين العربية والإنجليزية بالنقر على زر تبديل اللغة (🌐)
- اتجاه الواجهة يتكيف تلقائياً لليمين-يسار (العربية) واليسار-يمين (الإنجليزية)

#### توليد الفيديو
- استخراج نصي تلقائي من PDFs والوثائق
- تحويل النص إلى كلام بالذكاء الاصطناعي
- شرائح فيديو احترافية مع انتقالات سلسة
- أصوات طبيعية بالعربية والإنجليزية

#### إنشاء باور بوينت
- إنشاء شرائح تلقائي من محتواك
- قوالب وتخطيطات احترافية
- دمج الصور
- تنسيق مخصص للنصوص العربية والإنجليزية

### نصائح للحصول على أفضل النتائج

1. **للعروض المرئية (الفيديو):**
   - استخدم ملفات PDF بنص واضح وقابل للاستخراج
   - اجعل النص مختصراً للحصول على سرد أفضل
   - ادمج مع الصور للجاذبية البصرية

2. **لعروض باور بوينت:**
   - ارفع ملفات متعددة لإنشاء عروض شاملة
   - امزج PDFs وملفات نصية وصور للتنوع
   - استخدم عناوين وصفية

3. **نصائح عامة:**
   - ارفع الملفات قبل ضبط الإعدادات
   - اختر اللغة المناسبة لمحتواك
   - كن صبوراً أثناء التوليد - الجودة تستغرق وقتاً!

### حل المشاكل

**المشكلة: الملفات لا ترفع**
- تحقق من حجم الملف (يجب أن يكون أقل من 50 ميجابايت)
- تأكد من أن نوع الملف مدعوم
- جرب تحديث الصفحة

**المشكلة: التوليد يستغرق وقتاً طويلاً**
- توليد الفيديو قد يستغرق 2-5 دقائق حسب طول المحتوى
- توليد باور بوينت عادة أسرع (30-60 ثانية)
- تحقق من اتصال الإنترنت (مطلوب لتحويل النص إلى كلام بالذكاء الاصطناعي)

**المشكلة: رابط التحميل لا يظهر**
- تحقق من وحدة التحكم في المتصفح للأخطاء
- جرب التوليد بملفات أقل/أصغر
- تأكد من تثبيت جميع المكتبات المطلوبة

### البديل بسطر الأوامر

يمكنك أيضاً استخدام واجهة سطر الأوامر:

```bash
# إنشاء فيديو من PDF
python main.py document.pdf --title "عرضي التقديمي" --language ar

# التوليد مع اسم مخصص للإخراج
python main.py input.pdf --output my_video.mp4 --language en
```

---

## Support / الدعم

For questions, issues, or feature requests, please open an issue on GitHub.

للأسئلة أو المشاكل أو طلبات الميزات، الرجاء فتح issue على GitHub.

---

**Made with ❤️ by AWA Awareness Team**
