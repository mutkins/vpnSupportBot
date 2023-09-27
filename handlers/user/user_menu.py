from aiogram import types
from aiogram.types import InputFile
from create_bot import bot
from dotenv import load_dotenv
import os
load_dotenv()


async def send_welcome(message: types.Message):
    file = InputFile("content/welcome.png")
    await message.answer_photo(photo=file, caption='У вас проблема? Мы рядом. Опишите её, приложите скриншоты и прочие детали', parse_mode='HTML')


async def get_issue(message: types.Message):
    await message.answer("Ожидайте, вам ответит первый освободившийся оператор")
    await message.forward(chat_id=os.environ.get('my_chat_id'))

