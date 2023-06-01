# import logging
# from datetime import datetime
# from logging.handlers import RotatingFileHandler
# from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'hice messenger'
    app_description: str = 'Мессенджер для банка'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()


# def configure_logging():
#     """Описание конфигурации для логирования"""
#     LOGS_DIR.mkdir(exist_ok=True)
#     rotating_handler = RotatingFileHandler(
#         LOG_FILE, maxBytes=10**6, backupCount=5, encoding='utf-8'
#     )

#     logging.basicConfig(
#         datefmt=DR_FORMAT,
#         format=LOG_FORMAT,
#         level=logging.INFO,
#         handlers=(rotating_handler,)
#     )
