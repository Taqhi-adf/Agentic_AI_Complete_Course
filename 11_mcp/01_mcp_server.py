# Level 10 – MCP (Model Context Protocol)

# MCP allows AI applications to connect with external tools
# and data sources through a standard protocol.

# Learn:
# - MCP architecture.
# - MCP client.
# - MCP server.
# - Tools.
# - Resources.
# - Prompts.
# - Tool discovery.
# - Server connections.
# - Permissions and security.

### Code 30: Build your first MCP server

# Install: pip install "mcp[cli]"

# Create `11_mcp/01_mcp_server.py`.

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MyFirstMCPServer")


# Tool 1: Addition
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


# Tool 2: Greeting
@mcp.tool()
def greet(name: str) -> str:
    """Greet a user."""
    return f"Hello {name}"


# start the MCP server
if __name__ == "__main__":
    mcp.run(transport="stdio")


# Run:python 11_mcp/01_mcp_server.py

# The server waits for an MCP client over standard input/output.
# To test it, connect an MCP client or use an MCP inspector.
