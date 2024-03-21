from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
import asyncio

bot = Bot(token = TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)
if __name__ == "__main__":
    asyncio.run(main())