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


import asyncio

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    bot_user = loop.run_until_complete(get_bot_user())
    if bot_user:
        print(f"Bot User ID: {bot_user}")
    else:
        print("Failed to get bot user")
    loop.close()
