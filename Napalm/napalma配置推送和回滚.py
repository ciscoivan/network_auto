import  napalm
import logging

def merge_config(vendor,devices,template_file):
    try:
        drvice = napalm.get_network_driver(vendor)
        conn = drvice(**devices)
        conn.open()
        #print("登陆设备成功ip地址为{}".format(devices['ip']))
    except Exception as e:
        print("error connet{}".format(e))
        return
    try:

        conn.load_merge_candidate(filename=template_file)
        new_config = conn.compare_config()
        if new_config :
            print('**********login scuess*********')
            print("预推送的配置如下:")
            print('*'*80)
            print(new_config)
            print('*'*80)

            choice = input("你确定推送这些配置吗？[Y/N]:")
            if choice.lower() == 'y':
                print("开始提交配置,请稍后ing....")
                conn.commit_config()
                rollback = input("请检查推送的配置割接是否成功或者回滚[Y/N]:")
                if rollback.lower() == 'y':
                    print("配置开始回滚，请稍后ing....")
                    conn.rollback()
                    print("配置回滚完毕请检查")
                else:
                    print("配置下发成功")
            else:
                conn.discard_config()
                print("本次配置没有推送")
        else:
            print("无需重复配置")

    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    venv = 'ios'
    devices = {'hostname':'192.168.10.47',
               'username':'ivan',
               'password':'123.com',
               'optional_args':{'port':24}
    }
    tmp = 'D:/code/napalm/tmp.cfg'
    merge_config(vendor=venv,devices=devices,template_file=tmp)
    logging.basicConfig(filename='debug.log', level=logging.DEBUG)
    logger = logging.getLogger('napalm')