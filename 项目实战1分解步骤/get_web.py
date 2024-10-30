import requests
from urllib3 import encode_multipart_formdata

file_session = requests.Session()
login_data = {"user": "root", "pwd": "123.com"}
file_session.post('http://192.168.30.5:8080/#/ios', data=login_data)


file = r'backup.py'

# 上传文件的路径

file_data = {'file': open(file, 'rb'),'folder': (None,"/ios")}
resp = file_session.post('http://192.168.30.5:8080/chfs/upload', files=file_data)
print(resp)
if resp.ok:
    print('上传成功:', file)

else:
    # 文件已存在在目录中, 不能覆盖
    print('上传失败:', file)




"""
download_url = "http://192.168.30.5:8080/#/ios"
resp = file_session.get(download_url + 'vmware vsphere 6.0 keygen.exe')
with open('vmware vsphere 6.0 keygen.exe', mode='w', encoding='utf-8') as f:
    f.write(resp.text)
"""