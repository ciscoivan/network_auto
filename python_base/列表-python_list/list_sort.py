# coding:utf-8

shu = '01老鼠'
niu = '02牛'
hu = '03老虎'
tu = '04兔'
long = '05龙'
she = '06蛇'
ma = '07马'
yang = '08羊'
hou = '09猴'
ji = '10鸡'
gou = '11狗'
zhu = '12猪'

shengxiao = []
shengxiao.append(gou)
shengxiao.append(ji)
shengxiao.append(zhu)
shengxiao.append(she)
shengxiao.append(tu)
shengxiao.append(hou)
shengxiao.append(hu)
shengxiao.append(niu)
shengxiao.append(shu)
shengxiao.append(long)
shengxiao.append(ma)
shengxiao.append(yang)

print(shengxiao)
print(len(shengxiao))
shengxiao.sort()
print(shengxiao)
shengxiao.sort(reverse=True)
print(shengxiao)
shengxiao.sort(reverse=True)
print(shengxiao)


mix = ['python', 1.2, {'name': 'dewei'}]
