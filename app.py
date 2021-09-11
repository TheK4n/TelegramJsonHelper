#!/usr/bin/env python3.9

from aiogram import executor

from loader import dp
import middlewares, handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    print("Bot started")

async def on_shutdown(dispatcher):
    print("Bot stoped")
    dispatcher.stop_polling()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
