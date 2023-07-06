from aiogram import types
from loader import dp,bot,ADMIN, channel_id
from aiogram.filters import Text
from keyboards.inline.inline_keyboards import send_text_but
from keyboards.reply.reply_keyboards import get_reply_keyboard
from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from states.senders_states import SendText


"""Это наш бот менеджер, он может принимать ваш заказ, так же вы можете задать ему вопрос, после чего первый освободившийся оператор ответит вам"""

async def add_text(msg: types.Message, state: FSMContext):
    if str(msg.from_user.id) in ADMIN:
        await bot.send_message(chat_id= msg.chat.id, text='Введите текст, который хотите отправить в канал вместе с кнопкой Бот-менеджера',
                               reply_markup=get_reply_keyboard(['Отмена',],(1,)))
        await state.set_state(SendText.textState)
    else:
        await bot.send_message(chat_id= msg.chat.id, text='Вы не являетесь администратором бота, просьба покинуть данный чат')
        return

async def send_text(msg: types.Message, state: FSMContext):
    text_msg = msg.text
    ikb_tb = send_text_but()
    await state.clear()
    await bot.send_message(chat_id= channel_id,
                        text=text_msg, reply_markup=ikb_tb)
    await bot.send_message(chat_id=msg.chat.id, text = 'Пост успешно опубликован!', reply_markup=ReplyKeyboardRemove())
    
