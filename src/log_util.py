import datetime
import logging
import os
import threading as th

import requests
from dotenv import load_dotenv

load_dotenv()

__all__ = ("logger",)


class WebhookHandler(logging.StreamHandler):
    __WEBHOOK_URL = os.environ["LOGGING__WEBHOOK_URL"]

    def emit(self, record: logging.LogRecord):
        try:
            requests.post(
                WebhookHandler.__WEBHOOK_URL,
                json={"content": self.format(record)}
            )
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


level = os.environ["LOGGING__LEVEL"]
logger = logging.getLogger("discord_bot")
logger.setLevel(level=level)

formatter = logging.Formatter(
    "[{asctime}] [{levelname}] {message}", "%Y-%m-%d %H:%M:%S",
    style="{"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logging_path = os.environ["LOGGING__PATH"]
date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
log_file = f"{logging_path}/{date}.log"
file_handler = logging.FileHandler(filename=log_file, encoding="utf-8", mode="a")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

webhook_handler = WebhookHandler()
webhook_handler.setFormatter(formatter)
logger.addHandler(webhook_handler)

logger.info("bot running supaaa fast")
