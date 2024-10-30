data1 = ''
data2 = ''
with open('demo.txt') as f:
     info = f.readlines()
     print(info)
     for i in info:
         if i.startswith('info-center'):
             data1 = i.strip().split()[-1]
             print(data1)
         elif i.startswith(' ip address'):
             data2 = i.strip().split()[2]


data3 = {'info_center_ip':data1,'inter_loop0_ip':data2}

if data3['info_center_ip'] == data3['inter_loop0_ip']:
    print('match')
    print('info-ip {}'.format(data3['info_center_ip']))
    print('loop-ip {}'.format(data3['inter_loop0_ip']))
else:
    print("no match")
    print('info-ip {}'.format(data3['info_center_ip']))
    print('loop-ip {}'.format(data3['inter_loop0_ip']))