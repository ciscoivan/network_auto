
# coding:utf-8

import os
import time
import multiprocessing


def work(count, lock):
    #lock.acquire()
    print(count, os.getpid())
    time.sleep(5)
    #lock.release()
    return 'result is %s, pid is %s' % (count, os.getpid())


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)
    manger = multiprocessing.Manager()
    lock = manger.Lock()
    results = []
    for i in range(20):
        result = pool.apply_async(func=work, args=(i, lock))
        # results.append(result)

    # for res in results:
    #     print(res.get())

    pool.close()
    pool.join()
