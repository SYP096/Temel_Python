# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
#  hata mesajları verin.

def faktoriyel(x):
    x = int(x)
    if (x < 0):
        raise ValueError("Negatif değer")      # 这个括号内的数据会直接影响下面ValueError的信息:                                                                                

    sonuc = 1
    for i in range(1, x + 1):
        sonuc *= i

    return sonuc


for i in [5, 7, 'a', 2, -4, '10a']:
    try:
        x = faktoriyel(i)     # 召唤函数之后如果在函数内部报错， 也会返回这里然后进入到except
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)

# 2- Girilen parola içinde türkçe karakter hatası veriniz.


def parolaKontrol(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez.")

    print('geçerli parola')


parola = input('parola: ')

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)

