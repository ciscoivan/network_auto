import  napalm
import os


def replace_config(vendor, devices, template_file):
    try:
        # drive是一个类class
        drive = napalm.get_network_driver(vendor)
        # 类实例化
        conn = drive(**devices)
        # 建立连接会话
        conn.open()
    except Exception as e:
        print("连接错误:{}".format(e))
        return

    try:
        if not (os.path.exists(template_file) and os.path.isfile(template_file)):
            msg = '文件不存在或文件类型不可用.'
            raise ValueError(msg)

        print("开始加载候选替换配置...")
        # 这个还未加载到设备上的
        conn.load_replace_candidate(template_file)
        # 配置比较
        print("\n预览配置对比:")
        print(">"*80)
        compare_result = conn.compare_config()
        print(compare_result)
        print(">" * 80)

        # You can commit or discard the candidate changes.
        if compare_result:
            try:
                choice = input("\nWould you like to commit these changes? [yN]: ").lower()
            except NameError:
                choice = input("\nWould you like to commit these changes? [yN]: ").lower()
            if choice == "y":
                print("Committing ...")
                conn.commit_config()
            else:
                print("Discarding ...")
                conn.discard_config()
        else:
            print('没有新的配置.')
            conn.discard_config()

        conn.close()

        print("Done...")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    vendor = 'ios'
    devices = {'hostname': '192.168.0.20',
               'username': 'cisco',
               'password': 'cisco',
               'optional_args':{'port': 22}
               }
    tmp = 'LOG/192.168.0.20-running.conf'

    replace_config(vendor, devices, template_file=tmp)