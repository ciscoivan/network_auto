import  os
import json
import sys
from  datetime import  datetime
from  netmiko import  ConnectHandler
from  concurrent.futures import  ThreadPoolExecutor as Pool



def write_config_file(filenames,config_lists):
    with open(filenames,'w+') as f:
        for i in config_lists:
            f.write(i)

def auto_config(dev_info,config_file):
    ssh_client = ConnectHandler(**dev_info['connection'])
    dev_name = dev_info['name']
    dev_ips = dev_info['connection']
    dev_ip = dev_ips['ip']
    print('login'+dev_ip+'success')
    ssh_client.enable()
    ouput = ssh_client.send_config_from_file(config_file)
    filename = f'{dev_name}+{dev_ip}.txt'
    print(ouput)
    write_config_file(filenames=filename,config_lists=ouput)


def main(dev_file_path,config_path):
    now_time = datetime.now()
    now_time = now_time.strftime('%H-%M-%S')
    foldername = now_time
    old_folder_name = os.path.exists(foldername)
    if old_folder_name == True:
        print("have folder realy")
        sys.exit()
    else:
        os.mkdir(foldername)
        print("create Foldername")
        os.chdir(foldername)

    net_configs = []

    with open(dev_file_path,'r') as f:
        devices = json.load(f)


    with open(config_path,'r') as config_path_list:
        for config in config_path_list:
            config = config.strip()
            net_configs.append(config)
        print(net_configs)

    with Pool(max_workers=6) as t :
        for device , net_config in zip(devices,net_configs):
            task = t.submit(auto_config,device,net_config)
        print(task.result())


if __name__ == '__main__':
   print(os.getcwd())
   dev_info = 'D:\\code\\netmiko\\templates\\logn3.json'
   conf_path ='D:\\code\\netmiko\\templates\\config_path.txt'
   main(dev_file_path=dev_info,config_path=conf_path)



