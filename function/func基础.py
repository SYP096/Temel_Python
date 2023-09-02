def selamla(isim):
    return "Merhaba, " + isim


sonuc = selamla("Sadik")
sonuc = selamla("Yağmur")


def toplam(a, b):
    return a + b


sonuc = toplam(10, 20)
sonuc = toplam(20, 30)


def yasHesapla(dogumYili):
    return 2021 - dogumYili


sonuc = yasHesapla(1983)
sonuc = yasHesapla(1993)


def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)         # 函数里面可可以召唤其他函数, 也可以召唤本函数
    kalanSure = 65 - yas
    if kalanSure > 0:
        print(f"{isim}, emekliliğinize {kalanSure} yil kaldi.")
    else:
        print(f"{isim}, zaten {abs(kalanSure)} yil önce emekli oldunuz.")


emekliligeKacYilKaldi(1983, "Sadik")
emekliligeKacYilKaldi(1950, "Ali")


def now():
    import datetime           # 函数里面当然也可以导入另一个函数 import
    return datetime.datetime.now().year


print(now())
