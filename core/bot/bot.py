import aiohttp

from config import token
from utils.constants import base_url, bot_header


async def get_bot_user():
    async with aiohttp.ClientSession(headers=bot_header(token=token)) as session:
        async with session.get(f"{base_url}/users/@me") as response:
            if response.status == 200:
                return await response.json()
            else:
                return None
