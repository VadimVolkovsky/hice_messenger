from sqlalchemy.ext.asyncio import AsyncSession


async def update_user_message_counter(
        user,
        session: AsyncSession,
):
    """Обновляем счетик сообщений в профиле пользователя"""
    user.message_counter += 1
    session.add(user)
    return user, session


async def update_message_counter_for_message(
        message,
        user,
        session: AsyncSession,
):
    """Обновляем счетик сообщений пользователя в объекте сообщения"""
    message.message_counter = user.message_counter
    session.add(message)
    return message, session


async def commit_updates_in_db(
    message,
    user,
    session: AsyncSession
):
    await session.commit()
    await session.refresh(message)
    await session.refresh(user)
    return message, user
