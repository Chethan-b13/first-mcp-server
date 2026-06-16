from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("math-server")


@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b


@mcp.tool()
def square(number: int) -> int:
    return number * number


app = mcp.streamable_http_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001
    )