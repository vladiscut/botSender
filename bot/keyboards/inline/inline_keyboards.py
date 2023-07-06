from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def send_text_but():
    ikb = InlineKeyboardBuilder()
    ikb.button(text = 'Перейти к покупкам',url='https://t.me/FreshAndLush_Bot')
    ikb.button(text = 'Поддержка',url='https://t.me/ManagerMarketBuyer_bot')

    return ikb.as_markup()