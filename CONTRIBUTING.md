# Contributing to AWA AI Video Generation Tool
# المساهمة في أداة AWA لتوليد الفيديوهات

Thank you for your interest in contributing to the AWA AI Video Generation Tool! This document provides guidelines for contributing to the project.

شكراً لاهتمامك بالمساهمة في أداة AWA لتوليد الفيديوهات! يوفر هذا المستند إرشادات للمساهمة في المشروع.

---

## How to Contribute / كيفية المساهمة

### Reporting Bugs / الإبلاغ عن الأخطاء

If you find a bug, please open an issue on GitHub with:

إذا وجدت خطأ، يرجى فتح مشكلة على GitHub مع:

- **Clear description** / وصف واضح
- **Steps to reproduce** / خطوات إعادة الإنتاج
- **Expected behavior** / السلوك المتوقع
- **Actual behavior** / السلوك الفعلي
- **System information** (OS, Python version, etc.) / معلومات النظام
- **Error messages and logs** / رسائل الخطأ والسجلات

### Suggesting Features / اقتراح الميزات

We welcome feature suggestions! Please open an issue with:

نرحب باقتراحات الميزات! يرجى فتح مشكلة مع:

- **Clear description of the feature** / وصف واضح للميزة
- **Use case** / حالة الاستخدام
- **Why it would be useful** / لماذا ستكون مفيدة
- **Possible implementation approach** / نهج التنفيذ المحتمل

### Code Contributions / مساهمات الكود

1. **Fork the repository** / انسخ المستودع
2. **Create a feature branch** / أنشئ فرع ميزة
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** / قم بإجراء تغييراتك
4. **Test your changes** / اختبر تغييراتك
5. **Commit with clear messages** / التزم برسائل واضحة
   ```bash
   git commit -m "Add feature: description"
   ```
6. **Push to your fork** / ادفع إلى نسختك
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** / افتح طلب سحب

---

## Development Guidelines / إرشادات التطوير

### Code Style / نمط الكود

- Follow PEP 8 style guide for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Comment complex logic

**Example**:
```python
def process_text_chunk(text: str, max_length: int = 300) -> list:
    """
    Split text into chunks of specified maximum length.
    
    Args:
        text: Input text to split
        max_length: Maximum characters per chunk
        
    Returns:
        List of text chunks
    """
    # Implementation
    pass
```

### Testing / الاختبار

- Test your changes before submitting
- Add tests for new features when possible
- Ensure existing tests still pass
- Test with both Arabic and English content

### Documentation / التوثيق

- Update README.md if adding user-facing features
- Update DEVELOPER.md for technical changes
- Add comments for complex code
- Update FAQ.md for common questions
- Provide examples when appropriate

### Commit Messages / رسائل الالتزام

Use clear, descriptive commit messages:

- ✅ Good: "Add support for PDF password protection"
- ✅ Good: "Fix audio sync issue in video generation"
- ✅ Good: "Improve error handling in TTS module"
- ❌ Bad: "Fix bug"
- ❌ Bad: "Update code"
- ❌ Bad: "Changes"

---

## Areas for Contribution / مجالات المساهمة

### High Priority / أولوية عالية

- [ ] Support for more TTS engines (AWS Polly, Azure TTS, etc.)
- [ ] OCR support for scanned PDFs
- [ ] Video template system enhancements
- [ ] Performance optimizations
- [ ] Better error handling and recovery
- [ ] Progress tracking and estimation

### Medium Priority / أولوية متوسطة

- [ ] Support for more video formats
- [ ] Subtitle/caption generation
- [ ] Background music support
- [ ] Image extraction from PDFs
- [ ] Multi-language support (add more languages)
- [ ] GUI interface

### Low Priority / أولوية منخفضة

- [ ] Social media optimization (Instagram, TikTok formats)
- [ ] Cloud deployment guides
- [ ] Docker containerization
- [ ] API server mode
- [ ] Video editing features
- [ ] Advanced transitions and effects

---

## Pull Request Process / عملية طلب السحب

1. **Ensure your PR**:
   - Has a clear description
   - References related issues
   - Includes tests (if applicable)
   - Updates documentation
   - Follows code style guidelines

2. **PR Review**:
   - Maintainers will review your PR
   - Address feedback and comments
   - Make requested changes
   - Keep PR focused and small

3. **After Approval**:
   - PR will be merged by maintainers
   - Your contribution will be acknowledged
   - Thank you for contributing!

---

## Code of Conduct / قواعد السلوك

### Our Pledge / تعهدنا

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:

- Experience level
- Gender identity and expression
- Sexual orientation
- Disability
- Personal appearance
- Body size
- Race
- Ethnicity
- Age
- Religion
- Nationality

### Expected Behavior / السلوك المتوقع

- Be respectful and considerate
- Welcome newcomers warmly
- Give and accept constructive feedback gracefully
- Focus on what's best for the project
- Show empathy towards others

### Unacceptable Behavior / السلوك غير المقبول

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Any conduct that could be considered inappropriate

---

## Questions? / أسئلة؟

If you have questions about contributing:

- Open an issue labeled "question"
- Check the FAQ.md file
- Review DEVELOPER.md for technical details

---

## Recognition / التقدير

Contributors will be:
- Listed in project documentation
- Acknowledged in release notes
- Appreciated for their valuable contributions

---

## License / الترخيص

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to AWA AI Video Generation Tool!

شكراً لمساهمتك في أداة AWA لتوليد الفيديوهات!

---

**Maintained by**: AWA Awareness Team
**Contact**: GitHub Issues
