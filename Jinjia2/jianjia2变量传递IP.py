from jinja2 import  FileSystemLoader,Environment

loader = FileSystemLoader(['templates','other-templates'],encoding='utf-8')
enviroment = Environment(loader=loader)
tp1 = enviroment.get_template('vars.conf.j2')
ip = {'ip':'1.1.1.1'}
output = tp1.render(data=ip)
print(output)