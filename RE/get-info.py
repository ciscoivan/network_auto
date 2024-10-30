with open('demo.txt') as f:
    t = f.readlines()
    print(t)
    info1 =t[2].strip()
    info2 = t[7].strip()
    print(info1)
    print(info2)
    IP1 = info1.split()[-1]
    IP2= info2.split()[-2]
    print(IP1)
    print(IP2)

a = {'info_centert_ip':IP1,'inter_loop0_ip':IP2}

if a['info_centert_ip'] !=  a['inter_loop0_ip'] :
    print("error")
else:
    print('good')