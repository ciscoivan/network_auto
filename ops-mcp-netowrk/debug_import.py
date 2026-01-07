import sys
import traceback

# 尝试导入各个模块
modules = [
    "network_tools.managers.ssh_manager",
    "network_tools.tools.device_tools",
    "network_tools.main"
]

for module in modules:
    print(f"\n尝试导入: {module}")
    try:
        __import__(module)
        print(f"✓ 成功导入 {module}")
    except Exception as e:
        print(f"✗ 导入失败: {e}")
        traceback.print_exc()
        sys.exit(1)

print("\n所有模块导入成功!")
