# coding:utf-8

import threading
import time
import queue

# 创建队列
q = queue.Queue()


# 生产者
def Producer(name):
    for i in range(10):
        q.put(i)
        print('{} 生产的蛋糕{}'.format(name, i))

# 将制作的小蛋糕放入队列中


# 消耗者
def Consumer(name):
    count = 0
    while True:
        data = q.get()
        count = count + 1
        print(name,"吃蛋糕:", data)
        if count == 4:
            break


# 取出蛋糕并吃掉


if __name__ == '__main__':
    # 创建线程，一个生产者，三个消费者
    p = threading.Thread(target=Producer, args=('慕慕',))
    c1 = threading.Thread(target=Consumer, args=('小明',))
    c2 = threading.Thread(target=Consumer, args=('小红',))
    c3 = threading.Thread(target=Consumer, args=('安安',))
    thread_queue = [p, c1, c2, c3]
    for i in thread_queue:
        if i != p:
            # c1,c2,c3 设置为守护线程模式 ，主进程不会等这三个执行完才退出 同时 主进程退出时，这三个也一起退出
            i.daemon = True
        i.start()
    p.join()

