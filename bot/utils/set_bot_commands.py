from aiogram import types

async def set_default_commands(bot):
    commands=[
            # types.BotCommand(command = "video", description= "Видео"),
            types.BotCommand(command = "text", description= "Текстовое сообщение"),
            # types.BotCommand(command = "quiz", description= "Викторина"),
            types.BotCommand(command = "photo", description= "Отправить пост с фото"),
            # types.BotCommand(command = "document", description= "Документ"),
        ]
    await bot.set_my_commands(commands)
