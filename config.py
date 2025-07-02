# config.py

# Telegram API credentials
api_id = 21585498  # Replace with your own from my.telegram.org
api_hash = '873031a00ca632c3c9750a18fa983687'

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
