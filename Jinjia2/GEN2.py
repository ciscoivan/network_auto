from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('varisables.j2')

with open('../../wchat/WeChat Files/wxid_xmpw2zlrrb6m21/FileStorage/File/2022-12/variables.yaml') as f:
    vars_dict = yaml.safe_load(f)

for sw in vars_dict:
    swx_conf = sw['name'] + '.txt'
    with open(f'.\\{swx_conf}','w') as f:
         f.write(template.render(sw))