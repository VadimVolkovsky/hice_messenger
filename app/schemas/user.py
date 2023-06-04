from pydantic import BaseModel, Extra


class UserCreate(BaseModel):
    """Схема создания пользователя"""
    username: str
    message_counter: int = 0

    class Config():
        extra = Extra.forbid


class UserUpdate(UserCreate):
    """Схема обновления пользователя"""
    pass
