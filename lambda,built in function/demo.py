lis = ['3', '4', '5', '6', '7']
print(lis)
for i in range(len(lis)):
    lis[i] = int(lis[i])
print(lis)
'''
map()是python内置的高阶函数, 他接收一个函数 f 和一个 list ,
并通过函数 f 依次作用在 list 的每个元素上, 得到一个新的list并返回
'''
sonuc = list(map(int, lis))       # 这一行代码就等于上面那些行代码
print(sonuc)
sonuc = list(map(lambda a: a ** 2, sonuc))
print(sonuc)


def demo1(n):
    return lambda a: a ** n


demo = demo1(3)      # 同等于 demo = (lambda a: a** 3), 这样输入必须加括号
print(demo(2))
demo3 = (lambda a: a ** 3)
print(demo3(3))

users = [
    {"username": "sadikturan",
     "tweets": ["tweet 1", "tweet 2"], "email": "info@gmail.com"},

    {"username": "cinarturan",  "tweets": []},

    {"username": "senaturan",
     "tweets": ["tweet 1"], "name": "", "phone": "434312134"}
]
sonuc = sorted(users, key=lambda use: len(use))    # 根据键值对的数量排序
sonuc = sorted(users, key=lambda use: len(use['tweets']), reverse=True)
# Tweeets 大到小
sonuc = sorted(users, key=lambda use: use['username'])
sonuc = max(users, key=lambda user: user['tweets'])
print(sonuc)
sonuc = max(users, key=lambda user: user['username'])
print(sonuc)
sonuc = min(users, key=lambda user: user['tweets'])

print(sonuc)
