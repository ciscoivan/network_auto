from scrapli.driver.core import  IOSXEDriver

device = {
    "host": "192.168.200.1",
    "auth_username": "ivan",
    "auth_password": "123.com",
    "port": 22,
    "auth_strict_key": False,
}

conn = IOSXEDriver(**device)
conn.open()
responses = conn.send_commands(["show clock", "show ip int brief"])

for response in responses:
   print(r  ponse.result)
conn.close()