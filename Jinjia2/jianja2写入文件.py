from  jinja2 import FileSystemLoader,Environment

loder = FileSystemLoader('templates')
env = Environment(loader=loder)
tp1 = env.get_template('vars.conf.j2')
data = {'ip':'1.1.1.1'}
print(tp1.render(data=data))
with open('cisco.conf','w') as f :
    f.write(tp1.render(data=data))