#!/bin/bash

# 获取系统中的网络接口名称
interfaces=$(ip link show | awk -F': ' '{print $2}' | sed 's/@.*//' | sed '/^[0-9]*$/d')

# 打印网络接口名称供用户选择
echo "Available network interfaces:"
for i in $interfaces; do
    echo "$i"
done

# 让用户输入想要配置的网络接口名称
read -p "Enter the network interface you want to configure (e.g., eth0): " INTERFACE

# 检查输入的网络接口是否存在
if ! ip link show $INTERFACE &> /dev/null; then
    echo "Interface $INTERFACE does not exist."
    exit 1
fi

# 定义静态IP配置参数
read -p "Enter IP address for $INTERFACE: " IPADDR
read -p "Enter netmask for $INTERFACE (e.g., 255.255.255.0): " NETMASK
read -p "Enter gateway for $INTERFACE: " GATEWAY
read -p "Enter DNS for $INTERFACE (e.g., 8.8.8.8): " DNS1

# 创建或编辑网络配置文件
cat > /etc/sysconfig/network-scripts/ifcfg-$INTERFACE <<EOF
DEVICE=$INTERFACE
BOOTPROTO=static
ONBOOT=yes
IPADDR=$IPADDR
NETMASK=$NETMASK
GATEWAY=$GATEWAY
DNS1=$DNS1
EOF

# 重启网络服务以应用配置
systemctl restart network
