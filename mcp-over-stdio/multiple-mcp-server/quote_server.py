from mcp.server.fastmcp import FastMCP
import random

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


if __name__ == "__main__":
    mcp.run()
