from mcp.server.fastmcp import FastMCP
from pathlib import Path
import uvicorn

mcp = FastMCP("file-server")


@mcp.tool()
def read_file(path: str) -> str:

    file_path = Path(path)

    if not file_path.exists():
        return "File not found"

    return file_path.read_text()


app = mcp.streamable_http_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8002
    )