from datetime import datetime

from pydantic import BaseModel, Extra


class MessageCreate(BaseModel):
    """Схема создания сообщения"""
    username: str
    text: str

    class Config():
        extra = Extra.forbid


class MessageDB(MessageCreate):
    """Схема ответа при создании сообщения"""
    id: int
    text: str
    username: str
    create_date: datetime
    message_counter: int

    class Config:
        orm_mode = True
