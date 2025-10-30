# 📋 Windows Quick Reference Card
# 📋 البطاقة المرجعية السريعة لويندوز

---

## 🎯 النسخة العربية (Arabic Version)

### تشغيل المنصة بسرعة

**الطريقة السهلة:**
```
1. افتح مجلد AWA_Awarness_2025
2. انقر نقراً مزدوجاً على: awa_launch.bat
```

**من Command Prompt:**
```cmd
cd C:\path\to\AWA_Awarness_2025
awa_launch.bat
```

---

### الأوامر الأساسية

| الوظيفة | الأمر |
|---------|-------|
| القائمة التفاعلية | `python launcher.py` |
| عرض PowerPoint | `python launcher.py file.pdf --format powerpoint` |
| تقرير Word | `python launcher.py file.pdf --format word` |
| فيديو بالعربية | `python launcher.py file.pdf --format video --language ar` |
| جميع الصيغ | `python launcher.py file.pdf --format all` |

---

### أمثلة سريعة

**توليد عرض تقديمي:**
```cmd
python launcher.py "C:\Documents\myfile.pdf" --format powerpoint --title "عرضي"
```

**توليد فيديو توعوي:**
```cmd
python launcher.py "C:\Documents\guide.pdf" --format video --title "دليل توعوي" --language ar
```

**توليد كل شيء:**
```cmd
python launcher.py "C:\Documents\report.pdf" --format all --title "تقرير شامل"
```

---

### مواقع الملفات المولدة

| النوع | المسار |
|------|--------|
| فيديوهات | `output\videos\` |
| PowerPoint | `output\presentations\` |
| Word | `output\reports\` |
| PDF | `output\reports\` |
| Excel | `output\excel\` |

---

### حل المشاكل السريع

**Python غير موجود:**
```cmd
تثبيت من: https://www.python.org/downloads/
تأكد من: Add Python to PATH ✓
```

**المكتبات غير مثبتة:**
```cmd
pip install -r requirements.txt
```

**FFmpeg غير موجود:**
```cmd
تحميل من: https://www.gyan.dev/ffmpeg/builds/
راجع: WINDOWS_SETUP_GUIDE.md
```

**ملف PDF غير موجود:**
```cmd
استخدم المسار الكامل:
"C:\Users\YourName\Documents\file.pdf"
```

**الأحرف العربية لا تظهر:**
```cmd
chcp 65001
```

---

### روابط مفيدة

- **الدليل الكامل**: `WINDOWS_SETUP_GUIDE.md`
- **البدء السريع**: `QUICK_START.md`
- **التوثيق**: `README.md`
- **الأسئلة الشائعة**: `FAQ.md`

---

## 🎯 English Version

### Quick Launch

**Easy Way:**
```
1. Open AWA_Awarness_2025 folder
2. Double-click: awa_launch.bat
```

**From Command Prompt:**
```cmd
cd C:\path\to\AWA_Awarness_2025
awa_launch.bat
```

---

### Basic Commands

| Function | Command |
|----------|---------|
| Interactive Menu | `python launcher.py` |
| PowerPoint | `python launcher.py file.pdf --format powerpoint` |
| Word Report | `python launcher.py file.pdf --format word` |
| Arabic Video | `python launcher.py file.pdf --format video --language ar` |
| All Formats | `python launcher.py file.pdf --format all` |

---

### Quick Examples

**Generate Presentation:**
```cmd
python launcher.py "C:\Documents\myfile.pdf" --format powerpoint --title "My Presentation"
```

**Generate Awareness Video:**
```cmd
python launcher.py "C:\Documents\guide.pdf" --format video --title "Awareness Guide" --language ar
```

**Generate Everything:**
```cmd
python launcher.py "C:\Documents\report.pdf" --format all --title "Complete Report"
```

---

### Output File Locations

| Type | Path |
|------|------|
| Videos | `output\videos\` |
| PowerPoint | `output\presentations\` |
| Word | `output\reports\` |
| PDF | `output\reports\` |
| Excel | `output\excel\` |

---

### Quick Troubleshooting

**Python not found:**
```cmd
Install from: https://www.python.org/downloads/
Make sure: Add Python to PATH ✓
```

**Libraries not installed:**
```cmd
pip install -r requirements.txt
```

**FFmpeg not found:**
```cmd
Download from: https://www.gyan.dev/ffmpeg/builds/
See: WINDOWS_SETUP_GUIDE.md
```

**PDF file not found:**
```cmd
Use full path:
"C:\Users\YourName\Documents\file.pdf"
```

**Arabic characters don't display:**
```cmd
chcp 65001
```

---

### Useful Links

- **Complete Guide**: `WINDOWS_SETUP_GUIDE.md`
- **Quick Start**: `QUICK_START.md`
- **Documentation**: `README.md`
- **FAQ**: `FAQ.md`

---

## 📞 Getting Help / الحصول على المساعدة

**For detailed help:**
- Read: `WINDOWS_SETUP_GUIDE.md` (Complete installation guide)
- Read: `QUICK_START.md` (Platform usage guide)
- Read: `README.md` (Full documentation)
- Visit: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues

**للحصول على مساعدة مفصلة:**
- اقرأ: `WINDOWS_SETUP_GUIDE.md` (دليل التثبيت الكامل)
- اقرأ: `QUICK_START.md` (دليل استخدام المنصة)
- اقرأ: `README.md` (التوثيق الكامل)
- زر: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues

---

**Made with ❤️ by AWA Awareness Team**
