# from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

# from app.core.db import Base


# class User(SQLAlchemyBaseUserTable[int], Base):
#     pass


# from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(Base):
    """Условная модель пользователя"""
    username = Column(String, unique=True)
    message_counter = Column(Integer, default=0)
    # message = relationship('Message')
