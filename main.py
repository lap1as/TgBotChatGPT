import os
import logging
import openai
import json
from aiogram import Bot, Dispatcher, executor, types

from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)

telegram_api = os.environ.get("TELEGRAM_API")
openai.api_key = os.environ.get("OPENAI_API")


bot = Bot(token=telegram_api)
dp = Dispatcher(bot)

@dp.message_handler()
async def send_welcome(message: types.Message):
    print(f"[+]",{message.from_id},":",message.text)
    prompt = (f"{message.text}")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1
    )
    generated = response.choices[0].text
    await message.answer(text=generated)
    
    
if __name__ == '__main__':
    executor.start_polling(dp)