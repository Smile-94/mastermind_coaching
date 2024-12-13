from pydantic import field_validator
from pydantic_settings import BaseSettings

from config.env import EnvironmentChoices, env_config
from config.django.security import security_config


class MiddlewareSettings(BaseSettings):
    MIDDLEWARE: list[str] = [
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    @field_validator("MIDDLEWARE", mode="after")
    @classmethod
    def add_remove_middleware(cls, value: list[str]) -> list[str]:
        match env_config.PROJECT_ENVIRONMENT:
            case EnvironmentChoices.LOCAL | EnvironmentChoices.LOCAL_CONTAINER:
                if security_config.DEBUG:
                    value = [
                        "corsheaders.middleware.CorsMiddleware",
                        "debug_toolbar.middleware.DebugToolbarMiddleware",
                    ] + value
                else:
                    value = [
                        "corsheaders.middleware.CorsMiddleware",
                    ] + value
                return value

            case EnvironmentChoices.TEST:
                value = [
                    "corsheaders.middleware.CorsMiddleware",
                ] + value
                return value

            case EnvironmentChoices.DEV:
                if security_config.DEBUG:
                    value = [
                        "corsheaders.middleware.CorsMiddleware",
                        "debug_toolbar.middleware.DebugToolbarMiddleware",
                    ] + value
                else:
                    value = [
                        "corsheaders.middleware.CorsMiddleware",
                    ] + value
                return value

            case EnvironmentChoices.CI_CD:
                value = [
                    "corsheaders.middleware.CorsMiddleware",
                ] + value
                return value

            case EnvironmentChoices.STAGING:
                value = [
                    "corsheaders.middleware.CorsMiddleware",
                ] + value
                return value

            case EnvironmentChoices.PRODUCTION:
                value = [
                    "corsheaders.middleware.CorsMiddleware",
                ] + value
                return value


middleware_config = MiddlewareSettings()