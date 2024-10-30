# coding:utf-8

import random
import time
import threading


lists = ['dewei', 'xiaomu', 'xiaowang', 'xiaohua', 'xiaoman', 'xiaoli']
new_lists = []

def work():
    if len(lists) == 0:
        return
    data = random.choice(lists)
    lists.remove(data)
    new_data = '%s_new' % data
    new_lists.append(new_data)
    time.sleep(5)

if __name__ == '__main__':
    start = time.time()
    result = []
    for i in range(len(lists)):
        t = threading.Thread(target=work)
        result.append(t)
        t.start()

    # for i in result:
    #     i.join()

    print(new_lists)
    print(lists)
    print('time is %s' % (time.time() - start))

