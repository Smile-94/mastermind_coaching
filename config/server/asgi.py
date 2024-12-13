import os
import sys
from loguru import logger
from django.core.asgi import get_asgi_application
from pydantic import ValidationError as PydanticError


def shutdown():
    # Sending a shutdown signal to uvicorn
    logger.info("Shutting down the server.")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django")

try:
    application = get_asgi_application()
except PydanticError as error:
    logger.error(error.errors())
    shutdown()
    sys.exit(500)
    os._exit(1)