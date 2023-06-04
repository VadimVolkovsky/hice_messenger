from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.core.db import Base


class Message(Base):
    """Модель сообщений"""
    text = Column(Text)
    username = Column(String)
    create_date = Column(DateTime, default=datetime.now, nullable=False)
    message_counter = Column(Integer, default=0)
