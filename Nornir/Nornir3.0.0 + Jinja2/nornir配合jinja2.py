from nornir import InitNornir
from nornir_utils.plugins.tasks.data import load_yaml  #为了读取Jinja2渲染文件yaml
from nornir_jinja2.plugins.tasks import template_file  #为了调用Jinja2模板文件(BGP.j2)来做配置渲染
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
from nornir_netmiko import netmiko_send_command, netmiko_send_config

def load_data(task):
    data = task.run(task=load_yaml,file=f'{task.host}.yaml')  #task.host}的作用是读取hosts.yaml里的4台路由器的设备名配合后面的ro1 2...的yaml
    task.host["asn"] = data.result["asn"]
    task.host["neighbor"] = data.result["neighbor"]
    task.host["remoteas"] = data.result["remote-as"]
    task.host["loopbacks"] = data.result["loopbacks"]
    task.host["networks"] = data.result["networks"]
    rendering = task.run(task=template_file, template="BGP.j2", path="") #因为BGP.j2和我们的nornir8.py处于同一个文件夹下，因此这里的path参数设为空(path="")，
    task.run(task=netmiko_send_config, config_commands=rendering.result.split('\n'))

nr = InitNornir(config_file="config.yaml")
group1 = nr.filter(F(groups__contains="cisco_group1"))
r = group1.run(task=load_data)
print_result(r)