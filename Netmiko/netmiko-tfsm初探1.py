import netmiko
import textfsm
import json
with netmiko.ConnectHandler(device_type='huawei', ip='10.1.1.1', username='ivan', password='123.com') as connect:
    print('已经成功登录： 10.1.1.1' + '\n')
    output = connect.send_command('display cpu-usage')
    print(output)
with open('huawei_display_cpu-usage.template') as t:
    template = textfsm.TextFSM(t)
    disp_cpu_result_textfsm = template.ParseTextToDicts(output)
print('\n')
print(disp_cpu_result_textfsm)

print(json.dumps(disp_cpu_result_textfsm,indent=2))  #加json格式输出

