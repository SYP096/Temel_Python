'''
all(iterables)       iterable里面都是True的时候, 返回True,  若列表为空, 返回True
any(iterables)     iterable里面只要有一个True, 就会返回True,  若列表为空, 返回Flase

这两个函数只对 True 和 Flase 会作出判断。。。bool(x), 比较运算符
'''
sonuc = all([True, True, False])    # Flase
sonuc = all([True, True, True])      # True
sonuc = any([True, False, False])     # True

# And => True & True => True => All()
# Or  => True | False => True => Any()

sayilar = [0, 1, 3, 6, 8, 9, 10]

sonuc = any([bool(sayi) for sayi in sayilar])
print(sonuc)
sonuc = all([bool(sayi) for sayi in sayilar])
print(sonuc)
sonuc = all([bool(sayi) for sayi in sayilar if sayi % 2 == 1])
print(sonuc)
sonuc = all([sayi % 2 == 0 for sayi in sayilar])
print(sonuc)
sonuc = any([sayi % 2 == 0 for sayi in sayilar])
print(sonuc)

kisiler = ["ali", "ahmet", "çinar"]

sonuc = any([kisi[0] == 'a' for kisi in kisiler])
print(sonuc)
sonuc = all([kisi[0] == 'a' for kisi in kisiler if kisi[0] == 'a'])
print(sonuc)
sonuc = any(map(lambda kisi: kisi[0] == "a", kisiler))       # 同 29
sonuc = all(filter(lambda kisi: kisi == "a", kisiler))             # 同 31
print(sonuc)
