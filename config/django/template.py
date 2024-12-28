from typing import Any
from pydantic_settings import BaseSettings
from config.django.general import general_config


class TemplateSettings(BaseSettings):
    TEMPLATES: list[dict[str, Any]] = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [general_config.BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]


template_config = TemplateSettings()
