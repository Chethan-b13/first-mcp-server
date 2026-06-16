import asyncio
import json

from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama

from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


# ---------------------------------------------------
# STATE
# ---------------------------------------------------

class AgentState(TypedDict):
    user_input: str
    response: str


# ---------------------------------------------------
# LOAD MCP TOOLS
# ---------------------------------------------------

async def load_tools():

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )
    # Use a short-lived session to fetch available tools.
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()

    return tools, server_params


# ---------------------------------------------------
# AGENT NODE
# ---------------------------------------------------

async def agent_node(state: AgentState):

    user_input = state["user_input"]

    tools, server_params = await load_tools()

    print("\nAVAILABLE MCP TOOLS:\n")

    for tool in tools.tools:
        print(f"- {tool.name}")

    llm = ChatOllama(model="llama3.1")

    tool_descriptions = tools.model_dump_json(indent=2)

    prompt = f"""
    You are an intelligent assistant.

    Available tools:

    {tool_descriptions}

    User request:
    {user_input}

    Decide:
    1. Which tool to use
    2. What arguments to pass

    Return ONLY valid JSON:

    {{
        "tool": "...",
        "arguments": {{ ... }}
    }}
    """

    response = llm.invoke(prompt)

    tool_request = json.loads(response.content)

    tool_name = tool_request["tool"]
    arguments = tool_request["arguments"]

    print("\nTOOL SELECTED:\n")
    print(tool_name, arguments)

    # Open a fresh session for invoking the selected tool so the
    # underlying stdio streams are open while the call executes.
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(tool_name, arguments)

    return {
        "response": str(result)
    }


# ---------------------------------------------------
# BUILD GRAPH
# ---------------------------------------------------

builder = StateGraph(AgentState)

builder.add_node("agent", agent_node)

builder.set_entry_point("agent")

builder.add_edge("agent", END)

graph = builder.compile()


# ---------------------------------------------------
# RUN
# ---------------------------------------------------

async def main():

    user_query = input("\nEnter request: ")

    result = await graph.ainvoke({
        "user_input": user_query
    })

    print("\nFINAL RESPONSE:\n")
    print(result["response"])


if __name__ == "__main__":
    asyncio.run(main())
