from netmiko import ConnectHandler, file_transfer
sw1 = {
        'device_type': 'cisco_ios',
        'ip': '192.168.200.10',
        'username': 'python',
        'password': '123'
}

with ConnectHandler(**sw1) as connect:
     print ("已经成功登陆交换机" + sw1['ip'])
     output = file_transfer(connect,
                source_file="test.txt",  #要上传的文件或者image
                dest_file="test.txt",
                file_system="flash:", #如果是思科NX-OS的话，需要放bootflash:，如果是Arista设备的话，需要放/mnt/flash，如果是Junos设备的话，则要放/var/tmp
                direction="put") #最后的direction这个参数，根据Netmiko官网API资料只能放“put”这一个值：
     print (output)