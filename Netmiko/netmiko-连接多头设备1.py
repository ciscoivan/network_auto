import netmiko
from netmiko import ConnectHandler

# 存放认证失败的设备信息
switch_with_authentication_issue = []
# 存放网络不通的设备信息
switch_not_reachable = []

with open('ipfile') as f:

    for ips in f.readlines():
        try:
            ip = ips.strip()
            connection_info = {
                'device_type': 'cisco_ios',
                'ip': ip,
                'username': 'ivan',
                'password': '123.com',}

            with ConnectHandler(**connection_info) as conn:
                 print (f'已经成功登陆交换机{ip}')
                 output = conn.send_command('show run | i hostname')
                 print(output)

        except netmiko.NetmikoAuthenticationException:
            print(ip + "用户验证失败！")
            switch_with_authentication_issue.append(ip)

        except netmiko.ssh_exception.NetmikoTimeoutException:
            print(ip + "目标不可达！")
            switch_not_reachable.append(ip)

print('\n ====结果输出====')
print('·下列交换机用户验证失败：')
for i in switch_with_authentication_issue:
    print(f"  {i}")

print('·下列交换机不可达：')
for i in switch_not_reachable:
    print(f"  {i}")