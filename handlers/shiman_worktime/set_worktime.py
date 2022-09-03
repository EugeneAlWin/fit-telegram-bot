from aiogram import types
from aiogram.dispatcher.filters import Command
from bot import disp
from handlers.shiman_worktime.states.ShimanWorktime import ShimanWorktime
from aiogram.dispatcher import FSMContext
from db import db_cursor, db
from db_api.get_shiman_wt_db import get_shiman_wt_from_db
from db_api.set_shiman_wt_db import set_shiman_wt_db


@disp.message_handler(Command('setshiman'), state=None)
async def start_set(message: types.Message):
    old_wt = get_shiman_wt_from_db()
    await message.answer(old_wt)
    await message.answer("Это текущее расписание.\nСкопируйте, поправьте и отправьте новое. Проверьте правильность.")
    await ShimanWorktime.Q1.set()


@disp.message_handler(state=ShimanWorktime.Q1)
async def stop_set(message: types.Message, state: FSMContext):
    new_wt = message.text
    old_wt = get_shiman_wt_from_db()
    result = set_shiman_wt_db(old_wt, new_wt)
    await message.answer('Расписание установлено' if result else 'Ошибка обновления')
    await state.finish()
