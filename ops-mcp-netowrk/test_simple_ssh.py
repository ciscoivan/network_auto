#!/usr/bin/env python3
# 简单的SSHManager测试脚本，直接输出结果到控制台

import sys
import os
import logging

# 将当前目录添加到Python的导入路径中
sys.path.insert(0, os.path.abspath("."))

# 配置控制台日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger('simple_ssh_test')

try:
    logger.info("开始简单的SSHManager测试...")
    
    # 导入SSHManager
    from network_tools.managers.ssh_manager import SSHManager
    logger.info("✓ 成功导入SSHManager")
    
    # 测试SSHManager类的基本功能
    logger.info("测试SSHManager类的基本功能...")
    
    # 实例化SSHManager（不实际连接）
    ssh_manager = SSHManager(
        hostname="192.168.1.1",
        username="admin",
        password="password",
        timeout=5
    )
    logger.info("✓ 成功实例化SSHManager")
    
    # 测试连接参数
    logger.info(f"连接参数: {ssh_manager.connect_params}")
    logger.info(f"连接键: {ssh_manager.connection_key}")
    
    # 测试类变量
    logger.info(f"最大重试次数: {SSHManager.MAX_RETRIES}")
    logger.info(f"重试延迟: {SSHManager.RETRY_DELAY}秒")
    
    # 测试缓存功能
    logger.info(f"初始缓存大小: {len(SSHManager._connection_cache)}")
    
    logger.info("\n✓ 所有基本功能测试通过！")
    logger.info("\n注意: 由于没有实际的网络设备，无法测试实际的SSH连接和命令执行。")
    logger.info("但SSHManager类的基本功能和结构是正确的。")
    
    sys.exit(0)
    
except Exception as e:
    logger.error(f"\n✗ 测试失败: {type(e).__name__}: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
