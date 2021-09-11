from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
            types.BotCommand("help", "Shows help"),
            types.BotCommand("poll", "Sends test poll"),
            types.BotCommand("test", "Sends test message and reply to it"),
        ]
    )
