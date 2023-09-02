# filtre() 过滤,  filtre(function, iterables,....)
# filtre 会遍历 iterables 中的每一个数据, 用 function 判断,  符合条件(True), 才会留下
# input:   function : 判断函数               iterables: 可迭代对象,  列表, 元组, 集合, 字典都可以
# output: 输出是一个迭代器对象,  要用到 list() 使其转变为可迭代序列(iterables)
# 也要用到 list
yaslar = [5, 12, 18, 24, 45]


def yetiskinmi(x):
    if x < 18:
        return False
    else:
        return True


sonuc = list(filter(yetiskinmi,  yaslar))
sonuc = list(filter(lambda x: x >= 18,  yaslar))

sayilar = [0, 1, 25, 6, 8, 9]
sonuc = list(filter(lambda x: x % 2 != 0,  sayilar))      # 单数

isimler = ["çinar", "yiğit", "sena", "ada", "ali"]
sonuc = list(filter(lambda n: n[0] == 'a', isimler))

filteredResult = filter(lambda n: n[0] == 'a', isimler)
sonuc = list(map(lambda n: n.upper(),  filteredResult))

users = [
    {"username": "sadikturan",  "tweets": ["tweet 1", "tweet 2"]},
    {"username": "cinarturan",  "tweets": []},
    {"username": "senaturan",  "tweets": ["tweet 1"]}
]
'''迭代器对象iterator也是有序的, 可以迭代的, 是一组数据流,  所以可以想35行那样使用'''
sonuc = list(filter(lambda u: len(u["tweets"]) > 0,  users))
sonuc = list(map(lambda u: u["username"].upper(),
                 filter(lambda u: len(u["tweets"]) > 0,  users)))

sonuc = [user["username"].upper() for user in users if len(user["tweets"]) > 0]
# 和第35行输出一样
sonuc = filter(lambda u: len(u["tweets"]) > 0,  users)
print(sonuc)

'''
这里讲一下iterable(可迭代对象), iterator(迭代器对象)
iterable就是我们常见的列表之类的数据组, 可以直接拿来使用
iterator 的输出是这样的<filter object at 0x00000267AC323A00>
这是一个可迭代的, 甚至使用for循环可以对iterator进行遍历, 且不会报错, 会一次输出迭代器中的所有值
总之, iterator是一个有序的数据流, 提前不知道它的长度, 他是惰性计算的'''
