import os
import logging
import openai
#import json
from aiogram import Bot, Dispatcher, executor, types
from langdetect import detect

from logic import ai_response

from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)

telegram_api = os.environ.get("TELEGRAM_API")
openai.api_key = os.environ.get("OPENAI_API")


bot = Bot(token=telegram_api)
dp = Dispatcher(bot)

@dp.message_handler()
async def send_welcome(message: types.Message):
    lang = detect(message.text)
    print(f"[+]",{message.from_id},{lang},":",message.text)
    user_text = (f"{message.text}")
    await message.answer(text=ai_response(user_text))
    print("[+] Reply has been sent!")
    
    
if __name__ == '__main__':
    executor.start_polling(dp)