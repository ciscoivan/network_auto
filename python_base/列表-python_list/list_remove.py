# coding:utf-8

shops = ['可乐', '洗发水', '可乐', '牛奶', '牛奶', '牙膏', '牙膏']

print('我们的超市有这些内容:%s' % shops)
print('我们的可乐有%s件产品' % shops.count('可乐'))
print('我们的牛奶有%s件产品' % shops.count('牛奶'))
print('我们的牙膏有%s件产品' % shops.count('牙膏'))
print('我们的洗发水有%s件产品' % shops.count('洗发水'))
print('我们要购买一件洗发水')
shops.remove('洗发水')
print('现在我们的洗发水还剩下%s件, 当前已经没有洗发水了' % shops.count('洗发水'))
shops.remove('可乐')
print('当前可乐还有%s' % shops.count('可乐'))
shops.remove('可乐')
print('可乐还有%s件' % shops.count('可乐'))

del shops

print(shops)
