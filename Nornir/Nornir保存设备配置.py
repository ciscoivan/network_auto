

from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date
import schedule



"""在Nornir中给设备保存配置的思路很简单，首先用nornir_naplam中的get-config这个getter类API获取设备的show run，
然后从nornir_utils.plugins.taks.files中调取write_file插件，该插件支持创建文本文件来保存我们的设备的配置
"""

def backup_config(task):
    r = task.run(task=napalm_get, getters=["config"])

    task.run(task=write_file, content=r.result["config"]["running"], filename=str(task.host.name) + "-" + str(date.today()) + ".txt")
#host: host.hostname 代表设备IP地址

def backconfig():
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(name="4台路由器正在备份配置", task=backup_config)
    print_result(result)


backconfig()

