from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from callbacks.Work_Day_callback import WorkDayCallback

monday = InlineKeyboardButton(text='Понедельник', callback_data=WorkDayCallback(
    day='work'
).pack())
tuesday = InlineKeyboardButton(text='Вторник', callback_data=WorkDayCallback(
    day='work'
).pack())
wednesday = InlineKeyboardButton(text='Среда', callback_data=WorkDayCallback(
    day='work'
).pack())
thursday = InlineKeyboardButton(text='Четверг', callback_data=WorkDayCallback(
    day='work'
).pack())
friday = InlineKeyboardButton(text='Пятница', callback_data=WorkDayCallback(
    day='work'
).pack())
saturday = InlineKeyboardButton(text='Суббота', callback_data=WorkDayCallback(
    day='chill'
).pack())
sunday = InlineKeyboardButton(text='Воскресенье', callback_data=WorkDayCallback(
    day='chill'
).pack())
work_days_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
])
