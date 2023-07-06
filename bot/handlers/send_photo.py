from aiogram import types
from loader import dp,bot,ADMIN, channel_id
from aiogram.filters import Text
from keyboards.inline.inline_keyboards import send_text_but
from keyboards.reply.reply_keyboards import get_reply_keyboard
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.senders_states import SendPhoto



async def add_photo(msg: types.Message, state: FSMContext):
    if str(msg.from_user.id) in ADMIN:
        await bot.send_message(chat_id= msg.chat.id, text='Введите текст и приложите фото в одном сообщении, данный пост будет отправлен в канал вместе с кнопкой Бот-менеджера',
                               reply_markup=get_reply_keyboard(['Отмена',],(1,)))
        await state.set_state(SendPhoto.photoState)
    else:
        await bot.send_message(chat_id= msg.chat.id, text='Вы не являетесь администратором бота, просьба покинуть данный чат')
        return

async def send_photo(msg: types.Message, state: FSMContext):
    if msg.caption:
        text_msg = msg.caption
        ikb_tb = send_text_but()
        await state.clear()
        if msg.content_type == 'photo':
            ph = msg.photo[0].file_id
            await bot.send_photo(chat_id= channel_id, photo=ph,
                            caption=text_msg, reply_markup=ikb_tb)
            await bot.send_message(chat_id=msg.chat.id, text = 'Пост успешно опубликован!', reply_markup=ReplyKeyboardRemove())
        else:
            await bot.send_message(chat_id=msg.chat.id, text = 'Вы не прикрепили фото, нажмите заново в меню пункт фото!', reply_markup=ReplyKeyboardRemove())
    else:
        await bot.send_message(chat_id=msg.chat.id, text = 'Вы не написали текст, нажмите заново в меню пункт фото!', reply_markup=ReplyKeyboardRemove())