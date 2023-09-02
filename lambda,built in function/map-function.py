# map() 映射函数， map(function, iterables,....) ->map
# input:   function : 映射函数               iterables: 可迭代序列
# output: 输出是一个迭代器对象， 要用到 list() 使其转变为可迭代序列
'''
MAP()是PYTHON内置的高阶函数, 他接收一个函数 F 和一个 LIST ,
并通过函数 F 依次作用在 LIST 的每个元素上, 得到一个新的iterator并返回
'''
sayilar = [1, -2, 5, -7, -9]
str_sayilar = ["1", "2", "5", "7", "9"]
isimler = ["ali", "deniz", "emel", "Çinar"]
kullanicilar = [
    {"ad": "ali",  "soyad": "Yilmaz"},
    {"ad": "ahmet",  "soyad": "Yilmaz"}
]
# kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi ** 2)

# print(kareleri)

# def kareAl(sayi):
#     return sayi ** 2

sonuc = list(map(lambda sayi: sayi ** 2,  sayilar))
sonuc = list(map(int,  str_sayilar))
sonuc = list(map(abs,  sayilar))
sonuc = list(map(float,  sayilar))
sonuc = list(map(len,  isimler))
sonuc = list(map(str.capitalize,  isimler))
sonuc = list(map(str.lower,  isimler))
sonuc = list(map(lambda x: x["ad"],  kullanicilar))

print(sonuc)
