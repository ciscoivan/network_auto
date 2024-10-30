# coding:utf-8

from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now, type(now))
now_str = now.strftime('%Y-%m-%d %H:%M:%S')
print(now_str, type(now_str))
now_obj = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S')
print(now_obj, type(now_obj), '----')

three_days = timedelta(days=3)
after_three_day = now + three_days
print(after_three_day)
after_three_day_str = after_three_day.strftime('%Y/%m/%d %H:%M:%S')
print(after_three_day_str, type(after_three_day_str))
after_three_day_obj = datetime.strptime(after_three_day_str, '%Y/%m/%d %H:%M:%S')
print(after_three_day_obj, type(after_three_day_obj), '----')

before_three_day = now - three_days
print(before_three_day)
before_three_day_str = before_three_day.strftime('%Y%m%d')
print(before_three_day_str, type(before_three_day_str))
before_three_day_obj = datetime.strptime(before_three_day_str, '%Y%m%d')
print(before_three_day_obj, type(before_three_day_obj), '-----')

one_hour = timedelta(hours=1)
before_one_hour = now - one_hour
print(before_one_hour)
before_one_hour_str = before_one_hour.strftime('%H:%M:%S')
print(before_one_hour_str, type(before_one_hour_str))

# default_str = '2020 12 abc'
# print(datetime.strptime(default_str, '%Y %m'))


