import re


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
    log = get_log('show_interface.log')
    # '''编写正则表达式，构建re对象
    # re.S 代表的是. 可以匹配任意字符包括换行
    # '''
    # software_re = re.compile(r'\s+NXOS:\s+version\s+(\S+)')
    # software_re_search = software_re.search(log)
    # if software_re_search:
    #     ver = software_re_search.group(1)
    #     print(ver)
    intf_re = re.compile(r'Ethernet\d+/\d+.+?\n\n',re.S)
    intfs = intf_re.findall(log)
    print(intfs)
    '''
    
Ethernet1/1 is up
admin state is up, Dedicated Interface
  Belongs to Po11
  Hardware: 100/1000/10000 Ethernet, address: 00bb.2cfc.0101 (bia 00bb.2cfc.0101)
  MTU 1500 bytes, BW 1000000 Kbit , DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is trunk
  full-duplex, 1000 Mb/s
  Beacon is turned off
  Auto-Negotiation is turned on  FEC mode is Auto
  Input flow-control is off, output flow-control is off
  Auto-mdix is turned off
  Switchport monitor is off
  EtherType is 0x8100
  EEE (efficient-ethernet) : n/a
    admin fec state is auto, oper fec state is off
  Last link flapped 00:31:51
  Last clearing of "show interface" counters never
  1 interface resets
  Load-Interval #1: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  Load-Interval #2: 0 seconds
    0 seconds input rate 0 bits/sec, 0 packets/sec
    0 seconds output rate 0 bits/sec, 0 packets/sec
    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
  RX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 input packets  0 bytes
    0 jumbo packets  0 storm suppression packets
    0 runts  0 giants  0 CRC  0 no buffer
    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
    0 input with dribble  0 input discard
    0 Rx pause
  TX
    0 unicast packets  0 multicast packets  0 broadcast packets
    0 output packets  0 bytes
    0 jumbo packets
    0 output error  0 collision  0 deferred  0 late collision
    0 lost carrier  0 no carrier  0 babble  0 output discard
    0 Tx pause
    '''
