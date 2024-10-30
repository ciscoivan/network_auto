from jinja2 import Template,StrictUndefined

if __name__ == '__main__':
    # template = Template('Hello {{ name }}!')
    # output = template.render(name='John Doe')
    # print(output)
    intf_templ = Template('''
    config
    interface {{ intf_name }}
        description {{ desc }}
    no shutdown
    ''',)
    intf_config = intf_templ.render(intf_name='eth1/1', desc='configed by jinja2')
    print(intf_config)
    print(intf_config.splitlines())

    intf_templ = Template('''
        config
        interface {{ intf_name }}
            description {{ desc }}
        no shutdown
        ''')
    intf_config = intf_templ.render(intf_name='eth1/1')
    print(intf_config)

    # intf_templ = Template('''
    #         config
    #         interface {{ intf_name }}
    #             description {{ desc }}
    #         no shutdown
    #         ''', undefined=StrictUndefined)
    # intf_config = intf_templ.render(intf_name='eth1/1')
    # print(intf_config)


