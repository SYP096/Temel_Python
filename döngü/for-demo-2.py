urunler = [
    {'name': 'iphone 8', 'price': '4000'},
    {'name': 'iphone 8 Plus', 'price': '5000'},
    {'name': 'iphone X', 'price': '6000'},
    {'name': ' iphone XR', 'price': '7000'},
    {'name': 'iphone 11', 'price': '8000'},
    {'name': 'samsung s10', 'price': '6000'},
]

# 1- Tüm ürün bilgilerini listeleyiniz.

# for urun in urunler:
#     print(f"ürün adi: {urun['name']} ve ürün fiyati: {urun['price']} TL")

# 2- Ürünlerin fiyatlari toplami nedir ?

# toplam = 0
# for urun in urunler:
#     toplam = toplam + int(urun['price'])
# print(f'ürün toplamlari: {toplam} TL')
print(sum([int(i['price']) for i in urunler]))   # Ürünlerin fiyatlari toplami

# 3- Ürünlerden fiyati en fazla 6000 olan ürünleri gösteriniz ?
# for urun in urunler:
#     if (int(urun['price']) <= 6000):
#         print(f"ürün adi: {urun['name']} ürün fiyati: {urun['price']}")
print(list(filter(lambda a: int(a['price']) <= 6000, urunler)))     # 这个只是筛选
print(list(map(lambda a: a["name"],
               filter(lambda a: int(a['price']) <= 6000, urunler))))
# 这个是显示价格低于6000的产品名字

# 4- Kullanicidan alinan anahtar kelimeyi içeren ürünleri bulunuz.

kelime = input('aramak istediğiniz ürün: ')

for urun in urunler:
    if (urun['name'].find(kelime.lower()) > -1):
        print(f"ürün adi: {urun['name']} ürün fiyati: {urun['price']}")
# 这个代码时判断用户输入的关键字所有关的产品是否存在 , 并且输出
