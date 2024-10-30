from  jinja2 import  FileSystemLoader,Environment


loader = FileSystemLoader(['templates','other-templates'],encoding='utf-8')
environment = Environment(loader=loader)
tpl1= environment.get_template('first.conf.j2')
output = tpl1.render()
print(output)