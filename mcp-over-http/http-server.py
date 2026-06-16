from mcp.server.fastmcp import FastMCP
import random
import uvicorn

mcp = FastMCP("http-math-server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    """
    return a + b


@mcp.tool()
def random_quote() -> str:
    """
    Return random quote.
    """

    quotes = [
        "Protocols scale ecosystems.",
        "Observability enables autonomy.",
        "Infrastructure becomes intelligence."
    ]

    return random.choice(quotes)


if __name__ == "__main__":

    app = mcp.streamable_http_app()
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )