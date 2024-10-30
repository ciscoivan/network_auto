# coding:utf-8

import time
import json
import multiprocessing

class Work(object):
    def __init__(self, q):
        self.q = q

    def send(self, message):
        if not isinstance(message, str):
            message = json.dumps(message)
        self.q.put(message)

    def send_all(self):
        for i in range(20):
            self.q.put(i)
            time.sleep(1)

    def receive(self):
        while 1:
            result = self.q.get()
            try:
                res = json.loads(result)
            except:
                res = result
            print('recv is %s' % res)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    work = Work(q)
    send = multiprocessing.Process(target=work.send, args=({'name': '小慕'},))
    recv = multiprocessing.Process(target=work.receive)
    send_all_p = multiprocessing.Process(target=work.send_all)

    send_all_p.start()
    recv.start()
    send.start()


    send_all_p.join()
   # recv.terminate()  #终止因为whle = 1 的循环

