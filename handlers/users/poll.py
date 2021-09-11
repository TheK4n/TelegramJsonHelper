from aiogram.dispatcher.filters.builtin import Command
from loader import dp, bot
from aiogram import types
from utils.misc.formatter import get_formatted_message


@dp.message_handler(Command('poll'))
async def test_poll(message: types.Message):
    await bot.send_poll(message.chat.id, 'TestPool', ['answer1', 'answer2', 'answer3'],
                        is_anonymous=False,
                        reply_to_message_id=message.message_id,
                        allows_multiple_answers=True)


@dp.poll_answer_handler()
async def test_poll_answer(poll: types.PollAnswer):
    await bot.send_message(poll.user.id, get_formatted_message(poll), parse_mode=types.ParseMode.HTML)
