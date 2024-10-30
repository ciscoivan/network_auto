import random
import threading
from concurrent.futures import ThreadPoolExecutor
#生成奖品
gifts = ['手机', '平板电脑', '加湿器'] + ['未中奖' for i in range(30)]
#生成手机号
phone_numbers = range(13000000000, 18900000000)
phone_numbers = random.sample(phone_numbers, 20)

#定义线程锁
lock = threading.Lock()
def lottery():
    lock.acquire()
    #奖品中池没有奖品结束抽奖
    if len(gifts) == 0:
        print('抽奖已结束')
    else:
        #随机抽取手机号
        phone = random.choice(phone_numbers)
        #随机抽取奖品池中奖品
        res = random.choice(gifts)
        #删除奖品池中奖品
        gifts.remove(res)
        # 抽过奖后删除手机号
        phone_numbers.remove(phone)
        #判断中的几等奖
        if res == '手机':
            print('恭喜手机号为{}的朋友获得一等奖：手机，价值3999元'.format(phone))
        elif res == '平板电脑':
            print('恭喜手机号为{}的朋友获得二等奖：平板电脑，价值1999元'.format(phone))
        elif res == '加湿器':
            print('恭喜手机号为{}的朋友获得三等奖：加湿器，价值198元'.format(phone))
        else:
            print('抱歉手机号为{}的朋友未中奖'.format(phone))
    lock.release()
if __name__ == '__main__':
    #创建线程池
    t=ThreadPoolExecutor(3)
    #执行20个任务
    for i in range(20):
        t.submit(lottery)