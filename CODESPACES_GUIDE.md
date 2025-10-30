# 🚀 استخدام منصة AWA من البيئات السحابية
# Using AWA Platform from Cloud Environments

**GitHub Codespaces & Gitpod Support**

---

## 🌟 النسخة العربية

### ما هي البيئات السحابية؟

البيئات السحابية (مثل GitHub Codespaces و Gitpod) هي بيئات تطوير كاملة تعمل في السحابة مباشرة من المتصفح. لا تحتاج إلى تحميل أو تثبيت أي شيء على جهازك!

### 🎯 المميزات

✅ **لا حاجة للتحميل** - العمل مباشرة من المتصفح  
✅ **بيئة جاهزة** - كل شيء مثبت ومهيأ تلقائياً  
✅ **أي جهاز** - استخدم من Windows, Mac, Linux, أو حتى iPad  
✅ **مجاني** - ساعات مجانية شهرياً للمستخدمين  

### 🆚 الفرق بين Codespaces و Gitpod

| الميزة | GitHub Codespaces | Gitpod |
|--------|-------------------|---------|
| الساعات المجانية | 60 ساعة/شهر | 50 ساعة/شهر |
| التكامل | مدمج مع GitHub | يدعم GitHub, GitLab, Bitbucket |
| السرعة | سريع جداً | سريع |
| التوفر | حسابات GitHub | حسابات منفصلة |

**كلاهما ممتاز - اختر ما يناسبك!**

---

## 📝 خطوات البدء مع GitHub Codespaces

### الخطوة 1: فتح Codespace

1. اذهب إلى صفحة المستودع على GitHub:
   ```
   https://github.com/aliabdelaal-adm/AWA_Awarness_2025
   ```

2. انقر على زر **"Code"** الأخضر (في الأعلى)

3. اختر تبويب **"Codespaces"**

4. انقر على **"Create codespace on main"**
   - أو انقر على زر `+` لإنشاء codespace جديد

5. انتظر بضع ثوانٍ حتى يتم إنشاء البيئة (أول مرة قد تأخذ 2-3 دقائق)

#### الخطوة 2: انتظر التثبيت التلقائي

بمجرد فتح Codespace، سيتم تلقائياً:
- ✅ تثبيت Python والمكتبات المطلوبة
- ✅ تثبيت FFmpeg (لمعالجة الفيديو)
- ✅ إنشاء المجلدات الضرورية
- ✅ تجهيز البيئة بالكامل

ستشاهد رسالة تأكيد عند الانتهاء:
```
✨ AWA Platform is ready to use!
```

#### الخطوة 3: تشغيل المنصة

لديك خياران:

**الخيار 1: استخدام الواجهة التفاعلية (موصى به للمبتدئين)**

في Terminal (الموجود في الأسفل)، اكتب:
```bash
python launcher.py
```

ستظهر قائمة تفاعلية:
```
=== AWA Content Generation Platform ===
1. Video Generation          / توليد فيديو
2. PowerPoint Presentation   / عرض PowerPoint
3. Professional Report (Word)/ تقرير احترافي (Word)
4. PDF Report                / تقرير PDF
5. Excel Spreadsheet         / ملف Excel
6. Generate All Formats      / توليد جميع الصيغ
```

**الخيار 2: فتح الواجهة الويب**

1. في Terminal، اكتب:
   ```bash
   python app.py
   ```

2. ستظهر نافذة منبثقة تقول "Your application running on port 5000 is available"

3. انقر **"Open in Browser"**

4. ستفتح الواجهة الويب للمنصة!

#### الخطوة 4: رفع ملفاتك

**للواجهة التفاعلية:**
- اتبع التعليمات لرفع ملف PDF
- يمكنك سحب وإسقاط الملف في نافذة VS Code الجانبية

**للواجهة الويب:**
- اضغط على زر "اختر الملفات" أو "Choose Files"
- اختر ملف PDF من جهازك
- أدخل العنوان واختر اللغة
- اضغط "إعداد العرض الإحترافي"

#### الخطوة 5: تحميل النتائج

بعد توليد المحتوى:
- انتقل إلى مجلد `output/` في المستكشف الجانبي
- انقر بالزر الأيمن على الملف المُولّد
- اختر **"Download"** لتحميله على جهازك

### 📂 رفع الملفات إلى Codespace

هناك عدة طرق لرفع ملفاتك:

**الطريقة 1: السحب والإفلات**
- اسحب ملف PDF من جهازك
- أفلته في المستكشف الجانبي في VS Code (في مجلد `uploads/`)

**الطريقة 2: رفع من القائمة**
- انقر بالزر الأيمن على مجلد `uploads/`
- اختر **"Upload..."**
- اختر ملفك

**الطريقة 3: من الواجهة الويب**
- ببساطة استخدم زر "اختر الملفات" في الواجهة

### 💡 نصائح مهمة

1. **الحفظ التلقائي**: Codespace يحفظ عملك تلقائياً

2. **إيقاف وتشغيل**: يمكنك إيقاف Codespace والعودة إليه لاحقاً من نفس الحالة

3. **الساعات المجانية**: 
   - حساب GitHub مجاني: 60 ساعة شهرياً
   - Codespace يتوقف تلقائياً بعد 30 دقيقة من عدم النشاط

4. **تحميل الملفات**: حمّل نتائجك دائماً قبل إيقاف Codespace

5. **حذف Codespace**: بعد الانتهاء، يمكنك حذف Codespace لتوفير المساحة:
   - اذهب إلى github.com/codespaces
   - احذف Codespaces القديمة غير المستخدمة

### 🎯 أمثلة سريعة

**مثال 1: توليد عرض PowerPoint**
```bash
python launcher.py uploads/myfile.pdf --format powerpoint --title "عرضي"
```

**مثال 2: توليد فيديو بالعربية**
```bash
python launcher.py uploads/guide.pdf --format video --title "دليل توعوي" --language ar
```

**مثال 3: توليد كل الصيغ**
```bash
python launcher.py uploads/report.pdf --format all --title "تقرير شامل"
```

### 🐛 حل المشاكل

**مشكلة: Codespace/Gitpod لا يفتح**
- تأكد من تسجيل الدخول إلى GitHub/Gitpod
- جرب تحديث الصفحة
- جرب البيئة الأخرى كبديل

**مشكلة: الأوامر لا تعمل**
- تأكد من أن Terminal مفتوح (اضغط Ctrl+` لفتحه)
- تأكد من أنك في المجلد الصحيح: `cd /workspaces/AWA_Awarness_2025`

**مشكلة: ملف PDF لا يُقرأ**
- تأكد من رفع الملف إلى مجلد `uploads/`
- تأكد من أن PDF يحتوي على نص وليس صور ممسوحة فقط

---

## 📝 خطوات البدء مع Gitpod

### الخطوة 1: فتح Gitpod

**الطريقة السريعة:**

انقر هنا مباشرة:
```
https://gitpod.io/#https://github.com/aliabdelaal-adm/AWA_Awarness_2025
```

أو:

1. اذهب إلى صفحة المستودع على GitHub
2. أضف `gitpod.io/#` قبل رابط المستودع في المتصفح
3. اضغط Enter

### الخطوة 2-6: نفس خطوات Codespaces

باقي الخطوات مماثلة تماماً لـ Codespaces! استخدم نفس الأوامر والإرشادات.

**الفرق الوحيد:**
- Gitpod: المجلد يكون `/workspace/AWA_Awarness_2025`
- Codespaces: المجلد يكون `/workspaces/AWA_Awarness_2025`

---

## 🌟 English Version

### What are Cloud Development Environments?

Cloud development environments (like GitHub Codespaces and Gitpod) are complete development environments that run in the cloud directly from your browser. No need to download or install anything on your computer!

### 🎯 Benefits

✅ **No Download Required** - Work directly from your browser  
✅ **Ready Environment** - Everything installed and configured automatically  
✅ **Any Device** - Use from Windows, Mac, Linux, or even iPad  
✅ **Free Tier** - Free hours per month for users  

### 🆚 Codespaces vs Gitpod Comparison

| Feature | GitHub Codespaces | Gitpod |
|---------|-------------------|---------|
| Free Hours | 60 hours/month | 50 hours/month |
| Integration | Built into GitHub | Supports GitHub, GitLab, Bitbucket |
| Speed | Very Fast | Fast |
| Availability | GitHub accounts | Separate accounts |

**Both are excellent - choose what works for you!**

---

## 📝 Getting Started with GitHub Codespaces
✅ **Ready Environment** - Everything installed and configured automatically  
✅ **Any Device** - Use from Windows, Mac, Linux, or even iPad  
✅ **Free Tier** - 60 free hours per month for users  

### 📝 Getting Started

#### Step 1: Open a Codespace

1. Go to the repository page on GitHub:
   ```
   https://github.com/aliabdelaal-adm/AWA_Awarness_2025
   ```

2. Click the green **"Code"** button (at the top)

3. Select the **"Codespaces"** tab

4. Click **"Create codespace on main"**
   - Or click the `+` button to create a new codespace

5. Wait a few seconds for the environment to be created (first time may take 2-3 minutes)

#### Step 2: Wait for Automatic Setup

Once the Codespace opens, it will automatically:
- ✅ Install Python and required libraries
- ✅ Install FFmpeg (for video processing)
- ✅ Create necessary directories
- ✅ Prepare the complete environment

You'll see a confirmation message when ready:
```
✨ AWA Platform is ready to use!
```

#### Step 3: Launch the Platform

You have two options:

**Option 1: Use Interactive Interface (Recommended for Beginners)**

In the Terminal (at the bottom), type:
```bash
python launcher.py
```

An interactive menu will appear:
```
=== AWA Content Generation Platform ===
1. Video Generation          / توليد فيديو
2. PowerPoint Presentation   / عرض PowerPoint
3. Professional Report (Word)/ تقرير احترافي (Word)
4. PDF Report                / تقرير PDF
5. Excel Spreadsheet         / ملف Excel
6. Generate All Formats      / توليد جميع الصيغ
```

**Option 2: Open Web Interface**

1. In Terminal, type:
   ```bash
   python app.py
   ```

2. A popup will appear saying "Your application running on port 5000 is available"

3. Click **"Open in Browser"**

4. The web interface will open!

#### Step 4: Upload Your Files

**For Interactive Interface:**
- Follow the prompts to upload a PDF file
- You can drag and drop the file into the VS Code sidebar

**For Web Interface:**
- Click the "Choose Files" button
- Select a PDF file from your computer
- Enter title and select language
- Click "Generate Professional Presentation"

#### Step 5: Download Results

After generating content:
- Navigate to the `output/` folder in the sidebar explorer
- Right-click on the generated file
- Select **"Download"** to download it to your computer

### 📂 Uploading Files to Codespace

There are several ways to upload your files:

**Method 1: Drag and Drop**
- Drag a PDF file from your computer
- Drop it into the VS Code sidebar explorer (in the `uploads/` folder)

**Method 2: Upload from Menu**
- Right-click on the `uploads/` folder
- Select **"Upload..."**
- Choose your file

**Method 3: From Web Interface**
- Simply use the "Choose Files" button in the interface

### 💡 Important Tips

1. **Auto-Save**: Codespace saves your work automatically

2. **Stop and Resume**: You can stop the Codespace and resume later from the same state

3. **Free Hours**: 
   - Free GitHub account: 60 hours per month
   - Codespace stops automatically after 30 minutes of inactivity

4. **Download Files**: Always download your results before stopping the Codespace

5. **Delete Codespace**: After finishing, you can delete the Codespace to save space:
   - Go to github.com/codespaces
   - Delete old unused Codespaces

### 🎯 Quick Examples

**Example 1: Generate PowerPoint Presentation**
```bash
python launcher.py uploads/myfile.pdf --format powerpoint --title "My Presentation"
```

**Example 2: Generate Arabic Video**
```bash
python launcher.py uploads/guide.pdf --format video --title "Awareness Guide" --language ar
```

**Example 3: Generate All Formats**
```bash
python launcher.py uploads/report.pdf --format all --title "Complete Report"
```

### 🐛 Troubleshooting

**Issue: Codespace/Gitpod won't open**
- Make sure you're logged into GitHub/Gitpod
- Try refreshing the page
- Try the alternative environment

**Issue: Commands don't work**
- Make sure Terminal is open (press Ctrl+` to open it)
- Make sure you're in the right directory: `cd /workspaces/AWA_Awarness_2025`

**Issue: PDF file not read**
- Make sure the file is uploaded to the `uploads/` folder
- Make sure the PDF contains text and not just scanned images

---

## 📝 Getting Started with Gitpod

### Step 1: Open Gitpod

**Quick Way:**

Click here directly:
```
https://gitpod.io/#https://github.com/aliabdelaal-adm/AWA_Awarness_2025
```

Or:

1. Go to the repository page on GitHub
2. Add `gitpod.io/#` before the repository URL in your browser
3. Press Enter

### Steps 2-6: Same as Codespaces

The rest of the steps are exactly the same as Codespaces! Use the same commands and instructions.

**Only Difference:**
- Gitpod: Directory is `/workspace/AWA_Awarness_2025`
- Codespaces: Directory is `/workspaces/AWA_Awarness_2025`

---

## 🎥 Video Tutorials

[Video tutorials will be added here]

## 🆘 Need Help?

- Check the main documentation: `README.md`
- Quick start guide: `QUICK_START.md`
- Visit: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues

---

**Made with ❤️ by AWA Awareness Team**
