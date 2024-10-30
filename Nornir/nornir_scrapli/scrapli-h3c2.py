from scrapli import Scrapli

my_device = {
    "host": "100.79.167.10",
    "auth_username": "python",
    "auth_password": "123456",
    "auth_strict_key": False,
    "platform": "hp_comware"
}

conn = Scrapli(**my_device)
conn.open()

output = conn.send_configs(["inter loopb 1", "undo ip add","ip add 3.3.3.3 32"])
print(output.result)

output = conn.send_command("dis ip interf brief")
print(output.result)


"""nornir

from nornir import InitNornir
from nornir_scrapli.tasks import get_prompt, send_command, send_configs

nr = InitNornir(config_file="config.yaml")

prompt_results = nr.run(task=get_prompt)
config_results = nr.run(task=send_configs, configs=["inter loopb 1", "undo ip add", "ip add 5.5.5.5 32"])
command_results = nr.run(task=send_command, command="save force")

print(prompt_results["sw1"].result)
print(config_results["sw1"].result)
print(command_results["sw1"].result)
"""