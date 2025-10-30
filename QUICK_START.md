# 🚀 AWA Platform Quick Start Guide
# دليل البدء السريع لمنصة AWA

---

## English Version

### What is AWA Platform?

AWA is an **intelligent content generation platform** that automatically converts PDF documents into multiple professional formats:

- 🎬 **Videos** - Promotional and educational videos with AI voice
- 📊 **PowerPoint Presentations** - Professional slides
- 📄 **Word Reports** - Formatted professional documents
- 📑 **PDF Reports** - High-quality PDF documents
- 📊 **Excel Spreadsheets** - Structured data tables

### How to Launch the Platform

#### Method 1: Interactive Mode (Recommended for Beginners)

**Windows:**
```cmd
double-click: awa_launch.bat
```

**macOS/Linux:**
```bash
./awa_launch.sh
```

**Or using Python directly:**
```bash
python launcher.py
```

This will show an interactive menu where you can:
1. Select the type of content you want to generate
2. Choose your PDF file
3. Enter a title
4. Select language (Arabic or English)

#### Method 2: Command-Line Mode (For Advanced Users)

**Generate PowerPoint Presentation:**
```bash
python launcher.py input.pdf --format powerpoint --title "My Presentation"
```

**Generate Word Report:**
```bash
python launcher.py input.pdf --format word --title "Professional Report"
```

**Generate PDF Report:**
```bash
python launcher.py input.pdf --format pdf --title "Annual Report"
```

**Generate Excel File:**
```bash
python launcher.py input.pdf --format excel --title "Data Analysis"
```

**Generate Video:**
```bash
python launcher.py input.pdf --format video --title "Awareness Video" --language ar
```

**Generate ALL Formats at Once:**
```bash
python launcher.py input.pdf --format all --title "Complete Package"
```

### Step-by-Step Tutorial

#### Step 1: Prepare Your PDF
- Place your PDF file in the `uploads/` folder (or note its full path)
- Ensure the PDF contains extractable text (not scanned images)

#### Step 2: Launch the Platform
- Double-click `awa_launch.bat` (Windows) or `awa_launch.sh` (macOS/Linux)
- Or run: `python launcher.py`

#### Step 3: Follow the Interactive Menu
```
1. Video Generation          / توليد فيديو
2. PowerPoint Presentation   / عرض PowerPoint
3. Professional Report (Word)/ تقرير احترافي (Word)
4. PDF Report                / تقرير PDF
5. Excel Spreadsheet         / ملف Excel
6. Generate All Formats      / توليد جميع الصيغ
```

#### Step 4: Provide Information
- **PDF Path**: Enter the full path to your PDF file
- **Title**: Enter a title for your content (optional)
- **Language**: Choose `ar` for Arabic or `en` for English

#### Step 5: Wait for Generation
The platform will process your PDF and generate the selected format(s).

#### Step 6: Find Your Output
Generated files will be in:
- Videos: `output/videos/`
- PowerPoint: `output/presentations/`
- Word Reports: `output/reports/`
- PDF Reports: `output/reports/`
- Excel: `output/excel/`

### Quick Examples

**Example 1: Create a marketing presentation**
```bash
python launcher.py product_catalog.pdf --format powerpoint --title "Product Showcase 2025"
```

**Example 2: Generate an Arabic awareness video**
```bash
python launcher.py health_guide.pdf --format video --title "دليل الصحة" --language ar
```

**Example 3: Create everything from one PDF**
```bash
python launcher.py annual_report.pdf --format all --title "Annual Report 2024"
```

### Tips for Best Results

1. **PDF Quality**: Use PDFs with clear, extractable text
2. **File Names**: Use descriptive names without special characters
3. **Language**: Match the language setting to your PDF content
4. **Content Length**: Shorter, well-structured PDFs work best

---

## النسخة العربية

### ما هي منصة AWA؟

AWA هي **منصة ذكية لتوليد المحتوى** تحول مستندات PDF تلقائياً إلى صيغ احترافية متعددة:

- 🎬 **فيديوهات** - فيديوهات دعائية وتعليمية بصوت ذكاء اصطناعي
- 📊 **عروض PowerPoint** - شرائح احترافية
- 📄 **تقارير Word** - مستندات احترافية منسقة
- 📑 **تقارير PDF** - مستندات PDF عالية الجودة
- 📊 **جداول Excel** - جداول بيانات منظمة

### كيفية فتح المنصة

#### الطريقة 1: الوضع التفاعلي (موصى به للمبتدئين)

**ويندوز:**
```cmd
انقر نقراً مزدوجاً على: awa_launch.bat
```

**ماك/لينكس:**
```bash
./awa_launch.sh
```

**أو استخدام Python مباشرة:**
```bash
python launcher.py
```

سيعرض هذا قائمة تفاعلية حيث يمكنك:
1. اختيار نوع المحتوى الذي تريد توليده
2. اختيار ملف PDF
3. إدخال عنوان
4. اختيار اللغة (العربية أو الإنجليزية)

#### الطريقة 2: وضع سطر الأوامر (للمستخدمين المتقدمين)

**توليد عرض PowerPoint:**
```bash
python launcher.py input.pdf --format powerpoint --title "عرضي التقديمي"
```

**توليد تقرير Word:**
```bash
python launcher.py input.pdf --format word --title "تقرير احترافي"
```

**توليد تقرير PDF:**
```bash
python launcher.py input.pdf --format pdf --title "التقرير السنوي"
```

**توليد ملف Excel:**
```bash
python launcher.py input.pdf --format excel --title "تحليل البيانات"
```

**توليد فيديو:**
```bash
python launcher.py input.pdf --format video --title "فيديو توعوي" --language ar
```

**توليد جميع الصيغ مرة واحدة:**
```bash
python launcher.py input.pdf --format all --title "الحزمة الكاملة"
```

### دليل خطوة بخطوة

#### الخطوة 1: جهز ملف PDF
- ضع ملف PDF في مجلد `uploads/` (أو لاحظ مساره الكامل)
- تأكد من أن PDF يحتوي على نص قابل للاستخراج (وليس صور ممسوحة)

#### الخطوة 2: افتح المنصة
- انقر نقراً مزدوجاً على `awa_launch.bat` (ويندوز) أو `awa_launch.sh` (ماك/لينكس)
- أو نفذ: `python launcher.py`

#### الخطوة 3: اتبع القائمة التفاعلية
```
1. Video Generation          / توليد فيديو
2. PowerPoint Presentation   / عرض PowerPoint
3. Professional Report (Word)/ تقرير احترافي (Word)
4. PDF Report                / تقرير PDF
5. Excel Spreadsheet         / ملف Excel
6. Generate All Formats      / توليد جميع الصيغ
```

#### الخطوة 4: قدم المعلومات
- **مسار PDF**: أدخل المسار الكامل لملف PDF
- **العنوان**: أدخل عنواناً للمحتوى (اختياري)
- **اللغة**: اختر `ar` للعربية أو `en` للإنجليزية

#### الخطوة 5: انتظر التوليد
ستعالج المنصة ملف PDF وتولد الصيغة (الصيغ) المختارة.

#### الخطوة 6: ابحث عن الناتج
ستكون الملفات المولدة في:
- الفيديوهات: `output/videos/`
- PowerPoint: `output/presentations/`
- تقارير Word: `output/reports/`
- تقارير PDF: `output/reports/`
- Excel: `output/excel/`

### أمثلة سريعة

**مثال 1: إنشاء عرض تسويقي**
```bash
python launcher.py كتالوج_المنتجات.pdf --format powerpoint --title "عرض المنتجات 2025"
```

**مثال 2: توليد فيديو توعوي بالعربية**
```bash
python launcher.py دليل_الصحة.pdf --format video --title "دليل الصحة" --language ar
```

**مثال 3: إنشاء كل شيء من ملف PDF واحد**
```bash
python launcher.py التقرير_السنوي.pdf --format all --title "التقرير السنوي 2024"
```

### نصائح لأفضل النتائج

1. **جودة PDF**: استخدم ملفات PDF بنص واضح وقابل للاستخراج
2. **أسماء الملفات**: استخدم أسماء وصفية بدون أحرف خاصة
3. **اللغة**: طابق إعداد اللغة مع محتوى PDF
4. **طول المحتوى**: ملفات PDF الأقصر والمهيكلة جيداً تعمل بشكل أفضل

---

## Common Issues / المشاكل الشائعة

### Issue: "Module not found"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### مشكلة: "الوحدة غير موجودة"
**الحل**: ثبت المكتبات المطلوبة
```bash
pip install -r requirements.txt
```

---

### Issue: "PDF file not found"
**Solution**: Use the full path to your PDF file
```bash
# Windows example
python launcher.py "C:\Users\YourName\Documents\file.pdf" --format powerpoint

# Mac/Linux example
python launcher.py "/home/username/Documents/file.pdf" --format powerpoint
```

### مشكلة: "ملف PDF غير موجود"
**الحل**: استخدم المسار الكامل لملف PDF

---

## Need Help? / تحتاج مساعدة؟

- Check the full documentation: `README.md`
- راجع التوثيق الكامل: `README.md`
- Visit: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues
