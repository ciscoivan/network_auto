# coding:utf-8

import time
import datetime

now = time.time()
print(now, type(now))

time_obj = time.localtime(now)
print(time_obj, type(time_obj))
# time.sleep(5)
current_time_obj = time.localtime()
print(current_time_obj)

before = now - 100000
before_time_obj = time.localtime(before)
print(before_time_obj)

print(time.time() * 1000)
print(time.time())

# for i in range(10):
#     print(i)
#     time.sleep(1)

datetime_now = datetime.datetime.now()
datetime_timestamp = datetime.datetime.timestamp(datetime_now)
print('datetime 生成的时间戳 %s' % datetime_timestamp)

datetime_obj = datetime.datetime.fromtimestamp(datetime_timestamp)
print(datetime_obj)
