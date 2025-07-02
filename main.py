# main.py

import asyncio
from telethon import TelegramClient
from telethon.tl.types import InputMediaPhotoExternal

from config import api_id, api_hash, session_name, target_chat, poll_interval
from helpers import image_exists, ensure_cache_dir
from gift_tracker import detect_new_gifts

client = TelegramClient(session_name, api_id, api_hash)

async def send_gift_post(gift_id, gift_name):
    image_url = f"https://cdn.changes.tg/original/{gift_id}.png"

    message = (
        f"<b>🎁 New TON Gift Drop Detected!</b>\n\n"
        f"<b>Name:</b> <code>{gift_name}</code>\n"
        f"<b>ID:</b> <code>{gift_id}</code>\n\n"
        f"<b>🔔 Follow <a href='https://t.me/FragmentGiftUpdate'>@FragmentGiftUpdate</a> for rare TON gifts!</b>"
    )

    if await image_exists(image_url):
        await client.send_file(
            target_chat,
            InputMediaPhotoExternal(url=image_url),
            caption=message,
            parse_mode='html'
        )
    else:
        await client.send_message(target_chat, message, parse_mode='html')

async def run_bot():
    await client.start()
    ensure_cache_dir()
    print("🤖 Gift tracker running...")

    while True:
        new_gifts = await detect_new_gifts()
        for gift_id, gift_name in new_gifts:
            print(f"📢 New gift: {gift_name} ({gift_id})")
            await send_gift_post(gift_id, gift_name)
        await asyncio.sleep(poll_interval)

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(run_bot())