from work_calendar_ru import WCR
from aiogram import Router

from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inline import work_days_keyboard


common_router = Router()


@common_router.message(Command('start'))
async def start_command(message: Message):
        await message.answer('Какой сегодня день недели?', reply_markup=work_days_keyboard)


@common_router.message(Command('work'))
async def work_command(message: Message):
    work_time = message.text.split()[1:]
    if len(work_time) == 4:
        global wcr
        wcr = WCR(start_hour=int(work_time[0]), start_minutes=int(work_time[1]), end_hour=int(work_time[2]), end_minutes=int(work_time[3]))


@common_router.message(Command('is_work'))
async def is_work_command(message: Message):
    if wcr.is_work_time() == True:
        await message.answer('Иди работай!>:(')
    else:
        await message.answer('Можешь отдохнуть:)')