from typing import Any
from pydantic import Field, SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from config.env import env_config
from config.django.general import general_config


class DatabaseSettings(BaseSettings):
    """
    This class defines the setting configuration for this auth service
    """

    # General Database Configuration
    DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"

    # PostgreSQL Database Configuration
    POSTGRES_HOST: SecretStr = Field(default="localhost", frozen=True, repr=False)
    POSTGRES_PORT: int = Field(default=5432, frozen=True, repr=False)
    POSTGRES_DB: SecretStr = Field(default="postgres", frozen=True, repr=False)
    POSTGRES_USER: SecretStr = Field(default="postgres", frozen=True, repr=False)
    POSTGRES_PASSWORD: SecretStr = Field(default="postgres", frozen=True, repr=False)
    ATOMIC_DB: bool = Field(default=True, frozen=True, repr=False)

    # Redis Configuration
    REDIS_HOST: SecretStr = Field(default="localhost", frozen=True, repr=False)
    REDIS_PORT: int = Field(default=6379, frozen=True, repr=False)

    model_config = SettingsConfigDict(
        env_file=env_config.env_file,
        extra="ignore",
        case_sensitive=True,
    )

    # @computed_field()
    # def DATABASES(self) -> dict[str, Any]:
    #     return {
    #         "default": {
    #             "ENGINE": "django.db.backends.postgresql",
    #             "NAME": self.POSTGRES_DB.get_secret_value(),
    #             "USER": self.POSTGRES_USER.get_secret_value(),
    #             "PASSWORD": self.POSTGRES_PASSWORD.get_secret_value(),
    #             "HOST": self.POSTGRES_HOST.get_secret_value(),
    #             "PORT": self.POSTGRES_PORT,
    #         },
    #     }

    @computed_field()
    def DATABASES(self) -> dict[str, Any]:
        return {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": general_config.BASE_DIR / "db.sqlite3",
            }
        }


db_config = DatabaseSettings()
