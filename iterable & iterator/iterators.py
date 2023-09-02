# iterable?     可迭代对象
'''如果只实现了__iter__的话 , 就只是可迭代对象'''
# iterator?     迭代器对象       iter()
# 迭代器对象像可迭代对象一样 ,  可以用 for 遍历
'''迭代器是一个能够在容器对象上遍历并访问该容器对象中的元素的对象。
在Python中, 任何实现了__iter__和__next__方法的对象都是迭代器。必须同时实现__iter__和__next__
    __iter__方法返回迭代器对象自身。
    __next__方法返回容器中的下一个元素。当迭代器中没有元素时, 抛出StopIteration异常。

迭代器对象可以用于遍历容器对象的元素, 因此在Python中, 常常使用迭代器来遍历序列、列表、字典、集合等可迭代对象。

例如, 我们可以使用内置函数iter()来创建一个迭代器对象, 然后使用next()函数来访问容器中的元素:
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
print(next(my_iterator))  # 4
print(next(my_iterator))  # 5
print(next(my_iterator))  # StopIteration

'''
sayilar = [1, 2, 3, 4, 5]

iterator = iter(sayilar)          # 是可迭代对象sayilar转化成迭代器
print(iterator)         # <list_iterator object at 0x0000022C344A9A50>

# while True:
#     try:
#         sayi = next(iterator)         # next函数是用来遍历迭代器的。
#         print(sayi)
#     except StopIteration:
#         break

print(next(iterator))
print(next(iterator))
print("------------------迭代器对象也是惰性的-------------------")
for i in iterator:       # for 遍历迭代器
    print(i)

# 以下是迭代器的优势
'''
1, 节省内存: 迭代器对象只在需要时生成数据, 不会在内存中一次性存储所有的数据, 因此可以节省内存。

2, 支持惰性计算: 与生成器类似, 迭代器对象也支持惰性计算, 只在需要时才会生成数据。
这种特性可以在处理大量数据时提高效率。

3, 具有通用性: 迭代器对象可以用于处理各种类型的数据, 包括列表、字典、集合等等。 用  iter()

4, 可以实现自定义的迭代器:
在 Python 中, 我们可以自己定义一个迭代器对象, 使得我们可以按照自己的方式遍历容器中的元素。'''
