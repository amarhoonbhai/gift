# gift_tracker.py

from config import gift_ids_url
from helpers import load_cache, save_cache, fetch_json

async def detect_new_gifts():
    cached_gifts = load_cache('gifts')
    current_gifts = await fetch_json(gift_ids_url)

    if not current_gifts:
        return []

    new_items = []
    for gift_id, gift_name in current_gifts.items():
        if gift_id not in cached_gifts:
            new_items.append((gift_id, gift_name))

    if new_items:
        save_cache('gifts', current_gifts)

    return new_items