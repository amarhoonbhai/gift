# helpers.py

import os
import json
import aiohttp
from config import cache_dir

def ensure_cache_dir():
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

def cache_path(name):
    return os.path.join(cache_dir, f'{name}.json')

def load_cache(name):
    path = cache_path(name)
    if os.path.exists(path):
        with open(path, 'r') as f:
            return json.load(f)
    return {}

def save_cache(name, data):
    path = cache_path(name)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.json()
    return {}

async def image_exists(url):
    async with aiohttp.ClientSession() as session:
        async with session.head(url) as resp:
            return resp.status == 200