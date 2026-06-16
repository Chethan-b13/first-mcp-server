from mcp.server.fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("file-server")


@mcp.tool()
def read_file(path: str) -> str:

    file_path = Path(path)

    if not file_path.exists():
        return "File not found"

    return file_path.read_text()


if __name__ == "__main__":
    mcp.run()