import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


async def main():

    async with streamable_http_client(
        "http://127.0.0.1:8000/mcp"
    ) as (read, write, _):

        async with ClientSession(read, write) as session:

            await session.initialize()

            tools = await session.list_tools()

            print("\nAVAILABLE TOOLS:\n")

            for tool in tools.tools:
                print(f"- {tool.name}")

            result = await session.call_tool(
                "add",
                {
                    "a": 10,
                    "b": 20
                }
            )

            print("\nTOOL RESULT:\n")
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
