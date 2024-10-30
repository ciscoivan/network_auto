from netmiko import ConnectHandler
import  time

vnpt = {'device_type':'huawei',
      'ip':'123.30.147.67',
      'username':'ivan',
      'password':'1A.liyang.com'}

date1=time.strftime("%Y-%m-%d",time.localtime())

a=0
b=0
with ConnectHandler(**vnpt) as connect:
        print ("************成功登陆VN-Tencent-POP-SW-********************\n" + "设备登陆地址:"+ vnpt['ip'])
        print("当前日期为:",date1)
        output1 = connect.send_command('display device')
        print("设备型号状态健康检查:",end="")
        print(output1)
        print('ping测试上线的Dell-Server-idrac-ip')
        for i in range(10,74):
            ip = '10.0.0.' +str(i)
            output = connect.send_command('ping -c 2 ' + ip)
            if output.find('time=')!=-1:
               print("Ping Success！",ip)
               a=a+1
            else:
               print("Ping failure！",ip)
               b=b+1
            save = open("vnpt"+ date1 +'.txt','a+')
            save.write(output)
            save.close()
        print("ping成功地址次数",a)
        print("ping失败地址次数",b)
        print("记录测试结果保存到本地完成！")
        print("*********************************************")
