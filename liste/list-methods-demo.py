isimler = ['Ada', 'Yiğit', 'Hasan', 'Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")
'''isimler.insert(len(isimler), "Cenk")   和上面同一个结果'''
# 2-  "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0, "Sena")

# 3-  "Yiğit" ismini listeden siliniz.
# 4-  "Yiğit" isminin indeksi nedir ?
sonuc = isimler.index("Yiğit")
print(sonuc)
# 5-  "Beril" listenin bir elemanı mıdır ?
for a in isimler:                  # count = "Beril" in isimler
    if a == "Beril":               # print(count)      True: 在内， False: 不在内
        print(True)                # 用 if in ， 或者直接用in
        break
else:
    print("Beril is not in list isimler")
# 6-  Liste elemanlarını ters çevirin.
isimler.reverse()
# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
sonuc = sorted(isimler, reverse=True)    # 形成一个新的列表， reverse=True使其变成相反的
isimler.sort()        # 在原列表的基础上排序

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort()

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
s = "IPhone X,IPhone XR"
ss = s.split(',')
print(ss)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
max = max(yaslar)
min = min(yaslar)
print(max, min)
# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
marka1 = input("请输入一个品牌名字:")
marka2 = input("请输入一个品牌名字")
marka3 = input("请输入一个品牌名字")
markalar = []
markalar.append(marka1)
markalar.append(marka2)
markalar.append(marka3)
print(markalar)
print(sonuc)
print(isimler)
print(yaslar)
