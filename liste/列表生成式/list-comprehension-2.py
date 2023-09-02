# for item in liste:
#     if (koşul):
#         expression

'''[expression for item in liste if koşul]'''

sayilar = [1, 5, 8, 11, 15, 44]
sonuc = []

for sayi in sayilar:
    if (sayi % 2 == 0):
        sonuc.append(sayi)

sonuc = [sayi for sayi in sayilar if sayi % 2 == 0]
# if else 在 for 的前或后没有任何区别
sonuc = [sayi if sayi % 2 == 0 else "tek sayi" for sayi in sayilar]
''' if 的判断为 True 才会执行执行体， for 也是， Ture才会执行循环体, 所以有一个是Ture 就会两个一起执行'''
fiyatlar = [1000, 3000, 5000, 0, 4000]
vergiler = []

for fiyat in fiyatlar:
    if (fiyat > 0):
        vergiler.append(fiyat*1.18)

vergiler = [fiyat*1.18 for fiyat in fiyatlar if fiyat > 0]
vergiler = [fiyat*1.18 if fiyat > 0 else "vergi hesaplanmadi"
            for fiyat in fiyatlar]

sonuc = []
for x in range(3):
    for y in range(3):
        sonuc.append((x, y))
''' 下面这个很重要'''
sonuc = [(x, y, z, m) for x in range(2)
         for y in range(2) for z in range(2) for m in range(2)]
# 也可以是多个for来执行

print(sonuc)
