from pydantic_settings import BaseSettings

AUTHENTICATION_BACKENDS = [
    "apps.user.backends.MyAuthBackend",
    "django.contrib.auth.backends.ModelBackend",
]


class AuthSettings(BaseSettings):
    FIRST_RUN: bool = True  # Custom flag to check first run
    AUTH_USER_MODEL: str = "user.User"

    AUTHENTICATION_BACKENDS: list[str] = [
        "backends.MyAuthBackend",
        "django.contrib.auth.backends.ModelBackend",
    ]

    AUTH_PASSWORD_VALIDATORS: list[dict[str, str]] = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]


auth_config = AuthSettings()
