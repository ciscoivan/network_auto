from scrapli import Scrapli

my_device = {
    "host": "192.168.200.8",
    "auth_username": "ivan",
    "auth_password": "1a.qytang.com",
    "auth_strict_key": False,
    "platform": "hp_comware"
}

conn = Scrapli(**my_device)
conn.open()

responses = conn.send_commands(["dis cu", "dis ip int brief"])

for response in responses:
   print(  sponse.result)
conn.close()