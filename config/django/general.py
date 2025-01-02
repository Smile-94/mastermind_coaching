from pathlib import PosixPath, Path
from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings
from django.contrib.messages import constants as messages


class GeneralSettings(BaseSettings):
    BASE_DIR: PosixPath = Field(
        default=Path(__file__).resolve().parent.parent.parent,
        frozen=True,
    )
    ALLOWED_HOSTS: list[str] = ["*"]

    ROOT_URLCONF: str = "routes.urls"
    APPEND_SLASH: bool = False

    ASGI_APPLICATION: str = "config.server.asgi.application"
    money_to_point: PositiveInt = Field(default=200, frozen=True)
    point_to_money: PositiveInt = Field(default=1, frozen=True)

    # Messages Setting

    MESSAGE_TAGS: dict = Field(default={messages.ERROR: "danger"})


general_config = GeneralSettings()
