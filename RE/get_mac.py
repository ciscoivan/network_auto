

def get_mac():
    with open('mac-address.txt') as f:
        for i in f.readlines():
            print(i)



def get_mac_replay(rp):
    mac_address = ""
    with open('mac-address.txt') as f:
        for i in f.readlines():
            i = i.replace(":",rp)
            print(i)
            mac_address +=  i
    with open("mac-address-tran.txt", 'a+') as f:
        f.write(mac_address)



if __name__ == '__main__':
    get_mac()
    print("-------------------")
    get_mac_replay(rp="-")


