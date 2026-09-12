from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn
from typing import Optional

# Load environment variables
load_dotenv()

app = FastAPI(
    title="🤖 AI Hacker Assistant API",
    description="Cybersecurity & Ethical Hacking AI Assistant",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ChatMessage(BaseModel):
    message: str
    user_id: Optional[str] = "anonymous"
    
class AnalysisRequest(BaseModel):
    code: str
    language: str = "python"

class SecurityTip(BaseModel):
    title: str
    description: str
    severity: str  # low, medium, high, critical

# Routes
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "🤖 AI Hacker Assistant API",
        "version": "1.0.0",
        "endpoints": {
            "chat": "/api/chat",
            "analyze": "/api/analyze",
            "tips": "/api/security-tips",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "✅ AI Hacker Assistant is running!"}

@app.post("/api/chat")
async def chat(message: ChatMessage):
    """
    Chat endpoint for AI Assistant
    """
    try:
        # Placeholder response - will integrate with OpenAI
        response = {
            "status": "success",
            "user_message": message.message,
            "ai_response": f"🤖 Processing your security inquiry: {message.message[:30]}...",
            "user_id": message.user_id
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze")
async def analyze_code(request: AnalysisRequest):
    """
    Analyze code for security vulnerabilities
    """
    try:
        analysis = {
            "status": "success",
            "language": request.language,
            "vulnerabilities_found": 0,
            "analysis": "Code analysis in progress...",
            "recommendations": [
                "Use parameterized queries to prevent SQL injection",
                "Implement input validation",
                "Use secure password hashing"
            ]
        }
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/security-tips")
async def get_security_tips(category: Optional[str] = None):
    """
    Get security tips and best practices
    """
    tips = [
        {
            "id": 1,
            "title": "استخدم كلمات مرور قوية",
            "description": "استخدم كلمات مرور طويلة تحتوي على أحرف وأرقام ورموز",
            "severity": "high",
            "category": "authentication"
        },
        {
            "id": 2,
            "title": "تفعيل المصادقة الثنائية (2FA)",
            "description": "استخدم التحقق من خطوتين لحماية حساباتك",
            "severity": "critical",
            "category": "authentication"
        },
        {
            "id": 3,
            "title": "تحديث البرامج بانتظام",
            "description": "قم بتحديث جميع البرامج والتطبيقات بانتظام",
            "severity": "high",
            "category": "maintenance"
        }
    ]
    
    if category:
        tips = [t for t in tips if t["category"] == category]
    
    return {
        "status": "success",
        "count": len(tips),
        "tips": tips
    }

@app.get("/api/about")
async def about():
    """About the AI Hacker Assistant"""
    return {
        "name": "🤖 AI Hacker Assistant",
        "description": "متخصص في الأمان السيبراني والهاكينج الأخلاقي",
        "version": "1.0.0",
        "features": [
            "محادثة ذكية عن الأمان",
            "تحليل الأكواد",
            "نصائح أمنية",
            "اختبار الاختراق",
            "تقارير الأمان"
        ]
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )
