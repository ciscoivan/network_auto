from jinja2 import FileSystemLoader, Environment

ports = [{
      "type": "ethernet",
      "slot": 1,
      "port_num": 1,
      "intf_type": "access",
      'vlan': 10
      }, {
      "type": "ethernet",
      "slot": 1,
      "port_num": 2,
      "intf_type": "trunk",
      'vlan': 20
      }]

loader = FileSystemLoader('templates')
env = Environment(loader=loader)
tpl = env.get_template('mainmodular.conf.j2')
output = tpl.render(ports=ports)
print(output)