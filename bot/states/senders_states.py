from aiogram.fsm.state import State, StatesGroup

class SendText(StatesGroup):
    textState = State()


class SendPhoto(StatesGroup):
    photoState = State()