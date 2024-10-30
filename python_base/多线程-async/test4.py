# coding:utf-8

import time
import threading

from concurrent.futures import ThreadPoolExecutor, thread

lock = threading.Lock()

def work(i):
    lock.acquire()
    print(i)
    time.sleep(1)
    lock.release()


if __name__ == '__main__':
    t = ThreadPoolExecutor(2)
    result = []
    for i in range(20):
        res = t.submit(work, (i,))
        #result.append(res)

    # for r in result:
    #     print(r.result())
