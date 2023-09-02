def usalma(number):
    def inner(power):
        return number ** power        # 作为usalma的内部函数 , 导入usalma的参数也可以在inner中使用

    return inner                # 返回函数inner 到 two = usalma 以及 three........


two = usalma(2)   # 2-3          # 调用函数uslama , 并返回其内部函数 inner       可以这么说  two = inner()
three = usalma(3)   # 3-4
print(help(two))                     # 可以看到现在 two函数已经被替代成了 inner函数
print(two(3))          # 此时的two函数已经被替代为了inner函数, 同时会执行inner函数
print(three(4))       # 同two

# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role, page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
#     return inner

# user1 = yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma


toplama = islem("toplama")
print(toplama(1, 3, 5, 6, 7))

carpma = islem("carpma")
print(carpma(1, 2, 3, 6, 4))
