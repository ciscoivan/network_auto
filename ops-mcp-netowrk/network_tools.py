#!/usr/bin/env python
# 网络工具集MCP入口文件

import sys
import os
import argparse

# 将当前目录添加到Python的导入路径中
sys.path.insert(0, os.path.abspath("."))

# 导入network_tools包中的主模块
from network_tools.main import mcp

if __name__ == "__main__":
    # 添加命令行参数解析
    parser = argparse.ArgumentParser(description='网络设备巡检MCP服务')
    parser.add_argument('--transport', type=str, default='sse', help='传输模式')
    args = parser.parse_args()
    
    try:
        # 运行MCP服务，使用指定的传输模式
        mcp.run(transport=args.transport)
    except Exception as e:
        print(f"运行错误: {str(e)}")
        sys.exit(1) 