with open('demo.txt') as f:
    t = f.read().split('#')
    print(t)
    for i in t:
        if 'info-center' in i:
            c = i.split()
            s_ip = c[c.index("source-ip")+1]
            print(s_ip)