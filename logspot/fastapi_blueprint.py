import os
from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import PlainTextResponse

def create_logs_router(log_file: str, download_name: str = "logs.txt"):
    router = APIRouter()

    @router.get("/logs", response_class=PlainTextResponse)
    async def view_logs(
        limit: int = Query(200, ge=1),
        level: str | None = Query(None),
        search: str | None = Query(None),
        download: bool = Query(False)
    ):
        if not os.path.exists(log_file):
            return "(no logs yet)"

        try:
            with open(log_file, "r", encoding="utf-8") as f:
                data = f.read()
        except Exception as e:
            raise HTTPException(500, detail=str(e))

        lines = data.strip().split("\n")

        if level:
            level_pattern = f"- {level.upper().strip()} -"
            lines = [line for line in lines if level_pattern in line]

        if search:
            search = search.lower().strip()
            lines = [line for line in lines if search in line.lower()]

        if len(lines) > limit:
            lines = lines[-limit:]

        final_text = "\n".join(lines) if lines else "(no matching logs)"

        # attachment mode
        headers = {}
        if download:
            headers["Content-Disposition"] = f'attachment; filename="{download_name}"'

        return PlainTextResponse(final_text, headers=headers)

    return router
