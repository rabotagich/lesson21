import logging
from random import choice
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = '6610238403:AAH50T5dXUB6tZ6vo8YAjlOTUl5prNGdaQ0'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


answers = {
    'Привіт' : 'hello.txt',
    'Як справи' : 'howudoing.txt'
}


@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.answer(f'Привіт! Запитай в мене як справи, або скажи "Привіт" ')
    

@dp.message_handler()
async def echo(message : types.Message):
    if message.text in answers:
        with open(f'lesson21/answers/{answers[message.text]}', 'r', encoding='utf-8') as file:
            variants = file.read().split('\n')
            await message.answer(choice(variants))
    else:
        await message.answer('Я тебе не зрозумів,')
        
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

