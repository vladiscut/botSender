from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage


# import pandas as pd

token = 'your_token'

ADMIN = ['344150886', '358339266','690934300']

channel_id = '-1001780286274'

bot = Bot(token=token, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher()
