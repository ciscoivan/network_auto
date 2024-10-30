import re

text = '''Nexus 9000v is a demo version of the Nexus Operating System

Software
  BIOS: version
 NXOS: version 9.3(3)
  BIOS compile time:
  NXOS image file is: bootflash:///nxos.9.3.3.bin
  NXOS compile time:  12/22/2019 2:00:00 [12/22/2019 14:00:37]


Hardware
  cisco Nexus9000 C9300v Chassis
  Intel(R) Xeon(R) Gold 6148 CPU @ 2.40GHz with 16408988 kB of memory.
  Processor Board ID 9N3KD63KWT0

  Device name: NXOS-Always-On
  bootflash:    4287040 kB
Kernel uptime is 22 day(s), 12 hour(s), 31 minute(s), 33 second(s)

Last reset
  Reason: Unknown
  System version:
  Service:

plugin
  Core Plugin, Ethernet Plugin

Active Package(s):
        mtx-openconfig-all-1.0.0.0-9.3.3.lib32_n9000'''
def get_log(file):
    '''
    读取log内容，将所有\r\n替换为\n
    :param file: 文件路径
    :return: log内容
    '''
    with open(file,mode='r',encoding='utf8') as f:
        log_content = f.read()
        log_content = log_content.replace('\r\n','\n')
        return log_content

if __name__ == '__main__':
    log = get_log('version.log')
    '''编写正则表达式，构建re对象
    re.S 代表的是. 可以匹配任意字符包括换行
    '''

    ''' NXOS: version 9.3(3) \d+.\d+\(\d+\)'''

    software_re = re.compile(r'\s+NXOS:\s+version\s+(?P<version>\S+)\s+')
    software_re_search = software_re.search(text)
    if software_re_search:
        ver = software_re_search.group('version')
        print(ver)

    software_re = re.compile(r'\s+NXOS:\s+version\s+(\S+)\s+.+?NXOS image file is: bootflash:///(\S+)',re.S)
    # software_re = re.compile(r'\s+NXOS:\s+version\s+(?P<version>\S+)\s+.+?NXOS image file is: bootflash:///(?P<bin_file>\S+)',re.S)
    software_re_search = software_re.search(log)
    if software_re_search:
        ver = software_re_search.group(1)
        bin_file = software_re_search.group(2)
        # ver = software_re_search.group('version')
        # bin_file = software_re_search.group('bin_file')
        print(ver,bin_file)