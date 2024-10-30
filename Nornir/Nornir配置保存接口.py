from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from datetime import date

def backup_getports(task1):
    r = task1.run(task=napalm_get,getters=["facts"])
    #print(type(r.result["facts"]["interface_list"]))
    task1.run(task=write_file, content='\n'.join(r.result["facts"]["interface_list"]),
              filename=str(task1.host.name) + "-ports-" + str(date.today()) + ".txt")

nr = InitNornir(config_file="config.yaml")
result = nr.run(name="接口配置采集中",task=backup_getports)

print_result(result)