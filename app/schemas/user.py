# from fastapi_users import schemas


# class UserRead(schemas.BaseUser[int]):
#     pass


# class UserCreate(schemas.BaseUserCreate):
#     pass


# class UserUpdate(schemas.BaseUserUpdate):
#     pass

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field


class UserCreate(BaseModel):
    """Схема создания юзера"""
    username: str
    message_counter: int = 0

    class Config():
        extra = Extra.forbid


class UserUpdate(UserCreate):
    """ """
    pass
    