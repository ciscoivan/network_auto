from jinja2 import Template

tpl = Template("欢迎进入{{name}}运维系统")
print(tpl.render(name="思科"))