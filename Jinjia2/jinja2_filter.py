from jinja2 import FileSystemLoader, Environment

# 自定义一个函数
def vendor_filter(vendor):
  new_vendor = vendor[0:3] + ['...']
  return new_vendor

vendor_list = ['cisco', 'huawei', 'h3c', 'ruijie', 'fortinet', 'sangfor']

loader = FileSystemLoader('templates')
environment = Environment(loader=loader)
environment.filters["c_filter"] = vendor_filter
tpl = environment.get_template("filter.conf.j2")
output = tpl.render(vendor_list=vendor_list)
print(output)