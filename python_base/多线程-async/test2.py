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

    def recv(self):
        while 1:
            res = self.q.get()
            try:
                result = json.loads(res)
            except:
                result = res
            print('recv is %s' % result)


if __name__ == '__main__':
    q = multiprocessing.Queue()
    work = Work(q)
    send_p = multiprocessing.Process(target=work.send, args=({'name': 'dewei'},))
    recv_p = multiprocessing.Process(target=work.recv)
    send_all_p = multiprocessing.Process(target=work.send_all)
    send_all_p.start()

    send_p.start()
    recv_p.start()

    send_p.join()
    #recv_p.terminate()