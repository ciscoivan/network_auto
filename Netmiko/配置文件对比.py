import difflib

sw1 = open('02b202.txt').read()   #打开配置文件,加.read()之后类型是‘str’
sw2 = open('BR2.txt').read()
diff = difflib.HtmlDiff()
htmlout = diff.make_file(sw1.splitlines(keepends=True),sw2.splitlines(keepends=True))    #对比输出html结果
with open('htmlout.html', 'w') as f:                                 #推荐使用此方法，html彩色显示
    f.write(htmlout)
    print("结果分别分析结果在本地html显示")


#diffd = list(difflib.ndiff(sw1.splitlines(keepends=True),sw2.splitlines(keepends=True)))
#for i in diffd :
#    print(i)                #显示不够直观，根据 +，-，？，^^等标识修改地方