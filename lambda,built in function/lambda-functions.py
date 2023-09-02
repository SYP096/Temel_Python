# lambda 是一个轻量级的函数，lambda arguments： expression
# 参数可以是一个也可以是多个， 但是表达式就只能是一个
# lambda 同样适用 *args, **kwargs   , *args 的时候，输出为元组
""" def 函数内部， map(), filtre() 内不需要加括号， 单独使用lambda的时候要加括号"""
sonuc = (lambda a: a ** 2)(3)    # 这个直接就是把 3 代入到 a 了
multiply = (lambda a: a ** 2)
sonuc = multiply(5)


toplama = (lambda a, b, c: a+b+c)    # 这个时候toplama就成了函数名、可以用其调用lamda函数
sonuc = toplama(1, 4, 7)


tersCevir = (lambda s: s[::-1])
sonuc = tersCevir("Sadik")


def my_func(n):
    return lambda a: a * n


multiply2 = my_func(2)
multiply3 = my_func(3)

sonuc = multiply2(10)
print(sonuc)
sonuc = multiply2(20)
print(sonuc)
sonuc = multiply3(10)      # 同等于 demo = (lambda a: a** 3), 这样输入必须加括号
tersCevir = (lambda s: s[::-1])("Sadik")
print(tersCevir)
print(sonuc)
