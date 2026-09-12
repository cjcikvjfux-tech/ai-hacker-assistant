# 🤖 AI Hacker Assistant - مساعد الذكاء الاصطناعي للهاكينج الأخلاقي

## 📖 نبذة عن المشروع

تطبيق ذكاء اصطناعي متخصص في **الأمان السيبراني والهاكينج الأخلاقي**. يوفر المساعدة في:

- 🔍 اختبار الاختراق (Penetration Testing)
- 🛡️ تحليل الثغرات الأمنية
- 📚 تقديم نصائح أمنية متقدمة
- 🔐 تحليل أكواد البرمجة للثغرات
- 📊 توصيات الحماية والأمان

## 🚀 المميزات

✅ **محادثة ذكية** - واجهة chat تفاعلية
✅ **تحليل متقدم** - فحص الأكواد والأنظمة
✅ **قاعدة معرفية** - معلومات شاملة عن الأمان
✅ **توصيات فورية** - حلول واحترافية
✅ **واجهة حديثة** - Design احترافي وسهل الاستخدام

## 🛠️ التقنيات المستخدمة

### Backend
- **Python 3.9+**
- **FastAPI** - Framework سريع وحديث
- **OpenAI API / LLaMA** - نماذج AI
- **SQLAlchemy** - ORM لقاعدة البيانات
- **PostgreSQL** - قاعدة بيانات قوية

### Frontend
- **React 18+**
- **TypeScript**
- **Tailwind CSS** - Styling حديث
- **Axios** - HTTP Client

## 📁 هيكل المشروع

```
ai-hacker-assistant/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── config.py
│   └── routes/
│       ├── chat.py
│       └── analysis.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.tsx
│   └── package.json
├── database/
│   └── schema.sql
└── docs/
    └── API.md
```

## ⚙️ التثبيت والتشغيل

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## 📝 متطلبات البيئة

أنشئ ملف `.env` في مجلد backend:

```
OPENAI_API_KEY=your_key_here
DATABASE_URL=postgresql://user:password@localhost/ai_hacker
SECRET_KEY=your_secret_key
```

## 🔒 ملاحظة أمنية

**هذا المشروع مخصص للأغراض التعليمية والهاكينج الأخلاقي فقط.**

يجب استخدام هذه الأدوات فقط على الأنظمة التي تملكها أو لديك إذن من مالكها.

## 📞 التواصل والدعم

للأسئلة والاقتراحات، قم بإنشاء Issue جديد في المستودع.

## 📄 الترخيص

هذا المشروع مرخص تحت MIT License

---

**تم الإنشاء بواسطة GitHub Copilot** 🤖
