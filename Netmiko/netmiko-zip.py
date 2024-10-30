import os
import sys
from datetime import date
from  netmiko import  ConnectHandler
from concurrent.futures import ThreadPoolExecutor as Pool


def write_txt(filename,config_list):
    with open(filename,'w+') as f:
         for config in config_list:
             f.write(config)


def ssh_action(ip,pathconfig):
    dev_info = {'device_type':'cisco_ios','ip':ip,'username':'ivan','password':'123.com'}
    ssh_client = ConnectHandler(**dev_info)
    print('login'+dev_info['ip']+'success')
    output= ssh_client.send_config_from_file(pathconfig)
    print(output)
    file_name =f'{ip}.txt'
    write_txt(filename=file_name,config_list=output)

def main(ip,path_config):
    this_time = date.today()
    this_time = str(this_time)
    foldername = this_time
    old_folder_name = os.path.exists(foldername)
    if old_folder_name == True:
        print("folder realy have ")
        sys.exit()
    else:
        os.mkdir(foldername)
        os.chdir(foldername)
        net_configs = []

        with open(path_config, 'r') as config_path_list:
            for config in config_path_list:
                config = config.strip()
                net_configs.append(config)
            print(net_configs)

        with Pool(max_workers=6) as t:
            with open(ip,'r') as ip_list:
                 for ip ,config in zip(ip_list.readlines(),net_configs):
                     ip =ip.strip()
                     task = t.submit(ssh_action,ip,config)
                 print(task.result())




if __name__ == '__main__':
        print(os.getcwd())
        dev_info = 'D:\\code\\netmiko\\ipfile'
        conf_path = 'D:\\code\\netmiko\\templates\\config_path.txt'
        main(ip=dev_info,path_config=conf_path)


