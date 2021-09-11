from aiogram import types
from loader import dp, bot
from utils.misc.formatter import get_formatted_message
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command('test'))
async def test_poll(message: types.Message):
    bot_message = await bot.send_message(message.chat.id, "Test Message")
    await bot_message.reply(get_formatted_message(bot_message), parse_mode=types.ParseMode.HTML)
