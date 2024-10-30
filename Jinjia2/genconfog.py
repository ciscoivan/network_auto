
import yaml
from jinja2 import FileSystemLoader,Environment

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('sw_template.j2')

with open('../../wchat/WeChat Files/wxid_xmpw2zlrrb6m21/FileStorage/File/2022-12/sw_info.yaml') as f:
    sws = yaml.safe_load(f)

for sw in sws:
    swx_conf = sw['name'] + '.txt'
    with open(f'.\\{swx_conf}','w') as f:
         f.write(template.render(sw))