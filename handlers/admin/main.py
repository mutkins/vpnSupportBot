from aiogram import Dispatcher
from handlers.admin.actions import send_message_to_user
from dotenv import load_dotenv
import os
load_dotenv()


def register_admin_handlers(dp: Dispatcher):
    # this handler activates only when admin replied message
    dp.register_message_handler(send_message_to_user,
                                lambda message: message.from_user.id == int(os.environ.get('my_chat_id'))
                                                and bool(message.reply_to_message))