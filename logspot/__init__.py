from .manager import LogManager
from .blueprint import create_logs_blueprint
from .fastapi_blueprint import create_logs_router
from typing import Optional

def setup_logs(app, service="app", log_dir: str = "logs", telegram_chat_id: str | None = None, telegram_bot_token: Optional[str] = None):
    manager = LogManager(service=service, log_dir=log_dir, telegram_chat_id=telegram_chat_id, telegram_bot_token=telegram_bot_token)
    download_name = f"{service}.log"
    
    # Flask
    if hasattr(app, "register_blueprint"):
        bp = create_logs_blueprint(manager.log_file, download_name=download_name)
        app.register_blueprint(bp)

    # FastAPI
    elif hasattr(app, "include_router"):
        router = create_logs_router(manager.log_file, download_name=download_name)
        app.include_router(router)
    
    else:
        raise RuntimeError("Unsupported application type: must be Flask or FastAPI")

    app.log_info = manager.info
    app.log_debug = manager.debug
    app.log_warn = manager.warn
    app.log_error = manager.error
    app.log_critical = manager.critical

    return manager

