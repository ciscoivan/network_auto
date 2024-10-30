from netmiko import ConnectHandler, Netmiko

import logging

# # 进行debug，方便调试
logging.basicConfig(
    level=logging.DEBUG,
)

if __name__ == '__main__':
    import time

    """
    以下是一种比较python风格的书写方式，字典前加 ** 将字段以k1 = v1, k2 = v2的方式在函数里自动展开
    with 上下文管理 可以非常优雅的处理与设备连接断开(离开with的代码逻辑块后，Python会自动帮我们把netmiko的连接disconnect)
    import logging
    logging.basicConfig(
    level=logging.DEBUG,
    )
    开启debug模式，会详细的输出相关的netmiko执行情况，方便排障
    'session_log'可以将执行的结果完整的记录下来，包含了netmiko帮助我们进行的相关操作，也可以用于排障，查询一下为什么命令执行失败了
    """
    # # 将设备信息放入到字典中 可以让代码更加整洁
    nxosv9k = {
        'device_type': 'cisco_nxos',
        'host': 'sbx-nxos-mgmt.cisco.com',
        'username': 'admin',
        'password': 'Admin_1234!',
        'port': 22,  # optional, defaults to 22
        # 'secret': 'secret',  # optional, defaults to ''
        'session_log': 'show_demo.log',  # 保存到指定文件，完整的呈现整个登录和执行命令的过程
        'timeout': 60 * 3,
        'conn_timeout': 30
    }
    with Netmiko(**nxosv9k) as net_conn:
        net_conn.write_channel('show  running\n')

        timeout = net_conn.timeout
        loop_delay = 0.1
        loops = timeout / loop_delay
        final_delay = 2
        i = 0
        output = ''
        while i < loops:
            time.sleep(loop_delay)  # 自己控制停顿时间，然后从隧道中读取
            read_output = net_conn.read_channel()

            if read_output:
                output += read_output
            else:
                # 如果为空则再尝试读取一次，仍为空，认定读取结束
                time.sleep(final_delay)
                read_output = net_conn.read_channel()
                if read_output:
                    output += read_output
                else:
                    output += read_output
                    break

            i += 1
        print(output)
