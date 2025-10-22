# Frequently Asked Questions (FAQ)
# الأسئلة المتكررة

---

## English

### General Questions

**Q: What is AWA AI Video Generation Tool?**

A: It's an AI-powered application that automatically converts PDF documents into professional promotional, educational, and awareness videos with AI-generated voiceovers.

**Q: What languages are supported?**

A: Currently, the tool supports Arabic and English for both text processing and text-to-speech conversion.

**Q: Is this tool free to use?**

A: Yes, the tool is open-source and free under the MIT License. However, some features may require internet connectivity for AI services.

### Installation & Setup

**Q: What are the system requirements?**

A: 
- Python 3.8 or higher
- 4GB RAM minimum (8GB recommended)
- FFmpeg installed
- Internet connection (for TTS)
- 1GB free disk space

**Q: How do I install the tool?**

A:
```bash
git clone https://github.com/aliabdelaal-adm/AWA_Awarness_2025.git
cd AWA_Awarness_2025
pip install -r requirements.txt
```

**Q: Do I need to install FFmpeg separately?**

A: Yes, FFmpeg is required for video encoding:
- Ubuntu/Debian: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`
- Windows: Download from [ffmpeg.org](https://ffmpeg.org)

**Q: Can I use this tool offline?**

A: Partially. You need internet for the initial audio generation (using Edge TTS). However, you can configure it to use gTTS which works offline after the first download.

### Usage

**Q: What PDF formats are supported?**

A: The tool works best with text-based PDFs. Scanned PDFs may require OCR processing first.

**Q: How long does it take to generate a video?**

A: It depends on:
- PDF length (number of pages)
- Video resolution and quality settings
- TTS engine used
- Your computer's processing power

Typically, a 10-page PDF takes 5-10 minutes.

**Q: Can I customize the video style?**

A: Yes! Edit `config.yaml` to change:
- Video resolution
- Colors and fonts
- Transition effects
- Speech rate
- And more

**Q: What video formats are supported?**

A: The tool outputs MP4 videos by default, which is widely compatible. You can modify the code to support other formats supported by FFmpeg.

**Q: Can I add my own logo or watermark?**

A: Yes, the `VideoGenerator` class has an `add_logo()` method that you can implement. You'll need to provide your logo image.

### Troubleshooting

**Q: I get "PDF file not found" error**

A: Check:
1. The file path is correct
2. The file exists in the specified location
3. You have read permissions for the file

**Q: Audio generation is very slow**

A: This is usually due to:
- Slow internet connection (Edge TTS requires internet)
- Server load on TTS services
- Try using gTTS instead by setting `use_edge=False`

**Q: Video encoding fails with FFmpeg error**

A: Ensure:
1. FFmpeg is properly installed
2. FFmpeg is in your system PATH
3. You have write permissions in the output directory

**Q: The extracted text from PDF is garbled**

A: This can happen if:
- The PDF uses non-standard fonts
- The PDF is scanned (needs OCR)
- The PDF is password-protected

Try using a different PDF or convert it to a text-based format first.

**Q: Memory error during video generation**

A: Try:
1. Reduce video resolution in `config.yaml`
2. Process fewer pages at a time
3. Close other applications
4. Use a computer with more RAM

### Advanced

**Q: Can I integrate this with my own application?**

A: Yes! The tool is designed to be used both as a CLI tool and as a Python library. See `examples/advanced_usage.py` for examples.

**Q: Can I use a different TTS engine?**

A: Yes, you can add new TTS engines by modifying `src/modules/text_to_speech.py`. The code is modular and easy to extend.

**Q: Can I add AI narration with ChatGPT or Claude?**

A: The architecture supports this. You can add API calls to OpenAI or Anthropic in the text processing pipeline to enhance or rephrase content before TTS conversion.

**Q: Can I process multiple PDFs at once?**

A: Yes, see the batch processing example in `examples/advanced_usage.py`.

**Q: How do I contribute to the project?**

A: See `CONTRIBUTING.md` for guidelines. We welcome:
- Bug reports
- Feature requests
- Code contributions
- Documentation improvements

---

## العربية

### أسئلة عامة

**س: ما هي أداة AWA لتوليد الفيديوهات؟**

ج: هي تطبيق يعمل بالذكاء الاصطناعي يحول مستندات PDF تلقائياً إلى فيديوهات ترويجية وتعليمية وتوعوية احترافية مع تعليق صوتي مُولد بالذكاء الاصطناعي.

**س: ما اللغات المدعومة؟**

ج: حالياً، الأداة تدعم العربية والإنجليزية لمعالجة النصوص وتحويل النص إلى كلام.

**س: هل الأداة مجانية؟**

ج: نعم، الأداة مفتوحة المصدر ومجانية بموجب ترخيص MIT. ومع ذلك، قد تتطلب بعض الميزات اتصالاً بالإنترنت لخدمات الذكاء الاصطناعي.

### التثبيت والإعداد

**س: ما متطلبات النظام؟**

ج:
- Python 3.8 أو أحدث
- 4GB RAM كحد أدنى (8GB مستحسن)
- FFmpeg مثبت
- اتصال بالإنترنت (لـ TTS)
- 1GB مساحة حرة على القرص

**س: كيف أثبت الأداة؟**

ج:
```bash
git clone https://github.com/aliabdelaal-adm/AWA_Awarness_2025.git
cd AWA_Awarness_2025
pip install -r requirements.txt
```

**س: هل أحتاج لتثبيت FFmpeg بشكل منفصل؟**

ج: نعم، FFmpeg مطلوب لترميز الفيديو:
- Ubuntu/Debian: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`
- Windows: حمّل من [ffmpeg.org](https://ffmpeg.org)

**س: هل يمكنني استخدام الأداة بدون إنترنت؟**

ج: جزئياً. تحتاج إنترنت لتوليد الصوت الأولي (باستخدام Edge TTS). ومع ذلك، يمكنك تكوينها لاستخدام gTTS الذي يعمل بدون إنترنت بعد التحميل الأول.

### الاستخدام

**س: ما صيغ PDF المدعومة؟**

ج: تعمل الأداة بشكل أفضل مع ملفات PDF النصية. قد تتطلب ملفات PDF الممسوحة ضوئياً معالجة OCR أولاً.

**س: كم من الوقت يستغرق توليد فيديو؟**

ج: يعتمد على:
- طول PDF (عدد الصفحات)
- دقة وإعدادات جودة الفيديو
- محرك TTS المستخدم
- قوة معالج الكمبيوتر

عادةً، ملف PDF بـ 10 صفحات يستغرق 5-10 دقائق.

**س: هل يمكنني تخصيص نمط الفيديو؟**

ج: نعم! عدّل `config.yaml` لتغيير:
- دقة الفيديو
- الألوان والخطوط
- تأثيرات الانتقال
- سرعة الكلام
- والمزيد

**س: ما صيغ الفيديو المدعومة؟**

ج: الأداة تخرج فيديوهات MP4 افتراضياً، وهي متوافقة على نطاق واسع. يمكنك تعديل الكود لدعم صيغ أخرى يدعمها FFmpeg.

**س: هل يمكنني إضافة شعاري الخاص؟**

ج: نعم، فئة `VideoGenerator` لديها وظيفة `add_logo()` يمكنك تنفيذها. ستحتاج لتوفير صورة شعارك.

### حل المشاكل

**س: أحصل على خطأ "ملف PDF غير موجود"**

ج: تحقق من:
1. مسار الملف صحيح
2. الملف موجود في الموقع المحدد
3. لديك أذونات قراءة للملف

**س: توليد الصوت بطيء جداً**

ج: هذا عادة بسبب:
- اتصال إنترنت بطيء (Edge TTS يتطلب إنترنت)
- حمل الخادم على خدمات TTS
- جرب استخدام gTTS بدلاً من ذلك بتعيين `use_edge=False`

**س: يفشل ترميز الفيديو مع خطأ FFmpeg**

ج: تأكد من:
1. FFmpeg مثبت بشكل صحيح
2. FFmpeg في مسار النظام الخاص بك
3. لديك أذونات كتابة في دليل الإخراج

**س: النص المستخرج من PDF مشوه**

ج: قد يحدث هذا إذا:
- يستخدم PDF خطوط غير قياسية
- PDF ممسوح ضوئياً (يحتاج OCR)
- PDF محمي بكلمة مرور

حاول استخدام PDF مختلف أو حوله إلى صيغة نصية أولاً.

**س: خطأ في الذاكرة أثناء توليد الفيديو**

ج: جرب:
1. تقليل دقة الفيديو في `config.yaml`
2. معالجة صفحات أقل في المرة الواحدة
3. إغلاق التطبيقات الأخرى
4. استخدام كمبيوتر بذاكرة أكبر

### متقدم

**س: هل يمكنني دمج هذا مع تطبيقي الخاص؟**

ج: نعم! الأداة مصممة لاستخدامها كأداة CLI وككتبة Python. انظر `examples/advanced_usage.py` للأمثلة.

**س: هل يمكنني استخدام محرك TTS مختلف؟**

ج: نعم، يمكنك إضافة محركات TTS جديدة بتعديل `src/modules/text_to_speech.py`. الكود معياري وسهل التوسع.

**س: هل يمكنني إضافة سرد بالذكاء الاصطناعي مع ChatGPT أو Claude؟**

ج: البنية تدعم هذا. يمكنك إضافة استدعاءات API لـ OpenAI أو Anthropic في خط معالجة النص لتحسين أو إعادة صياغة المحتوى قبل تحويل TTS.

**س: هل يمكنني معالجة عدة ملفات PDF دفعة واحدة؟**

ج: نعم، انظر مثال المعالجة الدفعية في `examples/advanced_usage.py`.

**س: كيف أساهم في المشروع؟**

ج: انظر `CONTRIBUTING.md` للإرشادات. نرحب بـ:
- تقارير الأخطاء
- طلبات الميزات
- مساهمات الكود
- تحسينات التوثيق

---

## Contact & Support

- **GitHub Issues**: https://github.com/aliabdelaal-adm/AWA_Awarness_2025/issues
- **Documentation**: See README.md, USAGE.md, DEVELOPER.md

---

**Last Updated**: 2025-10-22
