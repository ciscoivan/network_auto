import xlwt

# 合并第0行的第0列到第3列。
# worksheet.write_merge(0, 0, 0, 3, 'First Merge')
# worksheet.write(0, 0, label='this is test')

#
# # # 合并第1行到第2行的第0列到第3列。
# # worksheet.write_merge(1, 2, 0, 3, 'Second Merge', style)
# #
# # worksheet.write_merge(4, 6, 3, 6, 'My merge', style)
# http://t.zoukankan.com/gtea-p-12752626.html 参考了这段代码

if __name__ == '__main__':
    # 数据按设备规整好，可以是通过别的方式得到的自动化结果 或者是中间产生的表格读取加载成字典的列表
    raw_data = [
        {'dev': 'as01', 'ip': '192.168.1.1', 'name': '端口检查', 'result': '100个 ok'},
        {'dev': 'as01', 'ip': '192.168.1.1', 'name': 'cpu', 'result': 'ok'},
        {'dev': 'as01', 'ip': '192.168.1.1', 'name': '端口检查', 'result': '100个 ok'},
        {'dev': 'as01', 'ip': '192.168.1.1', 'name': 'cpu', 'result': 'ok'},
        {'dev': 'as02', 'ip': '192.168.1.2', 'name': '端口检查', 'result': '100个 ok'},
        {'dev': 'as02', 'ip': '192.168.1.2', 'name': 'cpu', 'result': 'ok'},
        {'dev': 'as02', 'ip': '192.168.1.2', 'name': '端口检查', 'result': '100个 ok'},
        # {'dev': 'as02', 'ip': '192.168.1.2', 'name': 'cpu', 'result': 'ok'},

    ]

    # 字体
    font = xlwt.Font()
    font.blod = True
    # 样式
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 5

    # 对齐方式
    alignment = xlwt.Alignment()
    # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
    alignment.horz = 0x02
    # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
    alignment.vert = 0x01

    # 边框
    borders = xlwt.Borders()
    # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
    # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
    borders.left = 2
    borders.right = 2
    borders.top = 2
    borders.bottom = 2
    # borders.left_colour = i
    # borders.right_colour = i
    # borders.top_colour = i
    # borders.bottom_colour = i

    style = xlwt.XFStyle()
    style.font = font
    style.pattern = pattern
    style.alignment = alignment
    style.borders = borders

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('巡检')
    # 设置列宽，一个中文等于两个英文等于两个字符，11为字符数，256为衡量单位
    worksheet.col(0).width = 20 * 256
    worksheet.col(1).width = 20 * 256
    worksheet.col(2).width = 30 * 256
    worksheet.col(3).width = 40 * 256

    # 写入表头，写到了第一行
    worksheet.write(0, 0, label='设备名')
    worksheet.write(0, 1, label='ip')
    worksheet.write(0, 2, label='检查项')
    worksheet.write(0, 3, label='结果')

    index = 1
    # 合并单元格的起始
    merge_start_index = 1
    merge_end_index = 1
    rows = len(raw_data)
    while index <= rows:
        # 由于第一行（索引0）有数据，我们写的实际数据索引在表格里需要从1开始，而在数据列表中又是从0开始，实际差了1个索引值，这块要注意
        # 当前数据
        data = raw_data[index - 1]
        # 先写巡检项，和巡检结果
        worksheet.write(index, 2, label=data['name'], style=style)
        worksheet.write(index, 3, label=data['result'], style=style)
        # 当前设备
        current_dev = data['dev']
        # 下一行设备 当index 比row小的时候，可以取到下一设备，
        if index < rows:
            next_dev = raw_data[index]['dev']
        # else 即当index==row则代表读取到了末尾，下一个设备置为空，可以触发下一个合并的判断条件，从而结束并合并单元格
        else:
            next_dev = None
        # 本行dev和下一个是同台设备，则合并的index移动到下一行
        if current_dev == next_dev:
            merge_end_index = index + 1
        # 否则本行设备与下一行是不同设备则需要合并单元格
        else:
            worksheet.write_merge(merge_start_index, merge_end_index, 0, 0, data['dev'], style)
            worksheet.write_merge(merge_start_index, merge_end_index, 1, 1, data['ip'], style)
            # 同时合并单元的index移动到下一行
            merge_start_index = merge_end_index = index + 1
        index += 1
    workbook.save('巡检.xls')
