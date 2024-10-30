from napalm import  get_network_driver
import  json
from getpass import  getpass
ip = '192.168.10.1'
username = 'steven'
password = 'Tian.siyu1'

driver = get_network_driver('ios')

RT= driver(ip,username,password,optional_args={'port':9301})
RT.open()
output1 = RT.get_interfaces()
output2 = RT.get_interfaces_ip()
#print(json.dumps(output1,indent=2))
#print(json.dumps(output2,indent=2))
print("\n 路由器%s的端口状态为UP：\n" %(ip))

for key,value in output1.items():

    if value['is_up'] == True :
            print(key+'  mac地址为:'+value['mac_address'])
print("---------------------------------------------")

for key,value in output2.items():
    if 'ipv4' in value.keys():
        v1 = value['ipv4']
        for i in v1:
            print("接口信息"+key+"ip地址为：",i)



