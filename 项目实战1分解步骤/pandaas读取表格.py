import netmiko
import os
import  pandas as pd
from  openpyxl import load_workbook

class BackupConfig(object):
    def __init__(self):
        self.device_file = "dev-info.xlsx"



    def get_devices_info(self):

        try:
          names = ['comment','ip','protocol','port','username','password','secret','device_type']
          df = pd.read_excel(self.device_file,usecols='B:I',names=names,keep_default_na=False)
          data = df.to_dict(orient='records')
          for row in data:
              if row['comment'] == '#':
                  continue

              row['cmd_list'] = self.get_cmd_info(row['device_type'])
              yield  row
        except Exception as e :
            print('error',e)



    def get_cmd_info(self,cmd_sheet):
        cmd_list = []
        try:
            names = ['comment','cmd']
            df = pd.read_excel(self.device_file,sheet_name=cmd_sheet,usecols='A:B',names=names,keep_default_na=False)
            data = df.to_dict(orient='records')
            for row in data:
                if row['comment'].strip() != '#' and row['cmd']:
                    cmd_list.append(row['cmd'].strip())

            return cmd_list

        except Exception as e:
            print('get_cmd_error',e)


    def connect(self):
        hosts  = self.get_devices_info()
        for host in hosts:
            print(host)

if __name__ == '__main__':
    BackupConfig().connect()
