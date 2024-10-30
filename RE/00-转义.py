import re

if __name__ == '__main__':
    # \n代表了换行，是有转义意义的
    a = '后面会有一个换行，\n第二行开始'
    print(a)

    # 使用r 取消其转移意义

    a = r'后面不会有换行，因为\n被r给取消了转义意义，表示的是“\n”这个字符串本身'
    print(a)
    #
    text = '这里面有数字789'
    print('\\d')
    # 先进行字符串转义，将\\d转为实际的字符串，\d 然后在正则中使用\d匹配
    example_re = re.compile('\\d')
    results = example_re.findall(text)
    if results:
        print(results)
    #
    # # \d在字符串中无实际意义，所以此处打印出来的是\d本身，如果写的是\t，是有转义意义的 就会显示是tab
    # # r取消了第一步的字符串转义，直接用此字符串去进行正则匹配
    # print(r'\d')
    # example_re = re.compile(r'\d')
    # results = example_re.findall(text)
    # if results:
    #     print(results)
