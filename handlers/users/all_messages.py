from aiogram import types
from loader import dp
from utils.misc.formatter import get_formatted_message

content_types = ['text', 'document', 'audio', 'photo', 'sticker', 'video', 'video_note',
                 'voice', 'contact', 'dice', 'poll', 'venue', 'animation', 'location']


@dp.edited_message_handler(content_types=content_types)
@dp.message_handler(content_types=content_types)
async def all_messages_handler(message: types.Message):
    await message.reply(get_formatted_message(message), parse_mode=types.ParseMode.HTML)
