-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat Sessions Table
CREATE TABLE chat_sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat Messages Table
CREATE TABLE chat_messages (
    id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES chat_sessions(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id),
    sender VARCHAR(50) NOT NULL, -- 'user' or 'ai'
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Code Analysis Table
CREATE TABLE code_analysis (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    code_snippet TEXT NOT NULL,
    language VARCHAR(50),
    vulnerabilities_found INTEGER,
    analysis_result TEXT,
    severity VARCHAR(50), -- low, medium, high, critical
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Security Tips Table
CREATE TABLE security_tips (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100),
    severity VARCHAR(50),
    tags VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_user_id ON chat_sessions(user_id);
CREATE INDEX idx_session_id ON chat_messages(session_id);
CREATE INDEX idx_created_at ON chat_messages(created_at);
CREATE INDEX idx_severity ON code_analysis(severity);
