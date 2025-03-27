# main.py

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.enums import ParseMode
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()  # Завантажує токени з .env

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: Message):
    await message.answer("Бот працює. Тестове повідомлення отримано.")

async def main():
    print("Бот запущено...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
