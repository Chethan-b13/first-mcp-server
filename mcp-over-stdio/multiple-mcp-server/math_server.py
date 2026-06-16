from mcp.server.fastmcp import FastMCP

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


if __name__ == "__main__":
    mcp.run()