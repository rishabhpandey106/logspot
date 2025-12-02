from .manager import LogManager
from .blueprint import create_logs_blueprint

def setup_logs(app, service="app", log_dir: str = "logs", telegram_chat_id: str | None = None):
    manager = LogManager(service=service, log_dir=log_dir, telegram_chat_id=telegram_chat_id)
    bp = create_logs_blueprint(manager.log_file, download_name=f"{service}.log")
    app.register_blueprint(bp)

    app.log_info = manager.info
    app.log_debug = manager.debug
    app.log_warn = manager.warn
    app.log_error = manager.error
    app.log_critical = manager.critical

    return manager

