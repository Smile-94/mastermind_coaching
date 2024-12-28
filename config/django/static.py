import os
from pathlib import PosixPath, Path
from typing import Any
from pydantic_settings import BaseSettings
from config.django.general import general_config
from pydantic import Field


class StaticSettings(BaseSettings):
    """
    This class defines the setting configuration for this auth service
    """

    STATIC_URL: str = "static/"
    STATIC_DIR: Path = general_config.BASE_DIR / "static"
    STATIC_ROOT: Path = os.path.join(general_config.BASE_DIR, "staticfiles")
    # STATICFILES_STORAGE: str = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATICFILES_DIRS: list[PosixPath] = [STATIC_DIR]
    STORAGES: dict[str, dict[str, Any]] = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

    MEDIA_URL: str = "/media/"
    MEDIA_ROOT: PosixPath = os.path.join(general_config.BASE_DIR, "media")


static_config = StaticSettings()
