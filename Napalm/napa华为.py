from napalm import get_network_driver
driver = get_network_driver('huawei_vrp')
device = driver(hostname='123.30.147.67', username='liyang', password='1A.liyang.com')
device.open()

get_facts = device.get_facts()
print(get_facts)

send_command = device.cli(['dis ver', 'dis cu'])