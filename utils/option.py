from .types import ApplicationCommandOptionType


class Option:
    def __init__(
        self,
        name: str,
        type: ApplicationCommandOptionType,
        description: str = "...",
        required: bool = False,
    ):
        self.name = name
        self.description = description
        self.type = type
        self.required = required

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "type": self.type.value,
            "required": self.required,
        }
