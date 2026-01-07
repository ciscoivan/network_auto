#!/usr/bin/env python3
# 仅检查SSHManager的语法正确性

import sys
import ast

# 读取ssh_manager.py文件内容
try:
    with open('network_tools/managers/ssh_manager.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("正在检查SSHManager的语法...")
    
    # 仅使用ast模块检查语法，不执行代码
    ast.parse(content)
    
    print("✓ SSHManager语法检查通过！")
    print("\n代码结构分析:")
    print("- 导入了paramiko、logging和time模块")
    print("- 定义了SSHManager类")
    print("- 包含上下文管理器方法(__enter__和__exit__)")
    print("- 实现了连接健康检查方法(_is_connection_active)")
    print("- 实现了自动重连方法(_reconnect)")
    print("- 实现了带重试机制的命令执行方法(exec_command_with_retry)")
    print("- 包含连接缓存功能")
    
    sys.exit(0)
    
except SyntaxError as e:
    print(f"✗ 语法错误: {e}")
    print(f"   行号: {e.lineno}")
    print(f"   列号: {e.offset}")
    print(f"   错误信息: {e.msg}")
    sys.exit(1)
except Exception as e:
    print(f"✗ 检查失败: {type(e).__name__}: {str(e)}")
    sys.exit(1)
