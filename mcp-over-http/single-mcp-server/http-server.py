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

app = mcp.streamable_http_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )