#!/usr/bin/env python3
# 测试SSHManager导入

import sys
import traceback

# 将当前目录添加到Python的导入路径中
sys.path.insert(0, '.')

try:
    print("尝试导入SSHManager...")
    from network_tools.managers.ssh_manager import SSHManager
    print("✓ SSHManager导入成功")
    
    # 测试类实例化
    print("尝试实例化SSHManager...")
    ssh_manager = SSHManager("test-host", "test-user", "test-pass")
    print("✓ SSHManager实例化成功")
    
    print("所有测试通过！")
    sys.exit(0)
except Exception as e:
    print(f"✗ 测试失败: {type(e).__name__}: {str(e)}")
    print("详细错误信息:")
    traceback.print_exc()
    sys.exit(1)
