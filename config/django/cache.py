from typing import Any
from pydantic import Field, computed_field
from pydantic_settings import BaseSettings
from config.django.database import db_config


class CacheSettings(BaseSettings):
    """
    This class defines the setting configuration for this auth service
    """

    CACHE_TTL: int = 60 * 1500
    REDIS_CACHE_BACKEND: str = Field(
        default="django.core.cache.backends.redis.RedisCache",
        frozen=True,
        repr=False,
    )

    @computed_field()
    def CACHES(self) -> dict[str, Any]:
        return {
            "default": {
                "BACKEND": self.REDIS_CACHE_BACKEND,
                "LOCATION": f"redis://{db_config.REDIS_HOST.get_secret_value()}:{db_config.REDIS_PORT}",
                "OPTIONS": {
                    # 'PASSWORD': 'yourpassword',  # Make sure this line is commented out or removed
                },
            },
        }


cache_config = CacheSettings()
