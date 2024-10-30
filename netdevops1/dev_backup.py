from netmiko import ConnectHandler
from dev_manage import get_devs_in_df


def backup(dev_info, cmd='show running'):
    try:
        with ConnectHandler(**dev_info) as conn:
            conn.enable()
            content = conn.send_command(cmd)
            with open('{}.txt'.format(dev_info['host']), mode='w', encoding='utf8') as f:
                f.write(content)
            return True, '{}.txt'.format(dev_info['host'])
    except Exception as e:
        return False, None


def backup_single_dev4pd(dev_info):
    dev_info_in_dict = {
        'host': dev_info['host'],
        'username': dev_info['username'],
        'password': dev_info['password'],
        'device_type': dev_info['device_type'],
        'secret': dev_info['secret'],
    }

    return backup(dev_info_in_dict)


def backup_devs(filename='inventory,xlsx'):
    devs_df = get_devs_in_df()

    devs_df['backup'] = devs_df.apply(backup_single_dev4pd, axis=1)
    del devs_df['username']
    del devs_df['password']

    devs_df.to_excel('backup.xlsx', sheet_name='version', index=False)


if __name__ == '__main__':
    backup_devs()
