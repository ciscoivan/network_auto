# coding:utf-8

animals = ['小猫', '小狗', '龙猫', '小猫', '鹦鹉', '小狗', '小兔子', '小猫']

cat = animals.count('小猫')
dog = animals.count('小狗')
l_cat = animals.count('龙猫')
rabbit = animals.count('小兔子')

print('我家的院子里有很多小动物')
print('其中小猫有 %s 只' % cat)
print('小狗有 {} 只'.format(dog))
print(f'龙猫有 {l_cat} 只')
print('小兔子有 %d 只' % rabbit)
print('我们没有小松鼠， 所以松鼠有  %s 只' % animals.count('松鼠'))

animals_dict = [
    {'name': 'dog'},
    {'name': 'dog'},
    {'name': 'cat'}
]

dog_dict_count = animals_dict.count({'name': 'dog'})
print('小狗在动物的字典中有%s只' % dog_dict_count)

animals_tuple = ('小猫', '小狗', '龙猫', '小猫',
           '鹦鹉', '小狗', '小兔子', '小猫')

cat = animals_tuple.count('小猫')
dog = animals_tuple.count('小狗')
l_cat = animals_tuple.count('龙猫')
rabbit = animals_tuple.count('小兔子')

print('其中小猫有 %s 只\n小狗有 %s 只\n龙猫有 %s 只\n小兔子有%s只'
      % (cat, dog, l_cat, rabbit))
