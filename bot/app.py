import asyncio
from aiogram.filters import Command
from loader import dp, bot
from utils.set_bot_commands import set_default_commands
from states.senders_states import SendText
# from connectors.db_funct import create_table
from handlers.send_text import *
from handlers.cancel import *
from handlers.send_photo import *
from handlers.start_handler import *
from handlers.getid import *
from aiogram import F


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(bot)
    print('Bot Started!')

async def start():
    # dp.message.register(process_main_menu_command,Command(commands=['catalogue']))
    dp.message.register(cancel_handler,F.text=='Отмена')
    dp.message.register(start_bot,Command(commands=['start']))
    dp.message.register(add_text,Command(commands=['text']))
    dp.message.register(get_id_command,Command(commands=['getid']))
    dp.message.register(send_text,SendText.textState)
    dp.message.register(add_photo,Command(commands=['photo']))
    dp.message.register(send_photo,SendPhoto.photoState)
    dp.startup.register(on_startup)
    # try:
    await dp.start_polling(bot, skip_updates=True)
    # finally:
    #     await bot.session.close()

if __name__ == '__main__':
    # create_table()
    asyncio.run(start())

