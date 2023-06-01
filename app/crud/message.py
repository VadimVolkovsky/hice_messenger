from datetime import datetime
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.message import Message

from typing import Optional
from app.models.user import User


class CRUDMessage(CRUDBase):
    async def get_user_messages_with_limit(
        self,
        session: AsyncSession,
        user: User,
        limit: Optional[int] = 10
    ):
        """Получить последние сообщения пользователя с указанным лимитом"""
        db_objs = await session.execute(select(self.model).where(
            and_(self.model.username == user.username,
                 self.model.create_date <= self.model.create_date)
        ).order_by(self.model.id.desc()).limit(limit))
        return db_objs.scalars().all()
    

message_crud = CRUDMessage(Message)
