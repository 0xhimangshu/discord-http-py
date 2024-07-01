import aiohttp
from utils.constants import base_url, bot_header
from config import token


async def get_user(user_id: str):
    async with aiohttp.ClientSession(headers=bot_header(token)) as session:
        async with session.get(f"{base_url}/users/{user_id}") as response:
            if response.status == 200:
                return await response.json()
            else:
                return None
