# 🚀 How to Launch AWA Platform from Anywhere
# كيفية فتح منصة AWA من أي مكان

---

## 🆕 للمبتدئين / For Beginners

**🪟 إذا كنت مستخدم ويندوز ولا تعرف كيف تبدأ:**
- راجع الدليل الكامل: [`WINDOWS_SETUP_GUIDE.md`](WINDOWS_SETUP_GUIDE.md)
- يشرح كل شيء من البداية: تثبيت Python، Git، FFmpeg، وتشغيل المنصة

**🪟 If you're a Windows user and don't know where to start:**
- See the complete guide: [`WINDOWS_SETUP_GUIDE.md`](WINDOWS_SETUP_GUIDE.md)  
- Explains everything from scratch: installing Python, Git, FFmpeg, and running the platform

---

## English Version

### Overview

The AWA Content Generation Platform can be launched from any location on your computer. This guide shows you several methods to open and use the platform.

### Method 1: Using the Quick Launcher Scripts (Easiest)

#### Windows Users:

1. **Navigate to the AWA folder** in File Explorer
2. **Double-click** on `awa_launch.bat`
3. The platform will open automatically!

Or from Command Prompt:
```cmd
cd C:\path\to\AWA_Awarness_2025
awa_launch.bat
```

#### macOS/Linux Users:

1. **Open Terminal**
2. **Navigate to AWA folder**:
   ```bash
   cd /path/to/AWA_Awarness_2025
   ```
3. **Run the launcher**:
   ```bash
   ./awa_launch.sh
   ```

### Method 2: Using Python Directly

From **any directory**, you can run:

```bash
# Navigate to the AWA folder first
cd /path/to/AWA_Awarness_2025

# Then run the launcher
python launcher.py
```

Or specify the full path:
```bash
python /full/path/to/AWA_Awarness_2025/launcher.py
```

### Method 3: Add AWA to Your System PATH (Advanced)

This allows you to run AWA from anywhere without navigating to the folder.

#### Windows:

1. **Add to System PATH**:
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "User variables", find "Path"
   - Click "Edit" → "New"
   - Add: `C:\path\to\AWA_Awarness_2025`
   - Click OK to save

2. **Create a batch file** (Optional):
   - Create `awa.bat` in a folder that's in your PATH
   - Add this content:
     ```batch
     @echo off
     python C:\path\to\AWA_Awarness_2025\launcher.py %*
     ```

3. **Now you can run from anywhere**:
   ```cmd
   awa
   ```

#### macOS/Linux:

1. **Add an alias** to your `.bashrc` or `.zshrc`:
   ```bash
   alias awa='cd /path/to/AWA_Awarness_2025 && python3 launcher.py'
   ```

2. **Reload your shell**:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc
   ```

3. **Now you can run from anywhere**:
   ```bash
   awa
   ```

### Method 4: Using Command-Line Arguments

You can generate content directly without the interactive menu:

```bash
# PowerPoint from any PDF
python launcher.py /path/to/document.pdf --format powerpoint --title "My Presentation"

# Word Report
python launcher.py /path/to/document.pdf --format word --title "Annual Report"

# Excel File
python launcher.py /path/to/document.pdf --format excel

# Video
python launcher.py /path/to/document.pdf --format video --language ar

# Everything at once!
python launcher.py /path/to/document.pdf --format all --title "Complete Package"
```

### Quick Reference Card

| Action | Command |
|--------|---------|
| Open Interactive Menu | `python launcher.py` |
| Generate PowerPoint | `python launcher.py file.pdf --format powerpoint` |
| Generate Word Report | `python launcher.py file.pdf --format word` |
| Generate Excel | `python launcher.py file.pdf --format excel` |
| Generate Video | `python launcher.py file.pdf --format video` |
| Generate All | `python launcher.py file.pdf --format all` |

### Troubleshooting

**Problem**: "launcher.py not found"
- **Solution**: Make sure you're in the AWA_Awarness_2025 directory, or provide the full path

**Problem**: "Permission denied" on Linux/Mac
- **Solution**: Run `chmod +x awa_launch.sh launcher.py`

**Problem**: "Python not found"
- **Solution**: Install Python 3.8+ from python.org

---

## النسخة العربية

### نظرة عامة

يمكن تشغيل منصة AWA لتوليد المحتوى من أي موقع على جهازك. يوضح هذا الدليل عدة طرق لفتح واستخدام المنصة.

### الطريقة 1: استخدام نصوص الإطلاق السريع (الأسهل)

#### مستخدمو ويندوز:

1. **انتقل إلى مجلد AWA** في مستكشف الملفات
2. **انقر نقراً مزدوجاً** على `awa_launch.bat`
3. ستفتح المنصة تلقائياً!

أو من موجه الأوامر:
```cmd
cd C:\path\to\AWA_Awarness_2025
awa_launch.bat
```

#### مستخدمو ماك/لينكس:

1. **افتح الترمينال**
2. **انتقل إلى مجلد AWA**:
   ```bash
   cd /path/to/AWA_Awarness_2025
   ```
3. **شغل أداة الإطلاق**:
   ```bash
   ./awa_launch.sh
   ```

### الطريقة 2: استخدام Python مباشرة

من **أي مجلد**، يمكنك تنفيذ:

```bash
# انتقل إلى مجلد AWA أولاً
cd /path/to/AWA_Awarness_2025

# ثم شغل أداة الإطلاق
python launcher.py
```

أو حدد المسار الكامل:
```bash
python /full/path/to/AWA_Awarness_2025/launcher.py
```

### الطريقة 3: إضافة AWA إلى مسار النظام (متقدم)

هذا يسمح لك بتشغيل AWA من أي مكان بدون الانتقال إلى المجلد.

#### ويندوز:

1. **أضف إلى مسار النظام**:
   - انقر بالزر الأيمن على "هذا الكمبيوتر" → خصائص
   - انقر "إعدادات النظام المتقدمة"
   - انقر "متغيرات البيئة"
   - تحت "متغيرات المستخدم"، ابحث عن "Path"
   - انقر "تحرير" → "جديد"
   - أضف: `C:\path\to\AWA_Awarness_2025`
   - انقر موافق للحفظ

2. **أنشئ ملف دفعي** (اختياري):
   - أنشئ `awa.bat` في مجلد موجود في PATH
   - أضف هذا المحتوى:
     ```batch
     @echo off
     python C:\path\to\AWA_Awarness_2025\launcher.py %*
     ```

3. **الآن يمكنك التشغيل من أي مكان**:
   ```cmd
   awa
   ```

#### ماك/لينكس:

1. **أضف اختصاراً** إلى `.bashrc` أو `.zshrc`:
   ```bash
   alias awa='cd /path/to/AWA_Awarness_2025 && python3 launcher.py'
   ```

2. **أعد تحميل الشل**:
   ```bash
   source ~/.bashrc  # أو source ~/.zshrc
   ```

3. **الآن يمكنك التشغيل من أي مكان**:
   ```bash
   awa
   ```

### الطريقة 4: استخدام معاملات سطر الأوامر

يمكنك توليد المحتوى مباشرة بدون القائمة التفاعلية:

```bash
# PowerPoint من أي PDF
python launcher.py /path/to/document.pdf --format powerpoint --title "عرضي التقديمي"

# تقرير Word
python launcher.py /path/to/document.pdf --format word --title "التقرير السنوي"

# ملف Excel
python launcher.py /path/to/document.pdf --format excel

# فيديو
python launcher.py /path/to/document.pdf --format video --language ar

# كل شيء مرة واحدة!
python launcher.py /path/to/document.pdf --format all --title "الحزمة الكاملة"
```

### بطاقة مرجعية سريعة

| الإجراء | الأمر |
|---------|-------|
| فتح القائمة التفاعلية | `python launcher.py` |
| توليد PowerPoint | `python launcher.py file.pdf --format powerpoint` |
| توليد تقرير Word | `python launcher.py file.pdf --format word` |
| توليد Excel | `python launcher.py file.pdf --format excel` |
| توليد فيديو | `python launcher.py file.pdf --format video` |
| توليد الكل | `python launcher.py file.pdf --format all` |

### حل المشاكل

**مشكلة**: "launcher.py not found"
- **الحل**: تأكد من أنك في مجلد AWA_Awarness_2025، أو قدم المسار الكامل

**مشكلة**: "Permission denied" على لينكس/ماك
- **الحل**: نفذ `chmod +x awa_launch.sh launcher.py`

**مشكلة**: "Python not found"
- **الحل**: ثبت Python 3.8+ من python.org

---

## Video Tutorial Links

[Link to video tutorials will be added here]

## Need More Help?

- Check the full documentation: `README.md`
- Quick start guide: `QUICK_START.md`
- Visit: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues
