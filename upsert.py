from requests import Request, Session
from commands import commands
from config import token, application_id

s = Session()
s.headers.update({"Authorization": f"Bot {token}"})

r = s.send(
    s.prepare_request(
        Request(
            "PUT",
            f"https://discord.com/api/v10/applications/{application_id}/commands",
            json=[c.to_dict() for c in commands],
        )
    )
)

print(f"{r.json()}")
