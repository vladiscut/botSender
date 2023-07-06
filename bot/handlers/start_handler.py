from aiogram import types
from loader import ADMIN, bot


async def start_bot(msg: types.Message):
    if str(msg.from_user.id) in ADMIN:
        await bot.send_message(chat_id= msg.chat.id, text='Данный бот отправлет пост с кнопкой в канал, чтобы создать и отправить пост, выберете нужный пункт в меню')
    else:
        await bot.send_message(chat_id= msg.chat.id, text='Вы не являетесь администратором бота, просьба покинуть данный чат')
        return