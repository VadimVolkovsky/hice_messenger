from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.message import message_crud
from app.crud.user import user_crud
from app.models.user import User
from app.schemas.message import MessageCreate, MessageDB
from app.schemas.user import UserCreate
# from app.services import update_user_message_counter
from app.services.other_services import update_user_message_counter, commit_updates_in_db, update_message_counter_for_message


router = APIRouter()

@router.post(
    '/message/',
    # response_model=MessageDB,
    # response_model_exclude=('user_id', 'invested_amount', 'fully_invested'),
    # response_model_exclude_none=True
)
async def create_message(
    message: MessageCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Создает новое сообщение"""
    username = message.username
    message = await message_crud.create(
        message,
        session,
    )
    user = await user_crud.get_user_by_username(
        username,
        session
    )
    if user is None:
        user = UserCreate(username=message.username, message_counter=0)
        user = await user_crud.create(user, session)
    print(f'Счетчик сообщений юзера 1: {user.message_counter}')
    user, session = await update_user_message_counter(user, session)
    print(f'Счетчик сообщений юзера 2: {user.message_counter}')
    message, session = await update_message_counter_for_message(message, user, session)
    message, user = await commit_updates_in_db(message, user, session)
    messages = await message_crud.get_user_messages_with_limit(session, user)
    return messages
