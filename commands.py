import sys

import aiohttp
from utils.constants import cdn_url
from core.bot import get_bot_user
from core.user import get_user
from utils.command import SlashCommand
from utils.option import Option
from utils.types import (
    ApplicationCommandOptionType,
    ButtonStyle,
    ComponentType,
    InteractionResponseType,
)


class Hello(SlashCommand):
    def __init__(self):
        super().__init__(
            name="hello",
            description="Say hello to someone",
            options=[
                Option(
                    name="user",
                    type=ApplicationCommandOptionType.USER,
                    description="The user to say hello",
                    required=True,
                ),
            ],
        )

    async def respond(self, json_data: dict):
        user_id = json_data["data"]["options"][0]["value"]
        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {
                "content": f"Hello <@!{user_id}>",
            },
        }


class Bye(SlashCommand):
    def __init__(self):
        super().__init__(
            name="bye",
            description="Say bye to someone",
            options=[
                Option(
                    name="user",
                    type=ApplicationCommandOptionType.USER,
                    description="The user to say bye",
                    required=True,
                ),
            ],
        )

    async def respond(self, json_data: dict):
        user_id = json_data["data"]["options"][0]["value"]
        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {
                "content": f"Bye <@!{user_id}>",
            },
        }


class Avatar(SlashCommand):
    def __init__(self):
        super().__init__(
            name="avatar",
            description="Displays someone's avatar",
            options=[
                Option(
                    name="user",
                    type=ApplicationCommandOptionType.USER,
                    description="The user whose avatar you want to see",
                    required=False,
                ),
            ],
        )

    async def respond(self, json_data: dict):
        # print(f"{json_data}")
        user_id = (
            json_data["data"]["options"][0]["value"]
            if json_data.get("data") and json_data["data"].get("options")
            else None
        )

        if user_id is not None:
            user_data = await get_user(user_id=user_id)
            avatar_url = (
                f"{cdn_url}/avatars/{user_id}/{user_data['avatar']}.png?size=1024"
            )
            user_name = user_data["username"]
            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "embeds": [
                        {
                            "author": {"name": user_name, "icon_url": avatar_url},
                            "image": {"url": avatar_url},
                            "color": 0x2B2D31,
                        }
                    ]
                },
            }

        else:
            avatar_url = f"{cdn_url}/avatars/{json_data['member']['user']['id']}/{json_data['member']['user']['avatar']}.png?size=1024"
            return {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {
                    "embeds": [
                        {
                            "author": {
                                "name": json_data["member"]["user"]["username"],
                                "icon_url": avatar_url,
                            },
                            "image": {"url": avatar_url},
                            "color": 0x2B2D31,
                        }
                    ],
                },
            }


class BotInfo(SlashCommand):
    def __init__(self):
        super().__init__(name="botinfo", description="Show information about me")

    async def respond(self, json_data: dict):
        bot_data = await get_bot_user()
        username = bot_data["username"]
        avatar = f"https://cdn.discordapp.com/avatars/{bot_data['id']}/{bot_data['avatar']}.png?size=1024"

        return {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {
                "embeds": [
                    {
                        "author": {
                            "name": f"{username}'s information",
                            "icon_url": avatar,
                        },
                        "description": (
                            "I'm a Discord bot\n"
                            "Made by [0xhimangshu](https://discord.com/users/775660503342776341)\n"
                            f"With `aiohttp v{aiohttp.__version__}` <:aiohttp_plain:1257296912831352874>\n"
                            f"And `python v{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}` <:py:1168608526768275537>"
                        ),
                        "color": 0x2B2D31,
                        "thumbnail": {"url": avatar},
                        "footer": {"text": "Under heavy development 🛠️"},
                    }
                ],
                "components": [
                    {
                        "type": 1,
                        "components": [
                            {
                                "type": 2,
                                "label": "Invite",
                                "style": ButtonStyle.LINK,
                                "url": "https://discord.com/oauth2/authorize?client_id=1245347232803454976",
                            }
                        ],
                    }
                ],
            },
        }


commands = [Hello(), Bye(), Avatar(), BotInfo()]
