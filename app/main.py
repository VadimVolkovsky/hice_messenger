from fastapi import FastAPI

from app.api.routers import main_router
from app.core.config import  settings # configure_logging

# configure_logging()
app = FastAPI(
    title=settings.app_title,
    description=settings.app_description)

app.include_router(main_router)
