import datetime
'''这里的每一个题都应该好好看'''

isimler = ["Ahmet", "ali", "Çinar", "DeNiz"]
string = "Hello 123456 World."
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20, 5, 15, -2, 0, -6]

# 1-"1-100"arasındaki sayılardan 12' e tam bölünebilen sayı listesi oluşturunuz
sonuc = [i for i in range(1, 101) if i % 12 == 0]
# 或者， if i % 3 ==0 if i % 4 == 0

# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdınız.
sonuc = [isim.lower() for isim in isimler[::-1]]
print(sonuc)       # ['deniz', 'çinar', 'ali', 'ahmet']
sonuc = [isim.lower()[::-1] for isim in isimler]
print(sonuc)        # ['temha', 'ila', 'raniç', 'zined']
''' 第二题中, isim 是字符串, 想要反着输入, 必须是isimler[::-1], 这样的话, 就可以反过来输出所有元素了'''
# 或者，  sonuc = [isim.lower()[::-1] for isim in isimler]
# 3- verilen "string" içindeki rakamları içeren bir liste oluşturunuz.
sonuc = [i for i in string if i.isdigit()]   # 别忘了带括号
# ['1', '2', '3', '4', '5', '6']
# 4- "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste
# oluşturunuz.
now = datetime.datetime.now().year       # 表示现在的年份
sonuc = [now - old for old in yillar]
# 5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre
# eksi değer için buzlanma tehlikesi yazdırınız.
sonuc = [i if i >= 0 else "buzlanma tehlikesi" for i in dereceler]
'''如果是 if else 就必须在 for 之前， 而且不能带 print()'''
print(sonuc)

now = datetime.datetime.now().year
print(type(now), now)
sonuc = [now - old for old in yillar]
print(sonuc)
