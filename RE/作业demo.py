import re

NMAE_RE = re.compile(r'(Ethernet|Vlan|loopback|port-channel)\d+\S+',re.I)
DESC_RE = re.compile(r'Description: (.*)',re.I)
MTU_RE = re.compile(r'MTU\s+(\d+)\s+bytes',re.I)

def read_log(file,encoding='utf8'):
    with open(file,mode='r',encoding=encoding) as f:
        text = f.read()
        return text


def get_intf_texts(text):
    intf_block_re = re.compile(r'(?:Ethernet|Vlan|loopback|port-channel)\d+\S+\s+is.+?\n\n', re.S)
    intf_texts = intf_block_re.findall(text)
    return intf_texts


def parse_single_intf(text):
    # NMAE_RE = re.compile(r'(Ethernet|Vlan|loopback|port-channel)\d+\S+')
    # DESC_RE = re.compile(r'Description: (.*)')
    intf_dict = {'name':None,'desc':None,'mtu':None}
    name_re = NMAE_RE
    desc_re = DESC_RE
    name_match = name_re.search(text)
    if name_match:
        name = name_match.group()
        intf_dict['name'] = name
    desc_match = desc_re.search(text)
    if desc_match:
        desc = desc_match.group(1)
        intf_dict['desc'] = desc
    mtu_match = MTU_RE.search(text)
    if mtu_match:
        mtu = mtu_match.group(1)
        intf_dict['mtu'] = mtu

    return intf_dict


def parse_intfs(text):
    intfs = []
    intf_texts = get_intf_texts(text)
    for intf_text in intf_texts:
        intf_info = parse_single_intf(intf_text)
        intfs.append(intf_info)
    return intfs


if __name__ == '__main__':
    text = read_log('show_interface.log').replace('\r\n', '\n')
    intfs = parse_intfs(text=text)
    print(intfs)

