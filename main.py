from aiohttp import web
from core.verify import verify_request_signature
from utils.types import (
    InteractionType,
    InteractionResponseType,
    InteractionResponseFlags,
)
from core.command_handler import CommandHandler


async def interactions(request):
    if not await verify_request_signature(request):
        return web.Response(text="Bad request signature", status=401)

    json_data = await request.json()

    if json_data["type"] == InteractionType.PING:
        return web.json_response({"type": InteractionResponseType.PONG})

    if json_data["type"] == InteractionType.APPLICATION_COMMAND:
        handler = CommandHandler(json_data)
        result = await handler.execute()
        if result is not None:
            return web.json_response(result)

    return web.json_response(
        {
            "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
            "data": {
                "content": "Hello Buddy, This is a by default message for any unrecognized interaction.",
                "flags": InteractionResponseFlags.EPHEMERAL,
            },
        }
    )


app = web.Application()
app.router.add_post("/", interactions)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=3000)
