import sys
import os

print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Current working directory:", os.getcwd())
print("sys.path:", sys.path)
print("Environment variables:", list(os.environ.keys())[:10])  # 只显示前10个环境变量
