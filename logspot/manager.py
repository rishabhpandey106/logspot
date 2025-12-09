import logging
import os
from .alerting import send_telegram
from typing import Optional

class LogManager:
    def __init__(self, service="app", log_dir="logs", telegram_chat_id: str | None = None, telegram_bot_token: Optional[str] = None):
        """
        Parameters
        ----------
        service : str
            Logical name of the service / app (used in log file name & messages)
        log_dir : str
            Directory where the log file will be stored.
        telegram_bot_token : str | None
            Telegram bot token. If None, will try os.getenv("TELEGRAM_BOT_TOKEN").
        telegram_chat_id : str | None
            Default chat id for alerts. If None, will try os.getenv("TELEGRAM_CHAT_ID").
        """
        self.service = service
        self.log_dir = log_dir
        os.makedirs(log_dir, exist_ok=True)

        self.log_file = os.path.join(log_dir, f"{service}.log")
        self.logger = logging.getLogger(service)
        self.logger.setLevel(logging.DEBUG)  

        if not self.logger.handlers:
            handler = logging.FileHandler(self.log_file, encoding="utf-8")
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.propagate = False

        self.telegram_bot_token = telegram_bot_token
        self.telegram_chat_id = telegram_chat_id
        logging.getLogger("werkzeug").setLevel(logging.ERROR)
        logging.getLogger("faiss").setLevel(logging.ERROR)

    def info(self, msg: str):
        self.logger.info(msg)

    def debug(self, msg: str):
        self.logger.debug(msg)

    def warn(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str, *, notify: bool = False, chat_id: str | None = None):
        """
        Log an ERROR. If notify=True, send Telegram alert.
        chat_id override allowed; else uses default telegram_chat_id.
        """
        self.logger.error(msg)
        if notify:
            target = chat_id or self.telegram_chat_id
            send_telegram(f"[{self.service}] ERROR: {msg}", target, self.telegram_bot_token)

    def critical(self, msg: str, *, notify: bool = True, chat_id: str | None = None):
        """
        Log a CRITICAL error. By default notify=True.
        """
        self.logger.critical(msg)
        target = chat_id or self.telegram_chat_id
        send_telegram(f"[{self.service}] CRITICAL: {msg}", target, self.telegram_bot_token)