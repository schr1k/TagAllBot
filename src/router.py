from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from telethon.tl.types import PeerChannel, PeerChat

from src.bot import client

router = Router()


@router.message(Command('all'))
async def mention_all(message: Message):
    chat_id = message.chat.id
    members = []

    async with client:
        await client.get_dialogs()
        if str(chat_id).startswith('-100'):
            entity = await client.get_entity(PeerChannel(chat_id))
        else:
            entity = await client.get_entity(PeerChat(abs(chat_id)))

        async for user in client.iter_participants(entity):
            if not user.bot:
                if user.username:
                    members.append(f'@{user.username}')
                else:
                    members.append(f'<a href="tg://user?id={user.id}">{user.first_name}</a>')

    if members:
        text = ', '.join(members)
        await message.answer(text, parse_mode='HTML')
