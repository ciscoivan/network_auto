from netmiko import ConnectHandler

sw1 = {'device_type':'huawei',
      'ip':'192.168.11.11',
      'username':'python',
      'password':'123'}

commands = ['interface GigabitEthernet 0/0/1', 'description descby_send_config_set()']

with ConnectHandler(**sw1) as connect:
        print ("已经成功登陆交换机" + sw1['ip'])

        print('===实验目的（1），交互形式推送一条指令。')
        output = connect.send_command('display interface description | include GE0/0/[12][^0-9]')

# 正则表达式在网络运维中是一把利器，稍作解释：
#   因为 Layer3Switch-1 的 0 板是有 24 端口，我们只关注 GE0/0/1 和 GE0/0/2。
#   为了回显简洁，我们使用了 include 进行过滤。
#   正则表达式 GE0/0/[12][^0-9] 中 [12] 表示字符 1 或者 2 ，[^0-9] 表示非0-9。
#   于是 GE0/0/[12][^0-9] 只会匹配 GE0/0/1 和 GE0/0/2 ，不会匹配 GE0/0/3 等其它

        print(output)

        print('===实验目的（2），列表形式推送多条指令。')
        output = connect.send_config_set(commands)
        print(output)

        print('===实验目的（3），文件形式推送多条指令。')
        output = connect.send_config_from_file('netmiko-config-lab2.txt')
        print(output)

        print('===最后再检查配置')
        output = connect.send_command('display interface description | include GE0/0/[12][^0-9]')
        print(output)

        # 华为设备的保存配置save后需要输入y进行确认，后面实验再演示。