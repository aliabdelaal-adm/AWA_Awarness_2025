# 🪟 دليل التثبيت والإعداد الكامل لويندوز
# 🪟 Complete Windows Setup and Installation Guide

---

## 📖 النسخة العربية (Arabic Version)

### 🎯 نظرة عامة

هذا الدليل الشامل سيساعدك على تحميل وتثبيت وتشغيل منصة AWA لتوليد المحتوى على جهاز ويندوز الخاص بك من الصفر، حتى لو لم تكن لديك أي خبرة برمجية.

---

## 📋 الخطوة 1: تثبيت المتطلبات الأساسية

### 1.1 تثبيت Python

Python هو لغة البرمجة المطلوبة لتشغيل المنصة.

**خطوات التثبيت:**

1. **تحميل Python:**
   - افتح المتصفح وانتقل إلى: https://www.python.org/downloads/
   - انقر على زر "Download Python" الأصفر الكبير
   - سيتم تحميل ملف مثل `python-3.x.x-amd64.exe`

2. **تثبيت Python:**
   - انقر نقراً مزدوجاً على الملف المحمل
   - **مهم جداً**: ✅ ضع علامة في المربع "Add Python to PATH"
   - انقر على "Install Now"
   - انتظر حتى يكتمل التثبيت
   - انقر على "Close"

3. **التحقق من التثبيت:**
   - افتح Command Prompt (ابحث عن "cmd" في قائمة ابدأ)
   - اكتب الأمر التالي واضغط Enter:
     ```cmd
     python --version
     ```
   - يجب أن ترى رقم الإصدار مثل: `Python 3.12.0`

### 1.2 تثبيت Git (للتحميل من GitHub)

Git يتيح لك تحميل المشروع من GitHub.

**خطوات التثبيت:**

1. **تحميل Git:**
   - افتح المتصفح وانتقل إلى: https://git-scm.com/download/win
   - سيبدأ التحميل تلقائياً
   - إذا لم يبدأ، انقر على "Click here to download manually"

2. **تثبيت Git:**
   - انقر نقراً مزدوجاً على الملف المحمل
   - اتبع التعليمات واضغط "Next" في كل خطوة
   - احتفظ بالإعدادات الافتراضية
   - انقر على "Install" ثم "Finish"

3. **التحقق من التثبيت:**
   - افتح Command Prompt جديد
   - اكتب:
     ```cmd
     git --version
     ```
   - يجب أن ترى: `git version x.x.x`

### 1.3 تثبيت FFmpeg (لمعالجة الفيديو)

FFmpeg مطلوب لتوليد الفيديوهات.

**خطوات التثبيت:**

1. **تحميل FFmpeg:**
   - انتقل إلى: https://www.gyan.dev/ffmpeg/builds/
   - انقر على "ffmpeg-release-essentials.zip" لتحميله

2. **استخراج الملفات:**
   - انقر بالزر الأيمن على الملف المحمل
   - اختر "Extract All"
   - اختر مكان الاستخراج، مثلاً: `C:\ffmpeg`

3. **إضافة FFmpeg إلى PATH:**
   - انقر بالزر الأيمن على "This PC" أو "My Computer"
   - اختر "Properties" (خصائص)
   - انقر على "Advanced system settings" (إعدادات النظام المتقدمة)
   - انقر على "Environment Variables" (متغيرات البيئة)
   - في قسم "System variables"، ابحث عن "Path" وانقر على "Edit"
   - انقر على "New" وأضف: `C:\ffmpeg\bin` (أو المسار حيث استخرجت الملفات)
   - انقر على "OK" في جميع النوافذ

4. **التحقق من التثبيت:**
   - افتح Command Prompt جديد (مهم: يجب أن يكون جديداً)
   - اكتب:
     ```cmd
     ffmpeg -version
     ```
   - يجب أن ترى معلومات عن FFmpeg

---

## 📥 الخطوة 2: تحميل منصة AWA

### طريقة 1: باستخدام Git (مستحسنة)

1. **اختر مكان التحميل:**
   - افتح Command Prompt
   - انتقل إلى المجلد الذي تريد تحميل المشروع فيه، مثلاً:
     ```cmd
     cd C:\Users\YourName\Documents
     ```

2. **تحميل المشروع:**
   ```cmd
   git clone https://github.com/aliabdelaal-adm/AWA_Awarness_2025.git
   ```

3. **الدخول إلى مجلد المشروع:**
   ```cmd
   cd AWA_Awarness_2025
   ```

### طريقة 2: التحميل المباشر من GitHub

1. افتح المتصفح وانتقل إلى: https://github.com/aliabdelaal-adm/AWA_Awarness_2025
2. انقر على الزر الأخضر "Code"
3. اختر "Download ZIP"
4. استخرج الملف المحمل في المكان الذي تريده
5. افتح Command Prompt وانتقل إلى المجلد:
   ```cmd
   cd C:\path\to\AWA_Awarness_2025
   ```

---

## 🔧 الخطوة 3: تثبيت المكتبات المطلوبة

1. **تأكد من أنك في مجلد المشروع:**
   ```cmd
   cd C:\path\to\AWA_Awarness_2025
   ```

2. **تثبيت جميع المكتبات المطلوبة:**
   ```cmd
   pip install -r requirements.txt
   ```
   
   هذا الأمر سيقوم بتحميل وتثبيت جميع المكتبات اللازمة تلقائياً. قد يستغرق بضع دقائق.

3. **انتظر حتى يكتمل التثبيت:**
   - ستظهر العديد من الرسائل أثناء التثبيت
   - عندما يكتمل، ستعود إلى موجه الأوامر

---

## 🚀 الخطوة 4: تشغيل المنصة

### طريقة 1: الطريقة السهلة (نقرة مزدوجة)

1. افتح مستكشف الملفات (File Explorer)
2. انتقل إلى مجلد `AWA_Awarness_2025`
3. ابحث عن ملف `awa_launch.bat`
4. **انقر نقراً مزدوجاً** على الملف
5. ستفتح نافذة القائمة التفاعلية!

### طريقة 2: من موجه الأوامر

1. افتح Command Prompt
2. انتقل إلى مجلد المشروع:
   ```cmd
   cd C:\path\to\AWA_Awarness_2025
   ```
3. شغل المنصة:
   ```cmd
   awa_launch.bat
   ```

### طريقة 3: مباشرة بـ Python

```cmd
python launcher.py
```

---

## 🎬 الخطوة 5: استخدام المنصة

### استخدام القائمة التفاعلية

عند تشغيل المنصة، ستظهر القائمة التالية:

```
1. Video Generation          / توليد فيديو
2. PowerPoint Presentation   / عرض PowerPoint
3. Professional Report (Word)/ تقرير احترافي (Word)
4. PDF Report                / تقرير PDF
5. Excel Spreadsheet         / ملف Excel
6. Generate All Formats      / توليد جميع الصيغ
0. Exit                      / خروج
```

**اتبع الخطوات:**

1. **اختر رقم الخيار** الذي تريده (1-6)
2. **أدخل مسار ملف PDF**، مثلاً:
   ```
   C:\Users\YourName\Documents\myfile.pdf
   ```
3. **أدخل عنواناً** للمحتوى (أو اضغط Enter للتخطي)
4. **اختر اللغة**: `ar` للعربية أو `en` للإنجليزية
5. **انتظر** حتى يكتمل التوليد
6. **ابحث عن الملفات المولدة** في مجلد `output`

### استخدام سطر الأوامر (متقدم)

يمكنك توليد المحتوى مباشرة بدون القائمة:

**توليد عرض PowerPoint:**
```cmd
python launcher.py myfile.pdf --format powerpoint --title "عرضي التقديمي"
```

**توليد فيديو بالعربية:**
```cmd
python launcher.py myfile.pdf --format video --title "فيديو توعوي" --language ar
```

**توليد جميع الصيغ مرة واحدة:**
```cmd
python launcher.py myfile.pdf --format all --title "حزمة كاملة"
```

---

## 📂 أين تجد الملفات المولدة؟

بعد التوليد، ستجد الملفات في المجلدات التالية:

- **الفيديوهات**: `output\videos\`
- **عروض PowerPoint**: `output\presentations\`
- **تقارير Word**: `output\reports\`
- **تقارير PDF**: `output\reports\`
- **ملفات Excel**: `output\excel\`

---

## 🔍 حل المشاكل الشائعة

### مشكلة 1: "python is not recognized"

**السبب**: Python غير مثبت أو غير مضاف إلى PATH

**الحل**:
1. أعد تثبيت Python وتأكد من وضع علامة في "Add Python to PATH"
2. أو أضف Python يدوياً إلى PATH

### مشكلة 2: "ffmpeg is not recognized"

**السبب**: FFmpeg غير مثبت أو غير مضاف إلى PATH

**الحل**:
1. اتبع خطوات تثبيت FFmpeg أعلاه
2. تأكد من إضافة المسار الصحيح إلى PATH
3. أعد تشغيل Command Prompt

### مشكلة 3: "No module named 'xxx'"

**السبب**: المكتبات المطلوبة غير مثبتة

**الحل**:
```cmd
pip install -r requirements.txt
```

### مشكلة 4: "PDF file not found"

**السبب**: المسار إلى ملف PDF غير صحيح

**الحل**:
1. استخدم المسار الكامل للملف
2. تأكد من عدم وجود أخطاء إملائية
3. استخدم علامات اقتباس إذا كان المسار يحتوي على مسافات:
   ```cmd
   "C:\My Documents\file.pdf"
   ```

### مشكلة 5: الأحرف العربية لا تظهر بشكل صحيح

**الحل**:
1. افتح Command Prompt
2. اكتب:
   ```cmd
   chcp 65001
   ```
3. شغل المنصة مرة أخرى

---

## 💡 نصائح مهمة

1. **استخدم ملفات PDF بنص قابل للاستخراج**
   - لا تستخدم ملفات PDF التي هي صور ممسوحة فقط

2. **تأكد من اتصال الإنترنت**
   - المنصة تحتاج إنترنت لتحويل النص إلى صوت

3. **ابدأ بملفات صغيرة**
   - جرب المنصة أولاً مع ملف PDF صغير للتأكد من أن كل شيء يعمل

4. **احتفظ بنسخة احتياطية**
   - احفظ ملفاتك الأصلية في مكان آمن

---

## 📞 الحصول على المساعدة

إذا واجهت أي مشاكل:

1. راجع ملف `README.md` للمزيد من المعلومات
2. راجع ملف `FAQ.md` للأسئلة الشائعة
3. افتح issue على GitHub: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues

---

## 📖 English Version

### 🎯 Overview

This comprehensive guide will help you download, install, and run the AWA Content Generation Platform on your Windows computer from scratch, even if you have no programming experience.

---

## 📋 Step 1: Install Prerequisites

### 1.1 Install Python

Python is the programming language required to run the platform.

**Installation Steps:**

1. **Download Python:**
   - Open your browser and go to: https://www.python.org/downloads/
   - Click the big yellow "Download Python" button
   - A file like `python-3.x.x-amd64.exe` will download

2. **Install Python:**
   - Double-click the downloaded file
   - **Very Important**: ✅ Check the box "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete
   - Click "Close"

3. **Verify Installation:**
   - Open Command Prompt (search for "cmd" in Start menu)
   - Type the following command and press Enter:
     ```cmd
     python --version
     ```
   - You should see a version number like: `Python 3.12.0`

### 1.2 Install Git (to download from GitHub)

Git allows you to download the project from GitHub.

**Installation Steps:**

1. **Download Git:**
   - Open your browser and go to: https://git-scm.com/download/win
   - Download will start automatically
   - If not, click "Click here to download manually"

2. **Install Git:**
   - Double-click the downloaded file
   - Follow the instructions and click "Next" at each step
   - Keep the default settings
   - Click "Install" then "Finish"

3. **Verify Installation:**
   - Open a new Command Prompt
   - Type:
     ```cmd
     git --version
     ```
   - You should see: `git version x.x.x`

### 1.3 Install FFmpeg (for video processing)

FFmpeg is required to generate videos.

**Installation Steps:**

1. **Download FFmpeg:**
   - Go to: https://www.gyan.dev/ffmpeg/builds/
   - Click on "ffmpeg-release-essentials.zip" to download

2. **Extract Files:**
   - Right-click the downloaded file
   - Choose "Extract All"
   - Choose extraction location, e.g.: `C:\ffmpeg`

3. **Add FFmpeg to PATH:**
   - Right-click "This PC" or "My Computer"
   - Choose "Properties"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - In "System variables", find "Path" and click "Edit"
   - Click "New" and add: `C:\ffmpeg\bin` (or the path where you extracted)
   - Click "OK" on all windows

4. **Verify Installation:**
   - Open a new Command Prompt (important: must be new)
   - Type:
     ```cmd
     ffmpeg -version
     ```
   - You should see information about FFmpeg

---

## 📥 Step 2: Download AWA Platform

### Method 1: Using Git (Recommended)

1. **Choose Download Location:**
   - Open Command Prompt
   - Navigate to folder where you want to download, e.g.:
     ```cmd
     cd C:\Users\YourName\Documents
     ```

2. **Download Project:**
   ```cmd
   git clone https://github.com/aliabdelaal-adm/AWA_Awarness_2025.git
   ```

3. **Enter Project Folder:**
   ```cmd
   cd AWA_Awarness_2025
   ```

### Method 2: Direct Download from GitHub

1. Open browser and go to: https://github.com/aliabdelaal-adm/AWA_Awarness_2025
2. Click the green "Code" button
3. Choose "Download ZIP"
4. Extract the downloaded file to your desired location
5. Open Command Prompt and navigate to folder:
   ```cmd
   cd C:\path\to\AWA_Awarness_2025
   ```

---

## 🔧 Step 3: Install Required Libraries

1. **Make sure you're in the project folder:**
   ```cmd
   cd C:\path\to\AWA_Awarness_2025
   ```

2. **Install all required libraries:**
   ```cmd
   pip install -r requirements.txt
   ```
   
   This command will download and install all necessary libraries automatically. May take a few minutes.

3. **Wait for installation to complete:**
   - Many messages will appear during installation
   - When complete, you'll return to command prompt

---

## 🚀 Step 4: Launch the Platform

### Method 1: Easy Way (Double-Click)

1. Open File Explorer
2. Navigate to `AWA_Awarness_2025` folder
3. Find the file `awa_launch.bat`
4. **Double-click** the file
5. The interactive menu window will open!

### Method 2: From Command Prompt

1. Open Command Prompt
2. Navigate to project folder:
   ```cmd
   cd C:\path\to\AWA_Awarness_2025
   ```
3. Run the platform:
   ```cmd
   awa_launch.bat
   ```

### Method 3: Directly with Python

```cmd
python launcher.py
```

---

## 🎬 Step 5: Using the Platform

### Using the Interactive Menu

When you launch the platform, you'll see this menu:

```
1. Video Generation          / توليد فيديو
2. PowerPoint Presentation   / عرض PowerPoint
3. Professional Report (Word)/ تقرير احترافي (Word)
4. PDF Report                / تقرير PDF
5. Excel Spreadsheet         / ملف Excel
6. Generate All Formats      / توليد جميع الصيغ
0. Exit                      / خروج
```

**Follow these steps:**

1. **Choose option number** you want (1-6)
2. **Enter PDF file path**, e.g.:
   ```
   C:\Users\YourName\Documents\myfile.pdf
   ```
3. **Enter title** for content (or press Enter to skip)
4. **Choose language**: `ar` for Arabic or `en` for English
5. **Wait** for generation to complete
6. **Find generated files** in `output` folder

### Using Command Line (Advanced)

You can generate content directly without the menu:

**Generate PowerPoint Presentation:**
```cmd
python launcher.py myfile.pdf --format powerpoint --title "My Presentation"
```

**Generate Arabic Video:**
```cmd
python launcher.py myfile.pdf --format video --title "Awareness Video" --language ar
```

**Generate All Formats at Once:**
```cmd
python launcher.py myfile.pdf --format all --title "Complete Package"
```

---

## 📂 Where to Find Generated Files?

After generation, you'll find files in these folders:

- **Videos**: `output\videos\`
- **PowerPoint Presentations**: `output\presentations\`
- **Word Reports**: `output\reports\`
- **PDF Reports**: `output\reports\`
- **Excel Files**: `output\excel\`

---

## 🔍 Troubleshooting Common Issues

### Issue 1: "python is not recognized"

**Cause**: Python not installed or not added to PATH

**Solution**:
1. Reinstall Python and make sure to check "Add Python to PATH"
2. Or add Python manually to PATH

### Issue 2: "ffmpeg is not recognized"

**Cause**: FFmpeg not installed or not added to PATH

**Solution**:
1. Follow FFmpeg installation steps above
2. Make sure to add correct path to PATH
3. Restart Command Prompt

### Issue 3: "No module named 'xxx'"

**Cause**: Required libraries not installed

**Solution**:
```cmd
pip install -r requirements.txt
```

### Issue 4: "PDF file not found"

**Cause**: Path to PDF file is incorrect

**Solution**:
1. Use full path to file
2. Make sure there are no typos
3. Use quotes if path contains spaces:
   ```cmd
   "C:\My Documents\file.pdf"
   ```

### Issue 5: Arabic characters don't display correctly

**Solution**:
1. Open Command Prompt
2. Type:
   ```cmd
   chcp 65001
   ```
3. Run platform again

---

## 💡 Important Tips

1. **Use PDFs with extractable text**
   - Don't use PDFs that are just scanned images

2. **Ensure internet connection**
   - Platform needs internet for text-to-speech

3. **Start with small files**
   - Try platform first with a small PDF to make sure everything works

4. **Keep backups**
   - Save your original files in a safe place

---

## 📞 Getting Help

If you encounter any problems:

1. Check `README.md` file for more information
2. Check `FAQ.md` file for frequently asked questions
3. Open an issue on GitHub: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues

---

**Made with ❤️ by AWA Awareness Team**
