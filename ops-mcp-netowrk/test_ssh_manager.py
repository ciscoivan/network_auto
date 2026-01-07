#!/usr/bin/env python3
# 测试SSHManager的导入和基本功能

import sys
import os

# 将当前目录添加到Python的导入路径中
sys.path.insert(0, os.path.abspath("."))

def test_ssh_manager_import():
    print("开始测试SSHManager导入...")
    
    try:
        from network_tools.managers.ssh_manager import SSHManager
        print("✓ 成功导入SSHManager")
        
        # 测试SSHManager类的基本信息
        print(f"✓ SSHManager类: {SSHManager}")
        print(f"✓ SSHManager类名: {SSHManager.__name__}")
        print(f"✓ SSHManager模块: {SSHManager.__module__}")
        
        # 测试类变量
        print(f"✓ 最大重试次数: {SSHManager.MAX_RETRIES}")
        print(f"✓ 重试延迟: {SSHManager.RETRY_DELAY}秒")
        
        # 测试实例化（不实际连接）
        print("\n测试SSHManager实例化...")
        ssh_manager = SSHManager(
            hostname="test-host",
            username="test-user",
            password="test-pass",
            timeout=5,
            device_type="cisco_ios"
        )
        print(f"✓ 成功实例化SSHManager")
        print(f"✓ 连接参数: {ssh_manager.connect_params}")
        print(f"✓ 连接键: {ssh_manager.connection_key}")
        
        print("\n✓ 所有测试通过！SSHManager导入和基本功能正常。")
        return 0
        
    except Exception as e:
        print(f"✗ 测试失败: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(test_ssh_manager_import())
