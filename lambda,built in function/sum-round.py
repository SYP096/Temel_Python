sayilar = [34, 2, 5, 7, 98]

sonuc = sum(sayilar)
sonuc = sum(sayilar,  10)
print(sonuc)        # sayilarin toplami + 10       4行

urunler = [
    {"title": "iphone x",  "price": 5000},
    {"title": "iphone xr",  "price": 6000},
    {"title": "iphone 11",  "price": 7000},
    {"title": "iphone 11 Pro",  "price": 0},
]

# toplamFiyat = sum([urun["price"] for urun in urunler])
# sonuc = toplamFiyat / len(urunler)

toplamFiyat = sum([urun["price"] for urun in urunler])
urunAdeti = len([urun for urun in urunler if urun["price"] > 0])
urunAdeti = len(list(filter(lambda urun: urun["price"] > 0, urunler)))  # 同18
print(urunAdeti)
sonuc = toplamFiyat / urunAdeti

sonuc = round(10.2)
print(sonuc)
sonuc = round(10.6)
print(sonuc)

sonuc = round(10.50)     # 10
print(sonuc)
sonuc = round(1.424242, 2)
print(sonuc)
sonuc = round(1.426242, 2)
sonuc = round(1.426242, 4)
print(sonuc)
sonuc = round(3.5555555, 3)
print(sonuc)

sonuc = abs(-21)      # 取绝对值
print(sonuc)
print(round(9.5))        # 10       round 四舍五入   但是如果小数点前一位是0的话    五舍六入
print(round(111000.5))        # 111000
print(round(1000.51))      # 1001
# round正常情况下四舍五入、但是只有在小数点前一位是0、且小数点之后只有一个5或50..的时候才会五舍六入
# 但是、小数点前一位是0、小数点后是51、52、53、、59、、51111、5222等等的数字时、也是秉承这四舍五入
