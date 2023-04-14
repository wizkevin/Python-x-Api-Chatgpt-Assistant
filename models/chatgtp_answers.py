from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ChatGptAnswer(Base):
    __tablename__ = 'chat_gpt_answers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    input = Column(String(120), unique=True)
    answer = Column(String(120))

    def __repr__(self):
        return f'<ChatGptAnswer {self.input}: {self.answer}>'
    
__all__ = ['Base', 'ChatGptAnswer']
