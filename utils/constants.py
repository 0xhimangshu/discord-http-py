base_url = "https://discord.com/api/v10"
cdn_url = "https://cdn.discordapp.com"


def bot_header(token: str):
    return {
        "Authorization": f"Bot {token}",
        "User-Agent": "DiscordBot (https://github.com/0xhimangshu)",
    }


default_avatar = "https://cdn.discordapp.com/embed/avatars/0.png"
