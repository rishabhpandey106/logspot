import os
from flask import Blueprint, Response, abort, request

def create_logs_blueprint(log_file):
    bp = Blueprint("central_logs", __name__)

    @bp.route("/logs")
    def view_logs():
        if not os.path.exists(log_file):
            return Response("(no logs yet)", mimetype="text/plain")

        # ?limit=200 (default 200)
        try:
            limit = int(request.args.get("limit", 200))
        except ValueError:
            limit = 200

        if limit <= 0:
            limit = 200

        try:
            with open(log_file, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            abort(500, description=str(e))

        lines = data.strip().split("\n")
        last_lines = "\n".join(lines[-limit:])

        return Response(last_lines, mimetype="text/plain")

    return bp
