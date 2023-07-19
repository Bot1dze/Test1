from aiogram import Router
from aiogram.types import CallbackQuery

from callbacks.Work_Day_callback import WorkDayCallback

work_router = Router()


@work_router.callback_query(WorkDayCallback.filter())
async def handle_waifu_type(query: CallbackQuery, callback_data: WorkDayCallback):
    if callback_data.day == 'work':
        await query.message.answer('Давай проверим кое-что, напиши команду /work (час когда начинается работа) (минута когда начинается работа)\n (час когда кончается работа) (минута когда кончается работа)')
    else:
        await query.message.answer('Выходные прекрасны, не так ли?')