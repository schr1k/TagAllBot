import asyncio
import logging

from settings import settings
from src.bot import dp, bot, client
from src.router import router

dp.include_router(router)


async def main():
    if settings.PASSWORD is None:
        await client.start(phone=settings.PHONE)
    else:
        await client.start(phone=settings.PHONE, password=settings.PASSWORD)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
