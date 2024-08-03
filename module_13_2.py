from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = 'dkfdkjfhdkjfhdjkfdjkfhk895749875'#Ромдомные токены, не используйте их в реальной работе
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    print(f'Мы получили собщение {message.text} ')
    await message.answer( 'Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    if message.text == 'привет':
        print(f'Мы получили сообщение {message.text} ')
        await message.answer('Введите команду /start, чтобы начать общение.')
    elif message.text == 'start':
        print(f'Мы получили собщение {message.text} ')
        await message.answer('Привет! Я бот помогающий твоему здоровью.')
    else:
        print(f'Мы получили сообщение {message.text} ')
        await message.answer('Извините, но я не знаю такую команду.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)