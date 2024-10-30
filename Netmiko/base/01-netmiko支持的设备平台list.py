from netmiko.ssh_dispatcher import platforms
from netmiko import SSHDetect

if __name__ == '__main__':
    '''
    netmiko 是基于paramiko封装的一个支持多厂商的ssh工具包
    实现对设备的ssh（telnet）登陆操作，部分支持文件传输
    Multi-vendor library to simplify Paramiko SSH connections to network devices
    github地址：https://github.com/ktbyers/netmiko
    安装：pip install netmiko
    依赖：
        Paramiko >= 2.4.3
        scp >= 0.13.2
        pyserial
        textfsm
    根据适配程度各平台的支持分为以下三种
                Regularly Tested
                Limited Testing
                Experimental
    对于设备采集，个人认为适配程度非常好，封装程度非常高，非常适合网络运维开发新手。
    '''
    for platform in platforms:
        print(platform)


# # 更细致的可以参考这段代码


    from netmiko import platforms

    for i in platforms:
        print(i)

    ssh_platforms = [i for i in platforms if 'telnet' not in i and 'serial' not in i and 'ssh' not in i]
    if 'abc' in ssh_platforms:
        ssh_platforms.remove('abc')
    if 'autodetect' in ssh_platforms:
        ssh_platforms.remove('autodetect')
    if 'terminal_server' in ssh_platforms:
        ssh_platforms.remove('terminal_server')

    telnet_platforms = [i for i in platforms if 'telnet' in i]
    serial_platforms = [i for i in platforms if 'serial' in i]

    print(ssh_platforms)
    print(len(ssh_platforms))
    print(telnet_platforms)
    print(len(telnet_platforms))
    print(serial_platforms)