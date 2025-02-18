from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.bot import client

router = Router()


@router.message(Command('all'))
async def mention_all(message: Message):
    chat_id = message.chat.id
    members = []

    async with client:
        async for user in client.iter_participants(chat_id):
            if not user.bot:
                if user.username:
                    members.append(f'@{user.username}')
                else:
                    members.append(f'<a href="tg://user?id={user.id}">{user.first_name}</a>')

    if members:
        text = ', '.join(members)
        await message.answer(text, parse_mode='HTML')
