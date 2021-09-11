from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from utils.misc.formatter import get_formatted_message


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(get_formatted_message(await bot.me))
