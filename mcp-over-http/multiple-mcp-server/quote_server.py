from mcp.server.fastmcp import FastMCP
import random
import uvicorn

mcp = FastMCP("quote-server")


@mcp.tool()
def random_quote() -> str:

    quotes = [
        "Systems thinking scales.",
        "Observability is survival.",
        "Distributed systems are coordination problems.",
        "Protocol-first architecture wins."
    ]

    return random.choice(quotes)


app = mcp.streamable_http_app()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8003
    )
