import os
import logging
import openai
#import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from langdetect import detect

from logic import ai_response
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)

telegram_api = os.environ.get("TELEGRAM_API")
openai.api_key = os.environ.get("OPENAI_API")


bot = Bot(token=telegram_api)
dp = Dispatcher(bot)

welcome_text = " Hello! I am your personal Telegram bot that will do all your tasks much faster than you and with higher accuracy. I am able to do tasks in a fast and convenient way using AI. Do you want to know more?Then write to me on this topic!"

@dp.message_handler(Command(['start','help']))
async def send_welcome(message: types.Message):
    await message.answer(welcome_text)
    



@dp.message_handler(~Command('start'))
async def answer(message: types.Message):
    lang = detect(message.text)
    print(f"[+]",{message.from_id},{lang},":",message.text)
    user_text = (f"{message.text}")
    await message.answer(text=ai_response(user_text))
    print("[+] Reply has been sent!")
    
    
if __name__ == '__main__':
    executor.start_polling(dp)