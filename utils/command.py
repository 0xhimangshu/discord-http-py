class SlashCommand:
    def __init__(self, name: str, description: str = "...", options: list = None):
        self.name = name
        self.description = description
        self.options = options or []

    async def respond(self, json_data: dict): ...

    def to_dict(self):
        return {
            "type": 1,  # Slash command
            "name": self.name,
            "description": self.description,
            "options": [option.to_dict() for option in self.options],
        }
