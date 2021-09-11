
from aiogram import types
from loader import dp
from utils.misc.formatter import json_formatter


@dp.message_handler(
    content_types=['text', 'document', 'audio', 'photo', 'sticker',
                   'video', 'video_note', 'voice', 'location', 'contact'])
async def bot_start(message: types.Message):
    await message.reply('<code>' + json_formatter(str(message)) + '</code>', parse_mode=types.ParseMode.HTML)
