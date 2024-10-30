if __name__ == '__main__':
    '''
    open 内置函数，打开一个文件，mode 默认是r，encoding 默认为空，会根据系统本身的编码方式进行编解码。我们的windows多是GBK
    强烈建议，大家在保存、打开文本文件的时候都统一使用utf8（utf8大小写均可，-号有无均可）
    encoding 的utf8 大小写均可，也可以写成utf-8
    强烈建议，大家使用with+open打开文件，可以管理上下文，在程序离开的时候优雅的关闭文件，防止一些意外。
    '''
    # 普通读的方法，一次性全部读出文本
    # f = open('test.txt', mode='r', encoding='utf8')
    # text = f.read()
    # # 读取完内容后，建议关闭文件。
    # print(text)
    # f.close()

    # with open 上下文管理
    with open('test.txt', mode='r', encoding='utf8') as f:
        text = f.read()
        print(text)
    # 退出with的管辖范围之后，文件被关闭，无法再次read访问打开。



    # '''
    # 文件过大，一次性读入会使内存消耗，甚至溢出
    # 比较pythonic的方法是如下
    # 它会一行一行的打开文件，不会像read那样一次性读出所有的，我们根据实际文件大小去定，如果性能出现问题，可以如此调整
    # '''
    with open('test.txt', mode='r', encoding='utf8') as file:
        for line in file:
            print((line,)) # 此处通过把创建一个tuple可以观察到换行符，每行均会保留末尾的换行
    