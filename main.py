from aiogram.utils import executor
from create_bot import dp
from handlers import register_all_handlers


register_all_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
