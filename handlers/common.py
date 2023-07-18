from work_calendar_ru import WCR
from aiogram import Router

from aiogram.filters import Command, callback_data
from aiogram.types import Message
from keyboards.inline import work_days_keyboard
from callbacks.Work_Day_callback import WorkDayCallback


common_router = Router()


@common_router.message(Command('start'))
async def start_command(message: Message):
        await message.answer('Какой сегодня день недели?', reply_markup=work_days_keyboard)


@common_router.message(Command('work'))
async def work_command(message: Message):
    work_time = message.text.split()[1:]
    if len(work_time) == 4:
        wcr = WCR(start_hour=int(work_time[0]), start_minutes=int(work_time[1]), end_hour=int(work_time[2]), end_minutes=int(work_time[3]))
        if  wcr.is_work_time() == True:
            await message.answer('Иди работай!>:(')
        else:
            await message.answer('Можешь отдохнуть:)')