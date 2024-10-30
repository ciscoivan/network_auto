from netmiko import SSHDetect, Netmiko,ConnectHandler
# Netmiko等同于ConnectHanler
import logging

logging.basicConfig(
    level=logging.DEBUG,
)
if __name__ == '__main__':
    dev = {
        'device_type': 'autodetect',
        'host': '192.168.137.201',
        'username': 'netdevops',
        'password': 'admin123!',
        'port': 22,  # optional, defaults to 22
        # 'secret': 'admin1234!',  # optional, defaults to ''
        # 保存到指定文件，完整的呈现整个登录和执行命令的过程
    }
    dev['session_log'] = f"{dev['host']}.log"
    # 创建一个Detect的对象，将参数赋值
    guesser = SSHDetect(**dev)

    # 调用autodetect ，进行device_type的自动判断，返回结果是一个最佳结果的字符串，这个字符串就是netmiko自动判断的device_type
    # 无法判断的时候返回的是None
    best_match = guesser.autodetect()
    #
    print('best_match is:{}'.format(best_match))
    # 有一个潜在可能的device_type的字典，但是目前意义不大，了解即可。
    print('all guessers  is:{}'.format(guesser.potential_matches))

    dev['device_type'] = best_match
    connection = Netmiko(**dev)
    # 然后就可以去执行相关的命令了

    # 获取回显的前缀，提示符，prompt。可以从中获取设备名称，可以梳理资产信息。
    print('prompt is :{}'.format(connection.find_prompt()))
