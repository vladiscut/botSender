from loader import bot
from aiogram import types

async def get_id_command(msg: types.Message):
      await bot.send_message(chat_id= msg.chat.id,
                        text=msg.chat.id)