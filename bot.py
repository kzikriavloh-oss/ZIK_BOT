from aiogram import Bot, Dispatcher, types
import asyncio
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def music(message: types.Message):
    q = message.text.replace(" ", "+")
    link = f"https://www.youtube.com/results?search_query={q}"
    await message.answer(f"🎵 Вот что я нашёл:\n{link}")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
