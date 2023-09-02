# 第一步就是打开文件、不打开文件你啥也干不了
f = open("msg.txt", encoding='utf-8')
print(f)
# <_io.TextIOWrapper name='E:\\my_project\\Udemy课件\\Dosya yonetimi\\msg.txt' mode='r' encoding='cp936'>

print(f.read())
print(f.read())

f.seek(0)
print(f.readable())

f.seek(0)      # 回到第一行
# 0
# >>> f.read()
# 'hello world.\nevewv\nvwevwev\nffwefwf\negweg'
# >>> f.read()
# '\nyeni satır'
f.seek(5)    # 去到第五行
# 5
# >>> f.read()
# ' world.\nevewv\nvwevwev\nffwefwf\negweg\nyeni satır'
# >>>
# >>> f.seek(0)
# 0
f.readline()        # 只读一行，然后执行结束后停在原地
# 'birinci satır.\n'
f.readline()
# 'ikinci satır.\n'
f.readline()
# 'üçüncü satır.\n'
f.readline()
# 'dördüncü satır.\n'
f.readline()
# 'beşinci satır.'
f.readline()
# ''
# >>> f.seek(0)          回到最开头
# 0
f.readlines()      # 读每一行、且把每一行都当作一个元素输出为一个列表
# ['birinci satır.\n', 'ikinci satır.\n', 'üçüncü satır.\n',
# 'dördüncü satır.\n', 'beşinci satır.']
# >>> f.seek(0)
# 0
satirlar = f.readlines()
print(satirlar)
# ['birinci satır.\n', 'ikinci satır.\n', 'üçüncü satır.\n',
# 'dördüncü satır.\n','beşinci satır.']
satirlar[0]               # 0. satira gidiyor     去到第零行(第一行)
# 'birinci satır.\n'
satirlar[2]
# 'üçüncü satır.\n'
print(f)
# <_io.TextIOWrapper name='msg.txt' mode='r' encoding='UTF-8'>
f.closed    # 判断   现在文件关闭了吗？
# False
f.close()      # 执行   关闭文件
f.closed
# True
f.seek(0)      # 已经关闭的文件无法执行
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
# >>> f.read()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: I/O operation on closed file.
