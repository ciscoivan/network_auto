#!/usr/bin/env python3
# 测试网络设备巡检模块启动

import sys
import os
import logging

# 配置详细日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger('test_network_tools')

def main():
    logger.info("开始测试网络设备巡检模块...")
    
    try:
        # 将当前目录添加到Python的导入路径中
        sys.path.insert(0, os.path.abspath("."))
        
        logger.info("导入network_tools包...")
        from network_tools.main import mcp
        
        logger.info(f"成功导入mcp实例: {mcp}")
        logger.info(f"mcp名称: {mcp.name}")
        
        # 检查注册的工具数量
        logger.info("检查注册的工具...")
        # 注意：FastMCP可能没有直接的工具列表属性，我们尝试其他方式
        
        logger.info("尝试启动MCP服务...")
        # 使用非阻塞方式启动，以便捕获错误
        import threading
        
        def start_mcp():
            try:
                mcp.run(transport='sse', port=8001)
            except Exception as e:
                logger.error(f"MCP服务启动失败: {type(e).__name__}: {str(e)}")
                import traceback
                traceback.print_exc()
        
        # 在后台线程中启动MCP服务
        thread = threading.Thread(target=start_mcp)
        thread.daemon = True
        thread.start()
        
        # 等待3秒，查看是否有错误输出
        import time
        time.sleep(3)
        
        logger.info("测试完成")
        return 0
        
    except Exception as e:
        logger.error(f"测试失败: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
