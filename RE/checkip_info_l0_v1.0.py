# 0 定义两个比较变量
info_center_ip = ''
inter_loop0_ip = ''

# 1 找 info_center_ip 
f = open('../../../wchat/WeChat Files/wxid_xmpw2zlrrb6m21/FileStorage/File/2022-05/实战2-配置上下文检查（代码不唯一，仅供参考）/demo.txt')
found = 0
while found ==0:
    line = f.readline()
    if line.startswith('info-center loghost 192.168.10.1 source-ip'):
        info_center_ip = line.split()[-1]
        found = 1
        #print(info_center_ip)
f.close()

# 2 找 inter_loop0_ip 
f = open('../../../wchat/WeChat Files/wxid_xmpw2zlrrb6m21/FileStorage/File/2022-05/实战2-配置上下文检查（代码不唯一，仅供参考）/demo.txt')
found = 0
while found==0:
    line = f.readline()
    if line.startswith('interface LoopBack0'):
        line = f.readline()
        while line.startswith(' '):
            if line.startswith(' ip address '):                  
                inter_loop0_ip = line.split()[-2]
                found = 1
                #print(inter_loop0_ip)
                #break
            line = f.readline()
f.close()

# 3 比较两个IP
if info_center_ip==inter_loop0_ip:
    print(f"核查无误，均为{info_center_ip}")
else:print(f"核查有误！！！\
           \ninfo_center_ip：{info_center_ip}\
           \ninter_loop0_ip：{inter_loop0_ip}")


# 这样写效率很低，只是先把功能实现，然后慢慢可以调优这脚本。
# 用上循环解决多台设备配合，用上正则，用上Textfsm
# 读取部分封装成函数，异常检测，增加测试模块……
