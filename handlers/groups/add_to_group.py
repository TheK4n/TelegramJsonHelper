from loader import dp, bot
from aiogram import types
from utils.misc.formatter import get_formatted_message


@dp.my_chat_member_handler()
async def add_bot_to_group(my_chat_member: types.ChatMemberUpdated):
    await bot.send_message(my_chat_member.from_user.id, get_formatted_message(my_chat_member),
                           parse_mode=types.ParseMode.HTML)