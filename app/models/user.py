from sqlalchemy import Column, Integer, String

from app.core.db import Base


class User(Base):
    """Условная модель пользователя"""
    username = Column(String, unique=True)
    message_counter = Column(Integer, default=0)
