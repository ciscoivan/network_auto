# coding:utf-8

import threading


class Candy(object):
    def __init__(self):
        self.childs = list(range(1, 6))
        self.candys = list( range(100))
        self.res = {}
        self.count = 0

    def divide_candy(self):
        candy = []
        while len(self.candys) > 0:
            if len(candy) < 20:
                c = self.candys.pop()
                candy.append(c)
                if len(candy) == 20:
                    self.res[self.childs[self.count]] = candy
                    self.count += 1

    def thread(self):
        for i in self.childs:
            t = threading.Thread(target=self.divide_candy)
            t.start()


if __name__ == '__main__':
    one_child = Candy()
    one_child.thread()
    print(one_child.res)
