import logging
from mcp.server.fastmcp import FastMCP

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('simple_sse')

# 创建MCP实例
mcp = FastMCP("simple_sse")

# 添加一个简单的工具
@mcp.tool()
def hello(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

# 运行SSE服务
if __name__ == "__main__":
    logger.info("Starting SSE server...")
    mcp.run(transport='sse')
