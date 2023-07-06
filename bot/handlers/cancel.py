from aiogram.types import ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram import types


async def cancel_handler(msg: types.Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await msg.answer(
        "Действие отменено.",
        reply_markup=ReplyKeyboardRemove(),
    )