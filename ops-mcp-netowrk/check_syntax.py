#!/usr/bin/env python3
# 检查Python文件的语法正确性

import ast
import sys

# 要检查的文件路径
file_path = "network_tools/managers/ssh_manager.py"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"检查文件: {file_path}")
    print(f"文件大小: {len(content)} 字节")
    
    # 使用ast模块解析文件，检查语法错误
    ast.parse(content)
    
    print("✓ 语法检查通过！文件没有语法错误")
    sys.exit(0)
except SyntaxError as e:
    print(f"✗ 语法错误: {e}")
    print(f"   行号: {e.lineno}")
    print(f"   列号: {e.offset}")
    print(f"   错误信息: {e.msg}")
    sys.exit(1)
except Exception as e:
    print(f"✗ 检查失败: {type(e).__name__}: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
