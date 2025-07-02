# config.py

# Telegram API credentials
api_id = 123456  # Replace with your own from my.telegram.org
api_hash = 'your_api_hash_here'

# Session name (used for login session storage)
session_name = 'gift_userbot_session'

# Where to send updates (use '@channelusername' or chat ID)
target_chat = '@FragmentGiftUpdate'

# Poll interval (in seconds)
poll_interval = 300  # 5 minutes

# GiftChanges API endpoints
gift_api_base = 'https://cdn.changes.tg'
gift_ids_url = f'{gift_api_base}/gifts/id-to-name.json'

# Cache folder
cache_dir = 'cached'