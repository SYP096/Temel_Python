import time
with open("Notlar.txt", 'r', encoding='utf-8') as file:
    for satir in file.readlines()[:-1]:
        print(satir)
        print(len(satir))
        print(satir[5])
        ss = satir.split(':')
        print(ss[0])
        print(ss[1])
'''
如果不带那个[:-1]的话、最后一行空值也会被循环、空行(空值)只有一个单位、所以会报错

然后就是别用read()、那个东西可以用来读、但是他的索引是有问题的可以说是把整个文本都变成一个字符串
所以便利的时候会一个字母一个字母的遍历'''

with open("Notlar.txt", 'r', encoding='utf-8') as file:
    print(file.read())
    file.seek(0)
    print(len(file.read()))   # 128  可以看出file.read()是一个字符串
    file.seek(0)
    # for i in file.read():
    #     print(i)               # 可以看到是一个字母一个字母输出的

with open("Notlar.txt", 'r', encoding='utf-8') as file:
    for satir in file:
        print(satir[:-1])
        print(type(satir[:-1]))

'----------------------第一种方法----------------'
start_time = time.time()
with open("Notlar.txt", 'r', encoding='utf-8') as file1:
    for i in file1:
        with open("denemedosya.txt", 'a', encoding='utf-8') as file2:
            file2.write(i)
last_time = time.time()
print(last_time - start_time)    # 0.05010819435119629
'--------------------第二种方法------------------'
start_time = time.time()
liste = []
with open("Notlar.txt", 'r', encoding='utf-8') as file1:
    for i in file1:
        liste.append(i)

    with open("Sonuclar.txt", 'w', encoding='utf-8') as file2:
        for i in liste:
            file2.write(i + '\n')
last_time = time.time()
print(last_time - start_time)     # 0.001003265380859375
# 这样也可以、结果和想象的一模一样、然后就是抽时间了检测一下哪个更节省内存和时间
# 事实证明、一次性打开文件比多次打开文件要更加的节省时间  ---文本内部有300行的时候做的测试
