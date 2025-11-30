from .manager import LogManager
from .blueprint import create_logs_blueprint

def setup_logs(app, service="app"):
    manager = LogManager(service=service)
    bp = create_logs_blueprint(manager.log_file, download_name=f"{service}.log")
    app.register_blueprint(bp)

    app.log_info = manager.info
    app.log_debug = manager.debug
    app.log_warn = manager.warn
    app.log_error = manager.error
    app.log_critical = manager.critical

    return manager

