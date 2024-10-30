import netmiko
import textfsm
import json

disp_cpu_result_dict = {}

with open('devices_list.txt') as f:
    for line in f.readlines():
        line_s = line.split( )
        device_ip = line_s[0]
        device_name = line_s[1]
        connection_info = {
            'device_type': 'huawei',
            'ip': device_ip,
            'username': 'ivan',
            'password': '123.com'
        }
        with netmiko.ConnectHandler(**connection_info) as connect:
            print('已成功登录设备： ' + device_ip)
            disp_cpu_result = connect.send_command('display cpu-usage')
        with open('huawei_display_cpu-usage.template') as t:
            template = textfsm.TextFSM(t)
            disp_cpu_result_textfsm = template.ParseTextToDicts(disp_cpu_result)
            disp_cpu_result_dict[device_name] = disp_cpu_result_textfsm
print('=======================================================')
print(json.dumps(disp_cpu_result_dict))

print('=======================================================')
for k,v in disp_cpu_result_dict.items():
    print(k + ' 过去5秒钟CPU利用率:' + v[0]['CPU_5s'] + '   过去1分钟CPU利用率：' + v[0]['CPU_1m'] + '    过去5分钟CPU利用率：' + v[0]['CPU_5m'])