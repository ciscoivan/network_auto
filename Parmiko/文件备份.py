import  os
import  os.path


class fileback(object):

    def __init__(self,src,dist):
        self.src = src
        self.dist = dist


    def read_files(self):
        ls = os.listdir(self.src)
        print("读取目录文件")
        print(ls)
        for l in ls:
            self.backup_file(l)


    def backup_file(self,file_name):
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print("指定的目录不存在创建完成")

        full_path = os.path.join(self.src,file_name)
        print(full_path)
        full_dist_path = os.path.join(self.dist,file_name)
        print(full_dist_path)

        if os.path.isfile(full_path) and os.path.splitext(full_path)[-1].lower() == '.txt'or os.path.splitext(full_path)[-1].lower() == '.py':
            with open(full_dist_path,'w',encoding='utf8') as f_dist:
                print("开始备份{0}".format(file_name))
                with open(full_path,'r',encoding='utf-8') as f_src:
                    while True:
                        rest = f_src.read(100)
                        if not rest:
                          break
                        f_dist.write(rest)
                    f_dist.flush()
                    print("备份完成{0}".format(file_name))
        else:
            print("文件类型不和要求跳过》》")



if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_path, 'cisco\src')
    dist_path = os.path.join(base_path, 'cisco\dist')
    bak = fileback(src_path,dist_path)
    bak.read_files()
