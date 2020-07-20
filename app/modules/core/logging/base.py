import logging
from typing import Optional, Dict

from django.conf import settings


def custom_capture_message(
    msg: str, level: str, extra: Optional[Dict] = None, **kwargs
) -> None:
    if settings.APP_ENV in ["stage", "prod"]:
        from sentry_sdk import capture_message, configure_scope  # NOQA

        if extra:
            with configure_scope() as scope:
                for key, value in extra.items():
                    scope.set_extra(key, value)
                capture_message(message=msg, level="warning", **kwargs)
        else:
            capture_message(message=msg, level="warning", **kwargs)
    else:
        logger = {
            "critical": logging.critical,
            "error": logging.error,
            "warning": logging.warning,
            "info": logging.info,
            "debug": logging.debug,
        }
        logger.get(level, logging.error)(msg=msg)
