### Code 31: MCP client

# Create `11_mcp/02_mcp_client.py`.

import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    # Configure MCP server
    server = StdioServerParameters(command="python", args=["11_mcp/01_mcp_server.py"])

    # Connect to MCP server
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize connection
            await session.initialize()

            # Get available tools
            tools = await session.list_tools()

            print("\nAvailable MCP Tools:")

            for tool in tools.tools:
                print("-", tool.name)

            # Call addition tool
            result = await session.call_tool("add", arguments={"a": 10, "b": 20})

            print("\nAddition Result:")

            for content in result.content:
                if content.type == "text":
                    print(content.text)

            # Call greeting tool
            greeting = await session.call_tool("greet", arguments={"name": "Taqhi"})

            print("\nGreeting Result:")

            for content in greeting.content:
                if content.type == "text":
                    print(content.text)


# Execute asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())

# Run the client from your course root directory.
