from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage


# import pandas as pd

token = '5651209227:AAGT8midtTLyQMD2F2aCj2cEM9Z416gmxTU'

ADMIN = ['344150886', '358339266','690934300']

channel_id = '-1001780286274'

bot = Bot(token=token, parse_mode='HTML')
storage = MemoryStorage()
dp = Dispatcher()
