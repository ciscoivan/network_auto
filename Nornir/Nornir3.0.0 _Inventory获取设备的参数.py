"""这里可以看到我在hosts.yaml中保存了4台交换机的信息，本篇实验就来讲下如何在Nornir脚本中按需将上面host.yaml各个交换机对应的数据取出并打印出来。
实验目的：

学习如何使用Nornir的inventory来获取hosts.yaml中保存的设备的参数，这里我们将提取出交换机SW1对应的name, hostname, username, password, platform, groups, data等参数。
"""

import ipdb
from nornir import InitNornir
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file='config.yaml')
ipdb.set_trace()
#只需输入nr.inventory.hosts即可看到hosts.yaml中保存的4个交换机的名称（sw1, sw2, sw3, sw4），而从大括号可以判断出nr.inventory.hosts返回的值为一个字典：
"""#nr.inventory.hosts['ro1'].name
    nr.inventory.hosts['ro1'].hostname
    nr.inventory.hosts['ro1'].username
    nr.inventory.hosts['ro1'].password
    nr.inventory.hosts['ro1'].platform
    nr.inventory.hosts['ro1'].groups
    nr.inventory.hosts['ro1'].data
    这些文件都是配置yamlhosts里面的
"""