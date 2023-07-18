from aiogram import Router
from aiogram.types import CallbackQuery

from callbacks.Work_Day_callback import WorkDayCallback
from keyboards.inline import work_days_keyboard

work_router = Router()


@work_router.callback_query(WorkDayCallback.filter())
async def handle_waifu_type(query: CallbackQuery, callback_data: WorkDayCallback):
    if callback_data.work_day == 'work':
        await query.message.answer('Давай проверим кое-что, напиши команду /work (час когда начинается работа) (минута когда начинается работа)\n (час когда кончается работа) (минута когда кончается работа)', reply_markup=work_days_keyboard)
    else:
        await query.message.answer('Выходные прекрасны, не так ли?')