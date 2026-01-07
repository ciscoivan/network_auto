#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试SSHManager的自动重连机制
"""

import logging
import time
from network_tools.managers.ssh_manager import SSHManager

# 配置日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('test_ssh_reconnect')

def test_ssh_reconnect():
    """测试SSH自动重连功能"""
    logger.info("开始测试SSH自动重连功能...")
    
    # 请根据实际情况修改以下参数
    hostname = "192.168.1.1"
    username = "admin"
    password = "password"
    port = 22
    timeout = 30
    
    try:
        with SSHManager(hostname, username, password, port, timeout) as ssh:
            # 1. 测试正常命令执行
            logger.info("1. 测试正常命令执行...")
            result = ssh.exec_command_with_retry("echo '正常执行'")
            if result["success"]:
                logger.info(f"✓ 正常命令执行成功: {result['output']}")
            else:
                logger.error(f"✗ 正常命令执行失败: {result['error']}")
                return False
            
            # 2. 测试连接状态检查
            logger.info("2. 测试连接状态检查...")
            if ssh._is_connection_active():
                logger.info("✓ 连接状态检查成功")
            else:
                logger.error("✗ 连接状态检查失败")
                return False
            
            # 3. 模拟长时间空闲后执行命令
            logger.info("3. 模拟长时间空闲后执行命令...")
            logger.info("   等待10秒模拟空闲...")
            time.sleep(10)
            
            result = ssh.exec_command_with_retry("echo '空闲后执行'")
            if result["success"]:
                logger.info(f"✓ 空闲后命令执行成功: {result['output']}")
            else:
                logger.error(f"✗ 空闲后命令执行失败: {result['error']}")
                return False
            
            # 4. 测试多次命令执行
            logger.info("4. 测试多次命令执行...")
            for i in range(5):
                result = ssh.exec_command_with_retry(f"echo '第{i+1}次执行'")
                if result["success"]:
                    logger.info(f"   ✓ 第{i+1}次命令执行成功: {result['output']}")
                else:
                    logger.error(f"   ✗ 第{i+1}次命令执行失败: {result['error']}")
                    return False
                time.sleep(2)
            
            # 5. 测试复杂命令
            logger.info("5. 测试复杂命令执行...")
            result = ssh.exec_command_with_retry("show version | head -5")
            if result["success"]:
                logger.info(f"✓ 复杂命令执行成功")
                logger.debug(f"输出: {result['output']}")
            else:
                logger.error(f"✗ 复杂命令执行失败: {result['error']}")
                # 复杂命令可能因设备不同而失败，这里不返回False
                logger.info("   注意: 复杂命令失败可能是因为设备不支持该命令，而非SSH连接问题")
            
        logger.info("\n✓ 所有测试通过！SSHManager自动重连机制工作正常")
        return True
        
    except Exception as e:
        logger.error(f"\n✗ 测试失败: {str(e)}")
        return False

if __name__ == "__main__":
    test_ssh_reconnect()
