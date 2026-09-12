import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    
    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost:5432/ai_hacker"
    )
    
    # Server
    PORT = int(os.getenv("PORT", 8000))
    HOST = os.getenv("HOST", "0.0.0.0")
    DEBUG = os.getenv("DEBUG", "False") == "True"
    
    # CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
    
    # AI Model
    AI_MODEL = os.getenv("AI_MODEL", "gpt-3.5-turbo")
    AI_TEMPERATURE = float(os.getenv("AI_TEMPERATURE", "0.7"))

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = "sqlite:///test.db"

# Select config based on environment
config_name = os.getenv("FLASK_ENV", "development")
if config_name == "production":
    config = ProductionConfig()
elif config_name == "testing":
    config = TestingConfig()
else:
    config = DevelopmentConfig()
