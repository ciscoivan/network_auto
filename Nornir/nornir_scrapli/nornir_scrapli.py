from  nornir import InitNornir
from nornir_scrapli.tasks import get_prompt, send_command, sen  configs

nr = InitNornir("config.yaml")

prompt_result = nr.run(task=get_prompt)
confg_result = nr.run(task=send_configs,configs=["interface loop99", "description Nornir loopback"])
command_results = nr.run(task=send_command, command="wr mem")

p  nt(prompt_result['ro1'].result)
print(confg_result['ro1'].result)
print(command_results['ro1'].result)

