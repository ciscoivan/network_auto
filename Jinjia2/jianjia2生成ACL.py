from jinja2 import  FileSystemLoader,Environment

allowed = ['192.168.1.1','192.168.1.2','192.168.1.3']
disallowed = ['192.168.2.1',
         '192.168.2.2',
         '192.168.2.3']

loader = FileSystemLoader('templates')
env = Environment(loader=loader,trim_blocks=True)
tp1 = env.get_template('acl.conf.j2')
ouput = tp1.render(allow=allowed,disallow=disallowed)
print(ouput)