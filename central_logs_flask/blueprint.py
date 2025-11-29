import os
from flask import Blueprint, Response, abort, request

def create_logs_blueprint(log_file: str, download_name: str = "logs.txt"):
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
        
        level = request.args.get("level")
        if level:
            level = level.upper().strip()

        search = request.args.get("search")
        if search:
            search = search.strip().lower()
        
        download_flag = request.args.get("download", "0").lower() in ("1", "true", "yes", "y")

        try:
            with open(log_file, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            abort(500, description=str(e))

        lines = data.strip().split("\n")
        if level:
            level_pattern = f"- {level} -"
            lines = [line for line in lines if level_pattern in line]
        
        if search:
            lines = [line for line in lines if search in line.lower()]
        
        if limit and len(lines) > limit:
            lines = lines[-limit:]

        final_text = "\n".join(lines) if lines else "(no matching logs)"

        headers = {}
        if download_flag:
            headers["Content-Disposition"] = f'attachment; filename="{download_name}"'

        return Response(final_text, mimetype="text/plain", headers=headers)

    return bp
