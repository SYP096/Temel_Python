# 列表表达式
liste = [10, 4, 7, 9, 70]

sayilar = []

for i in liste:
    i *= 2
    sayilar.append(i)

# [expression for item in list]
# sayilar = [i*i for i in range(10)]
# sayilar = [i*2 for i in liste]

isim = "Ahmet"
isimler = ["Ahmet", "ali", "Çinar", "DeNiz"]

sonuc = [c.upper() for c in isim]
print(sonuc)
sonuc = [str(sayi) for sayi in liste]
print(sonuc)
sonuc = [i.lower() for i in isimler]

print(sonuc)
