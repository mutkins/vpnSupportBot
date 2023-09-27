from aiogram import Dispatcher
from handlers.user.user_menu import *


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'старт'])
    dp.register_message_handler(get_issue)



