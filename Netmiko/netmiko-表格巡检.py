import openpyxl
from  netmiko import ConnectHandler
import time

date1=time.strftime("%Y-%m-%d",time.localtime())
num = 0

def exec():
    data = []
    sep = {}
    wb = openpyxl.load_workbook('devicelist.xlsx')
    ws = wb.active

    for n in ws.iter_rows(min_row=2,min_col=1):


        sep = {
            "device_type": n[0].value,
            "ip": n[1].value,
            "username": n[2].value,
            "password": n[3].value,
            "port": n[4].value,
            'secret': n[5].value,
        }
        data.append(sep)
    return {
        'device':data,
    }


def ssh_session(data):
    num = 0
    for info in data:
        with ConnectHandler(device_type=info['device_type'], ip=info['ip'], username=info['username'],
                            password=info['password'], port=info['port'], secret=info['secret']) as connect:
            print("-------------------------设备正在登录中---------------------------------")
            print("您以成功登录", info["ip"])
            print("备份命令执行中。。。")
            connect.enable()
            output = connect.send_command('show run ')
            time.sleep(3)
            print(output)
            backup = open(date1 + "-" + info["ip"] + ".txt", 'w+')
            backup.write(output)
            backup.close()
            num = num + 1

    print("您一共备总计{}台设备已完成！".format(num))

if __name__ == "__main__":
    device = exec()
    ssh = ssh_session(device['device'])