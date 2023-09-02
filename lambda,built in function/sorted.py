'''
sorted() 是python的内置函数
iterable 为可迭代对象,   cmp 用于比较的对象,  比较什么由key决定
key 用列表元素的某个属性 或 函数进行作为  关键字  ,  有默认值,  迭代集合中的一项
reverse : reverse = False, 升序,   reverse = True,  降序,   默认为升序
'''
# sorted()  的输出永远是   list
# 其中  key  最为重要，可以是函数lambda，也可以是内置函数len等

sayilar = [1, 53, 45, 67, 97, 5, 7]

# sayilar.sort()   这个是在列表基础上进行的排序，排序过后无法回到原始列表
sonuc = sorted(sayilar)
sonuc = sorted(sayilar,  reverse=True)
sonuc = sorted((1, 53, 45, 67, 97, 5, 7))    # 元组也可以输出为列表
print(sonuc)

users = [
    {"username": "sadikturan",
     "tweets": ["tweet 1", "tweet 2"], "email": "info@gmail.com"},
    {"username": "cinarturan",
     "tweets": []},
    {"username": "senaturan",
     "tweets": ["tweet 1"], "name": "", "phone": "434312134"}
]

sonuc = sorted(users, key=len)
print(sonuc)
sonuc = sorted(users, key=len,  reverse=True)
print(sonuc)
sonuc = sorted(users, key=lambda user:  user["username"])       # 根据名字的首字母大小写
print(sonuc)
sonuc = sorted(users, key=lambda user:  len(user["tweets"]))
print(sonuc)

kurslar = [
    {"title": "python kursu", "students": 25000},
    {"title": "web geliştirme kursu", "students": 35000},
    {"title": "javascript kursu", "students": 5000}
]

sonuc = sorted(kurslar,  key=lambda kurs:  kurs["students"])
print(sonuc)
sonuc = sorted(kurslar,  key=lambda kurs:  kurs["students"], reverse=True)
print(sonuc)
sonuc = map(lambda kurs:  kurs["title"],
            sorted(kurslar, key=lambda kurs:  kurs["students"], reverse=True))

print(list(sonuc))

dic = {
        'a': 3, 'b': 7, 'c': 5
}
# 在键名不同的情况下，如何根据值来排序？ 看以下例子
aa = sorted(dic.items(), key=lambda a: a[1])
# 当多个值进入到 lambda 时,  这些值在进入lambda的那一刻就自动组成了元组
print(aa)
aa = sorted(dic.values())
print(aa)
