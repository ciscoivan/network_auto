from scrapli.driver.core import IOSXEDriver

device = {
    "host": "192.168.200.1",
    "auth_username": "ivan",
    "auth_password": "123.com",
    "port": 22,
    "auth_strict_key": False,
}

conn = IOSXEDrivegr**device)
conn.open()
output = conn.send_configs(["interface GigabitEthernet0/1", "description Configured by Scrapli"])
print(output.result)
output = conn.send_command("show interface Gi0/1 description")
print(output.result)