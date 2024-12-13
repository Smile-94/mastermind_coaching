from pydantic import field_validator
from pydantic_settings import BaseSettings

from config.env import EnvironmentChoices, env_config
from config.django.security import security_config


class InstalledAppsSettings(BaseSettings):
    THIRD_PARTY_PACKAGE: list[str] = [
        "rest_framework",
        "rangefilter",
        "drf_spectacular",
    ]

    LOCAL_APPS: list[str] = [
        "apps.user.apps.UserConfig",
    ]

    INSTALLED_APPS: list[str] = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        *THIRD_PARTY_PACKAGE,
        *LOCAL_APPS,
    ]

    @field_validator("INSTALLED_APPS", mode="after")
    def add_remove_apps(cls, value: list[str]) -> list[str]:
        match env_config.PROJECT_ENVIRONMENT:
            case EnvironmentChoices.LOCAL | EnvironmentChoices.LOCAL_CONTAINER:
                if security_config.DEBUG:
                    value = (
                        [
                            "corsheaders",
                            "debug_toolbar",
                        ]
                        + value
                        + ["phonenumber_field"]
                    )
                else:
                    value = (
                        [
                            "corsheaders",
                        ]
                        + value
                        + ["phonenumber_field"]
                    )

                return value

            case EnvironmentChoices.TEST:
                value = (
                    [
                        "corsheaders",
                    ]
                    + value
                    + ["phonenumber_field"]
                )
                return value

            case EnvironmentChoices.DEV:
                if security_config.DEBUG:
                    value = (
                        [
                            "corsheaders",
                            "debug_toolbar",
                        ]
                        + value
                        + ["phonenumber_field"]
                    )
                else:
                    value = (
                        [
                            "corsheaders",
                        ]
                        + value
                        + ["phonenumber_field"]
                    )

                return value

            case EnvironmentChoices.CI_CD:
                value = (
                    [
                        "corsheaders",
                    ]
                    + value
                    + ["phonenumber_field"]
                )
                return value

            case EnvironmentChoices.STAGING:
                value = (
                    [
                        "corsheaders",
                    ]
                    + value
                    + ["phonenumber_field"]
                )
                return value

            case EnvironmentChoices.PRODUCTION:
                value = (
                    [
                        "corsheaders",
                    ]
                    + value
                    + ["phonenumber_field"]
                )
                return value


installed_apps_config = InstalledAppsSettings()
