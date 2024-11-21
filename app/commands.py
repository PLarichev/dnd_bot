from telegram import Update
from telegram.ext import CallbackContext
from db import get_session
from sqlmodel import select
from models import Users

# Функция-обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    user_tg_id = update.effective_user.id
    username = update.effective_user.username

    with next(get_session()) as session:
        # Проверяем, есть ли пользователь в базе
        user_in_db = session.exec(select(Users).where(Users.tg_id == user_tg_id)).one_or_none()
        # Если пользователь не найден, добавляем его в базу
        if not user_in_db:
            new_user = Users(username=username, tg_id=user_tg_id)
            session.add(new_user)
            session.commit()
            await update.message.reply_text('Теперь ты под колпаком')
        else:
            await update.message.reply_text('Ты уже в базе, погнали')


