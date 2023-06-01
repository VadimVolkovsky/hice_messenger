# получает JSON-сообщение, содержащее имя отправителя и текст, 
# и сохраняет его в базу данных (выбор конкретной базы данных не имеет принципиального значения)

# • возвращает JSON с последними 10 (или меньшим количеством, если история не накопилась) сообщениями, включая текущее
# • каждое сообщение в ответе должно содержать имя отправителя, текст сообщения, дату отправки, 
# порядковый номер сообщения и количество сообщений от текущего пользователя

# [
#     {
#         "id": "Порядковый номер сообщения",
#         "text": "Текст сообщения",
#         "username": "Имя отправителя",
#         "date": "Дата отправки",
#         "counter": "количество сообщений от текущего пользователя"
#     }
# ]

from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text

from app.core.db import Base


class Message(Base):
    """Модель сообщений"""
    text = Column(Text)
    username = Column(String)
    create_date = Column(DateTime, default=datetime.now, nullable=False)
    message_counter = Column(Integer, default=0)
    # username = Column(String, ForeignKey('user.name'))
    # message_counter = Column(Integer, ForeignKey('user.message_counter'))
