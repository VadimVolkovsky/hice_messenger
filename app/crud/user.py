from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.user import User


class CRUDUser(CRUDBase):
    async def get_user_by_username(
        self,
        username,
        session: AsyncSession
    ):
        """Поиск пользователя в БД по полю username"""
        user = await session.execute(
            select(User).where(
                User.username == username
            ).with_for_update(key_share=True)
        )
        return user.scalars().first()


user_crud = CRUDUser(User)
