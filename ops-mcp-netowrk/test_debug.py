#!/usr/bin/env python
# 测试脚本，用于捕获网络设备巡检工具的DEBUG日志

import logging
import sys
import os

# 将当前目录添加到Python的导入路径中
sys.path.insert(0, os.path.abspath("."))

# 配置详细的DEBUG日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('test_debug')

# 导入需要测试的函数
from network_tools.tools.device_tools import (
    check_cisco_device_health,
    check_device_interfaces_detail,
    check_device_logs,
    check_device_neighbors,
    check_device_vlan_config
)

from network_tools.tools.session_tools import check_device_sessions

def test_function(function_name, **kwargs):
    """测试指定的函数并捕获日志"""
    logger.info(f"=== 开始测试函数: {function_name.__name__} ===")
    logger.info(f"参数: {kwargs}")
    
    try:
        result = function_name(**kwargs)
        logger.info(f"测试结果: {result}")
        logger.info(f"=== 函数 {function_name.__name__} 测试完成 ===")
        return result
    except Exception as e:
        logger.error(f"函数 {function_name.__name__} 测试失败: {e}", exc_info=True)
        logger.info(f"=== 函数 {function_name.__name__} 测试失败 ===")
        return None

if __name__ == "__main__":
    logger.info("开始网络设备巡检工具DEBUG测试")
    
    # 测试参数（请根据实际情况修改）
    test_params = {
        "hostname": "192.168.1.1",  # 替换为您的设备IP
        "username": "admin",        # 替换为您的用户名
        "password": "password",     # 替换为您的密码
        "timeout": 10
    }
    
    # 测试各个函数
    test_function(check_cisco_device_health, **test_params)
    # test_function(check_device_interfaces_detail, **test_params)
    # test_function(check_device_logs, **test_params, log_level="error", lines=10)
    # test_function(check_device_neighbors, **test_params)
    # test_function(check_device_vlan_config, **test_params)
    # test_function(check_device_sessions, **test_params)
    
    logger.info("网络设备巡检工具DEBUG测试完成")
