import logging
import sys
from mcp.server.fastmcp import FastMCP

# 配置详细日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

# 创建MCP实例
mcp = FastMCP("test_sse")

# 运行SSE服务
print("Starting SSE server...")
mcp.run(transport='sse')
