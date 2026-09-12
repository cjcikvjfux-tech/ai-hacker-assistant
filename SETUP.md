# 🚀 دليل التثبيت والتشغيل

## المتطلبات الأساسية

- Python 3.9+
- Node.js 18+
- PostgreSQL 12+ (اختياري - يمكن استخدام Docker)
- Git

## التثبيت السريع

### 1️⃣ استنساخ المستودع

```bash
git clone https://github.com/cjcikvjfux-tech/ai-hacker-assistant.git
cd ai-hacker-assistant
```

### 2️⃣ إعداد Backend

```bash
cd backend

# إنشاء بيئة افتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
# على Windows:
venv\Scripts\activate
# على Mac/Linux:
source venv/bin/activate

# تثبيت المتطلبات
pip install -r requirements.txt

# نسخ ملف البيئة
cp .env.example .env

# تعديل .env وأضف مفتاح OpenAI API
# OPENAI_API_KEY=your_key_here

# تشغيل الخادم
python app.py
```

سيبدأ الخادم على `http://localhost:8000`

### 3️⃣ إعداد Frontend

```bash
cd frontend

# تثبيت المتطلبات
npm install

# نسخ ملف البيئة
cp .env.example .env

# تشغيل التطبيق
npm run dev
```

سيبدأ التطبيق على `http://localhost:5173`

## التشغيل باستخدام Docker

### المتطلبات

- Docker
- Docker Compose

### الخطوات

```bash
# في مجلد المشروع الرئيسي

# 1. إنشاء ملف .env
cp backend/.env.example .env

# 2. تعديل .env وأضف مفتاح OpenAI API

# 3. تشغيل التطبيقات
docker-compose up -d

# 4. التحقق من الحالة
docker-compose ps
```

سيكون التطبيق متاحاً على:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- Database: `localhost:5432`

### إيقاف التطبيقات

```bash
docker-compose down
```

## الاختبار

### اختبار Backend

```bash
cd backend
pytest
```

### اختبار الـ API

```bash
# الحصول على قائمة التلميحات الأمنية
curl http://localhost:8000/api/security-tips

# إرسال رسالة للمساعد الذكي
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "كيف أحمي نظامي؟"}'
```

## المشاكل الشائعة

### 1. خطأ: "No module named 'fastapi'"

```bash
# تأكد من تفعيل البيئة الافتراضية
source venv/bin/activate  # على Mac/Linux
venv\Scripts\activate     # على Windows

# أعد تثبيت المتطلبات
pip install -r requirements.txt
```

### 2. خطأ: "Connection refused" من الـ Frontend

```bash
# تأكد من أن الخادم يعمل على المنفذ 8000
# وأن عنوان API صحيح في .env
VITE_API_URL=http://localhost:8000
```

### 3. خطأ: "Database connection failed"

```bash
# تأكد من تشغيل PostgreSQL
# أو استخدم Docker
docker-compose up db
```

## الخطوات التالية

1. ✅ اقرأ [توثيق الـ API](./docs/API.md)
2. ✅ استكشف [البنية](./README.md#-هيكل-المشروع)
3. ✅ ساهم في المشروع بـ Pull Request

---

**هل تواجه مشكلة؟** أنشئ [Issue](https://github.com/cjcikvjfux-tech/ai-hacker-assistant/issues) جديداً 🐛
