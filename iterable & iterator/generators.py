'''
yield
yiled 工作原理类似于return、不过这种特性只有在用在循环遍历的时候才会这样
在 Python 中, generator(生成器)是一种特殊类型的函数 , 可以用来生成一个序列 , 而不需要在内存中存储所有的值。
Generator 使用 yield 关键字来产生值 , 并且每次返回一个值后暂停执行 , 等待下一次调用时再恢复执行'''

gen = (i**2 for i in range(10000))     # 生成器生成式

# yield 和生成器是固定搭配 , 当然也可以用第45行直接创建生成器

# 以下是生成器的优势
"""
1, 惰性计算 : 生成器只在需要时才会生成值 , 而不是一次性生成所有的值。
这种惰性计算可以节省大量的内存 , 并且在处理大量数据时可以显著提高性能。

2, 可以无限扩展 : 由于生成器是在需要时动态生成值的 , 因此它们可以无限扩展 , 而不会受到内存限制。

3, 更加简洁 : 使用生成器可以使代码更加简洁和易于理解。
相比于使用列表等容器类型 , 使用生成器可以避免很多中间变量的定义和操作 , 从而使代码更加简洁。

4, 更加灵活 : 由于生成器可以动态生成值 , 并且可以在任何时候中断和恢复执行,
因此它们非常灵活 , 可以用于处理各种类型的数据和算法。"""


def sayi_say(max):
    sayi = 1
    while sayi <= max:
        yield sayi          # 创建迭代器对象是需要用到 yield
        sayi += 1


generator = sayi_say(10)
print(type(generator))
# print(help(generator))

print(next(generator))      # 1
print(next(generator))      # 2
print("因为生成器是惰性的 , 所以他结束调用时只会在停在原地 , 等待下一次调用才会恢复执行")
# 下面的遍历是从 3 开始的 ,  因为生成器之前在 2 的时候停止调用 , 就停在原地了
for i in generator:        # 生成器可以用for遍历 , 这点和iterator不一样
    print(i)

# sonuc = list(generator)

generator = (i for i in range(1, 11))         # 快速创建生成器 , 类似于列表生成式

print(next(generator))
print(next(generator))
# print(dir(generator))
# 生成器里也有__iter__和__next__


# 斐波那契数列
def fibonacci():
    a, b = 0, 1
    while True:
        yield a         # 类似于return, 返回到斐波那契数列中数字num、并在下一次调用时恢复执行
        a, b = b, a + b


# 使用 for 循环打印前 10 个斐波那契数列的值
for i, num in enumerate(fibonacci()):        # 再次调用的时候会到达56行
    if i >= 10:                              # 因为上次在yiled暂定执行、现在再次调用的时候会恢复执行
        break
    print(num)
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
gen = (i**2 for i in range(10000))     # 生成器生成式