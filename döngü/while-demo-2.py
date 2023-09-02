#    Kullanicidan alacağiniz sinirsiz ürün bilgisini
# urunler listesi içinde saklayiniz.
#    ** ürün sayisini kullaniciya sorun.
#    ** dictionary listesi yapisi (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

i = 0
adet = int(input('kaç adet ürün eklemek istiyorsunuz: '))
urunler = []

while (i < adet):
    urunAdi = input('ürün adi: ')
    fiyat = input('ürün fiyati: ')
    urunler.append({
        'urunAdi': urunAdi,
        'fiyat': fiyat
    })
    i += 1

# for urun in urunler:
#     print(f"ürün adi: {urun['urunAdi']} ürün fiyati: {urun['fiyat']}")

a = 0
while (a < len(urunler)):
    print(f"adi: {urunler[a]['urunAdi']} fiyati: {urunler[a]['fiyat']}")
    # 自己写的时候尽量把名字编辑的短一点，尽量加空格、不然打印出来的数据不好看
    a += 1
