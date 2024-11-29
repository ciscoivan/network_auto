#!/bin/bash

# 检查当前用户是否为 root
if [ "$(id -u)" != "0" ]; then
   echo "该脚本必须以 root 用户运行" 1>&2
   exit 1
fi

# 将代理设置追加到 /root/.bashrc 文件末尾
echo 'export http_proxy=http://172.16.1.15:7890' >> /root/.bashrc
echo 'export https_proxy=http://172.16.1.15:7890' >> /root/.bashrc

echo "代理设置已添加到 /root/.bashrc"
