import  netmiko
import  os
import time
from  datetime import  datetime

from  netmiko import ConnectHandler


date1 = time.strftime("%Y-%m-%d",time.localtime())

cisco = {
    'device_type':'cisco_ios',
    'host':'124.248.48.47',
    'username':'admin',
    'password':'1a.qytang.com',
    'port':9301
}
huawei = {
    'device_type':'huawei_ios',
    'host':'124.248.48.46',
    'username':'ivan',
    'password':'1m',
    'port':9301
}


while True :

    print('********************************************************************************************')
    print('****************************欢迎使用网络配置备份系******************************************')
    print('****************************','1:','Cisco 网络设备备份', '*****************************************')
    print('****************************','2:','Huawei 网络设备备份', '****************************************')
    print('****************************', '3:', '退出程序', '**************************************************')
    print('********************************************************************************************')
    choose = input("请输入您要选择的服务")

    if choose == '1':
        print("欢迎使用cisco网络备份")
        print("经过检查您一共有8台设备需要备份正在进行中请稍后")
        net_connect = ConnectHandler(**cisco)
        # net_connect.enable()  # 进入使能模式
        current_view = net_connect.find_prompt()
        print(current_view)
        ontput = net_connect.send_command("show run")
        date = datetime.now()
        file = open('d:\\code\\cisco'+date1+'.txt','w')
        file.write(ontput)
        print(ontput)

    elif choose == '2':
        et_connect = ConnectHandler(**huawei)
        # net_connect.enable()  # 进入使能模式
        current_view = net_connect.find_prompt()
        print(current_view)
        ontput = net_connect.send_command("show run")
        date = datetime.now()
        file = open('d:\\code\\huawei' + date1 + '.txt', 'w')
        file.write(ontput)
        print(ontput)
    else:
        print("欢迎下次使用")
        break


