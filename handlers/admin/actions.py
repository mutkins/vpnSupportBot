from aiogram import types
from create_bot import bot


async def send_message_to_user(message: types.Message):
    # Send message to user, which message was forwarded and replied
    await bot.send_message(chat_id=message.reply_to_message.forward_from.id, text=message.text)




