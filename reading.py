import csv
# 首先csv是一个模块、运用的时候要以模块或者说class的方式运用
# with open("products.csv") as file:
#     print(file.read())

with open("products.csv") as file:
    csv_reader = csv.reader(file)    # 可以理解为 这个csv_reader就是csv模块中reader类的实例对象
    print(csv_reader)     # output: <_csv.reader object at 0x00000276857C7460>
    next(csv_reader)        # next()就是执行这一行数据、然后停留到下一行数据上
    print(list(csv_reader))
    print('--------------------------')
    file.seek(0)
    for csv_row in csv_reader:
        print(csv_row)               # 从输出可以看到每一行以列表的形式打印出来的
    print('-----------------以下是没卖出去的产品------------------')
    file.seek(0)
    for p in csv_reader:     # 现在在这里还是单个字符串的格式、所以无法正常遍历
        if p[2] == 'False':
            print('Product name: ', p[0], 'Price: ', p[1])
# 如果想要完成15-17行的遍历的话、你需要用到dictreader
# DictReader
