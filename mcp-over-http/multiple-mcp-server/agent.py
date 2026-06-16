import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


SERVERS = [
    ("math", "http://localhost:8001/mcp"),
    ("file", "http://localhost:8002/mcp"),
    ("quote", "http://localhost:8003/mcp"),
]


async def handle_server(name, url):

    async with streamable_http_client(url) as (read, write, _):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print(f"\nSERVER: {name}")

            tools = await session.list_tools()

            for tool in tools.tools:
                print(f"  - {tool.name}")


async def main():

    tasks = []

    for name, url in SERVERS:
        tasks.append(handle_server(name, url))

    await asyncio.gather(*tasks)


asyncio.run(main())