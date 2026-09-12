# 📖 API Documentation - AI Hacker Assistant

## Base URL
```
http://localhost:8000
```

## Endpoints

### 1️⃣ Health Check
**GET** `/health`

Check if the API is running

**Response:**
```json
{
  "status": "✅ AI Hacker Assistant is running!"
}
```

---

### 2️⃣ Chat Message
**POST** `/api/chat`

Send a message to the AI Assistant

**Request Body:**
```json
{
  "message": "كيف أحمي نظامي من الهجمات السيبرانية؟",
  "user_id": "user123"
}
```

**Response:**
```json
{
  "status": "success",
  "user_message": "كيف أحمي نظامي من الهجمات السيبرانية؟",
  "ai_response": "هناك عدة خطوات يمكنك اتخاذها...",
  "user_id": "user123"
}
```

---

### 3️⃣ Code Analysis
**POST** `/api/analyze`

Analyze code for security vulnerabilities

**Request Body:**
```json
{
  "code": "SELECT * FROM users WHERE id = " + user_input",
  "language": "python"
}
```

**Response:**
```json
{
  "status": "success",
  "language": "python",
  "vulnerabilities_found": 1,
  "analysis": "SQL Injection vulnerability detected...",
  "recommendations": [
    "استخدم parameterized queries",
    "تحقق من المدخلات"
  ]
}
```

---

### 4️⃣ Security Tips
**GET** `/api/security-tips`

Get security tips and best practices

**Query Parameters:**
- `category` (optional): Filter by category (e.g., "authentication")

**Response:**
```json
{
  "status": "success",
  "count": 3,
  "tips": [
    {
      "id": 1,
      "title": "استخدم كلمات مرور قوية",
      "description": "استخدم كلمات مرور طويلة...",
      "severity": "high",
      "category": "authentication"
    }
  ]
}
```

---

### 5️⃣ About
**GET** `/api/about`

Get information about the AI Hacker Assistant

**Response:**
```json
{
  "name": "🤖 AI Hacker Assistant",
  "description": "متخصص في الأمان السيبراني والهاكينج الأخلاقي",
  "version": "1.0.0",
  "features": [
    "محادثة ذكية عن الأمان",
    "تحليل الأكواد"
  ]
}
```

---

## Error Handling

All errors return a standardized format:

```json
{
  "detail": "خطأ في المعالجة"
}
```

## Authentication

Authentication will be added in future versions using JWT tokens.

## Rate Limiting

Rate limiting will be implemented in production to prevent abuse.

---

**Version:** 1.0.0
**Last Updated:** 2024
