import asyncio

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


SERVERS = [
    (
        "math",
        StdioServerParameters(
            command="python",
            args=["math_server.py"]
        )
    ),
    (
        "file",
        StdioServerParameters(
            command="python",
            args=["file_server.py"]
        )
    ),
    (
        "quote",
        StdioServerParameters(
            command="python",
            args=["quote_server.py"]
        )
    )
]


async def handle_server(name, server_params):

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print(f"\nSERVER: {name}")

            tools = await session.list_tools()

            for tool in tools.tools:
                print(f"  - {tool.name}")

            # Keep connection alive if needed
            await asyncio.sleep(2)


async def main():

    tasks = []

    for name, server in SERVERS:
        tasks.append(handle_server(name, server))

    await asyncio.gather(*tasks)


asyncio.run(main())