import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

interface Message {
  id: string;
  sender: 'user' | 'ai';
  content: string;
  timestamp: Date;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      sender: 'ai',
      content: '🤖 مرحباً! أنا مساعد الذكاء الاصطناعي المتخصص في الأمان السيبراني. كيف يمكنني مساعدتك؟',
      timestamp: new Date()
    }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!input.trim()) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      sender: 'user',
      content: input,
      timestamp: new Date()
    };

    setMessages([...messages, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post(`${API_BASE_URL}/api/chat`, {
        message: input
      });

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        sender: 'ai',
        content: response.data.ai_response,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        sender: 'ai',
        content: '❌ حدث خطأ في الاتصال بالخادم. يرجى المحاولة لاحقاً.',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="header">
        <h1>🤖 AI Hacker Assistant</h1>
        <p>متخصص في الأمان السيبراني والهاكينج الأخلاقي</p>
      </div>

      <div className="chat-container">
        <div className="messages">
          {messages.map(msg => (
            <div key={msg.id} className={`message ${msg.sender}`}>
              <div className="message-content">
                {msg.content}
              </div>
              <span className="timestamp">
                {msg.timestamp.toLocaleTimeString('ar-SA')}
              </span>
            </div>
          ))}
          {loading && (
            <div className="message ai">
              <div className="message-content loading">
                ⏳ جاري الرد...
              </div>
            </div>
          )}
        </div>

        <form onSubmit={handleSendMessage} className="input-form">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="اسأل عن الأمان السيبراني..."
            disabled={loading}
          />
          <button type="submit" disabled={loading || !input.trim()}>
            {loading ? '⏳' : '📤'}
          </button>
        </form>
      </div>
    </div>
  );
}

export default App;
