import logging
import os

class LogManager:
    def __init__(self, service="app", log_dir="logs"):
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

        logging.getLogger("werkzeug").setLevel(logging.ERROR)
        logging.getLogger("faiss").setLevel(logging.ERROR)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
