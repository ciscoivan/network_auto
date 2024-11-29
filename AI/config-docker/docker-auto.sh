#!/bin/bash

# 安装 Docker CE
# 此脚本适用于 CentOS 7

# 卸载旧版本（如果已安装）
#yum remove -y docker \
#              docker-client \
#              docker-client-latest \
#              docker-common \
#              docker-latest \
#              docker-latest-logrotate \
#              docker-logrotate \
#              docker-engine

# 设置 Docker 仓库
yum install -y yum-utils
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo


#ACCELERATOR="https://tawedu6l.mirror.aliyuncs.com"
# 安装 Docker CE
yum install -y docker-ce 

# 获取阿里云加速器地址
# 请替换 <Your_Access_Key_ID> 和 <Your_Access_Key_Secret> 为你的阿里云 AccessKey
# 访问 https://cr.console.aliyun.com/#/accelerator 获取加速器地址


# 重启 Docker 服务
systemctl daemon-reload
systemctl restart docker
#

# 配置阿里云 Docker 加速器
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
   "registry-mirrors": ["https://registry.docker-cn.com","https://pee6w651.mirror.aliyuncs.com"]
}


EOF


systemctl daemon-reload
systemctl restart docker
# 验证 Docker 是否正确安装并启动
#docker run hello-world

#echo "Docker installation is complete and Docker service is running with Aliyun加速器."
mkdir -p /etc/systemd/system/docker.service.d

tee /etc/systemd/system/docker.service.d/http-proxy.conf <<-'EOF'
[Service]
Environment="HTTP_PROXY=http://172.16.1.15:7890"
Environment="HTTPS_PROXY=http://172.16.1.15:7890"


EOF

echo "Docker procx install"
