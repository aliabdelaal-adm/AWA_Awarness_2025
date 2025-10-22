# Usage Guide / دليل الاستخدام

## English

### Basic Usage

1. **Prepare your PDF file**: Place your PDF document in the `uploads/` folder or note its path.

2. **Run the tool**:
   ```bash
   python main.py uploads/your_document.pdf
   ```

3. **Find your video**: The generated video will be in `output/videos/`

### Advanced Usage

#### Custom Output Name
```bash
python main.py input.pdf --output custom_name.mp4
```

#### Set Video Title
```bash
python main.py input.pdf --title "My Educational Video"
```

#### Choose Language
```bash
# Arabic (default)
python main.py input.pdf --language ar

# English
python main.py input.pdf --language en
```

#### Combine All Options
```bash
python main.py uploads/guide.pdf \
  --output awareness_video.mp4 \
  --title "Health Awareness Guide" \
  --language ar
```

### Configuration Options

Edit `config.yaml` to customize:

#### Video Settings
- `fps`: Frame rate (default: 30)
- `resolution`: Video dimensions (default: [1920, 1080])
- `default_duration`: Seconds per slide (default: 5)
- `transition_duration`: Transition effect length (default: 1)

#### Text-to-Speech Settings
- `default_language`: ar or en (default: ar)
- `voice_rate`: Speech speed multiplier (default: 1.0)

#### PDF Processing
- `max_chars_per_slide`: Characters per video segment (default: 300)

### Tips for Best Results

1. **PDF Quality**: Use PDFs with clear, extractable text
2. **Content Length**: Keep sections concise for better video flow
3. **Language**: Match the language setting to your PDF content
4. **File Names**: Use descriptive names for easy organization

---

## العربية

### الاستخدام الأساسي

1. **جهز ملف PDF**: ضع مستند PDF في مجلد `uploads/` أو لاحظ مساره.

2. **شغّل الأداة**:
   ```bash
   python main.py uploads/المستند.pdf
   ```

3. **ابحث عن الفيديو**: سيكون الفيديو المُولَّد في `output/videos/`

### الاستخدام المتقدم

#### اسم مخصص للناتج
```bash
python main.py input.pdf --output اسم_مخصص.mp4
```

#### تعيين عنوان الفيديو
```bash
python main.py input.pdf --title "فيديو تعليمي"
```

#### اختيار اللغة
```bash
# العربية (افتراضي)
python main.py input.pdf --language ar

# الإنجليزية
python main.py input.pdf --language en
```

#### دمج جميع الخيارات
```bash
python main.py uploads/دليل.pdf \
  --output فيديو_توعوي.mp4 \
  --title "دليل التوعية الصحية" \
  --language ar
```

### خيارات التكوين

عدّل `config.yaml` للتخصيص:

#### إعدادات الفيديو
- `fps`: معدل الإطارات (افتراضي: 30)
- `resolution`: أبعاد الفيديو (افتراضي: [1920, 1080])
- `default_duration`: ثواني لكل شريحة (افتراضي: 5)
- `transition_duration`: طول تأثير الانتقال (افتراضي: 1)

#### إعدادات تحويل النص لكلام
- `default_language`: ar أو en (افتراضي: ar)
- `voice_rate`: معامل سرعة الكلام (افتراضي: 1.0)

#### معالجة PDF
- `max_chars_per_slide`: عدد الأحرف لكل جزء فيديو (افتراضي: 300)

### نصائح لأفضل النتائج

1. **جودة PDF**: استخدم ملفات PDF بنص واضح وقابل للاستخراج
2. **طول المحتوى**: اجعل الأقسام موجزة لتدفق فيديو أفضل
3. **اللغة**: طابق إعداد اللغة مع محتوى PDF
4. **أسماء الملفات**: استخدم أسماء وصفية لسهولة التنظيم

---

## Examples / أمثلة

### Example 1: Marketing Video
```bash
python main.py product_catalog.pdf \
  --output product_video.mp4 \
  --title "New Product Launch 2025" \
  --language en
```

### Example 2: Educational Content (Arabic)
```bash
python main.py درس_الرياضيات.pdf \
  --output درس_فيديو.mp4 \
  --title "شرح الرياضيات - الصف الثالث" \
  --language ar
```

### Example 3: Awareness Campaign
```bash
python main.py health_guidelines.pdf \
  --output health_awareness.mp4 \
  --title "دليل الصحة العامة" \
  --language ar
```

---

## Troubleshooting / حل المشاكل

### Common Issues / المشاكل الشائعة

**Problem**: "PDF file not found"
**Solution**: Check the file path and ensure the PDF exists

**مشكلة**: "ملف PDF غير موجود"
**الحل**: تحقق من مسار الملف وتأكد من وجود PDF

---

**Problem**: Audio generation is slow
**Solution**: Check your internet connection (required for Edge TTS)

**مشكلة**: توليد الصوت بطيء
**الحل**: تحقق من اتصال الإنترنت (مطلوب لـ Edge TTS)

---

**Problem**: Video encoding fails
**Solution**: Ensure FFmpeg is installed and in your system PATH

**مشكلة**: فشل ترميز الفيديو
**الحل**: تأكد من تثبيت FFmpeg وإضافته لمسار النظام

---

For more help, visit: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues
