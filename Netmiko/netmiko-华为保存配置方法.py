import netmiko
net_dev = {
   'username': 'admin',
   'password': 'huawei',
   'ip': '192.168.47.30',
   'device_type': 'huawei'
}

ssh_client = netmiko.ConnectHandler(**net_dev)
print('login ' + net_dev['ip'] + ' success')
output = ssh_client.send_command('save', expect_string='\[Y\/N\]:')
output += ssh_client.send_command('y', expect_string='>')
print(output)