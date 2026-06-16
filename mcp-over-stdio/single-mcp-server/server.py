from mcp.server.fastmcp import FastMCP
import random
from pathlib import Path

mcp = FastMCP("utility-server")


# ---------------------------------------------------
# MATH TOOLS
# ---------------------------------------------------

@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.
    """
    return a * b


# ---------------------------------------------------
# RANDOM TOOLS
# ---------------------------------------------------

@mcp.tool()
def random_number(min: int, max: int) -> int:
    """
    Generate random integer.
    """
    return random.randint(min, max)


@mcp.tool()
def random_quote() -> str:
    """
    Return motivational quote.
    """

    quotes = [
        "Stay hungry stay foolish",
        "Simplicity scales",
        "Make systems observable",
        "Build resilient infrastructure"
    ]

    return random.choice(quotes)


# ---------------------------------------------------
# FILE TOOLS
# ---------------------------------------------------

@mcp.tool()
def read_file(path: str) -> str:
    """
    Read text file content.
    """

    file_path = Path(path)

    if not file_path.exists():
        return "File not found"

    return file_path.read_text()


if __name__ == "__main__":
    mcp.run()
