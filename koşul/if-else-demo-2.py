# Bir aracin yakit tipine göre (benzin,dizel) belirtilen bir mesafede
# ne kadar yakit masrafi olduğunu
# hesaplayan uygulamayi yapiniz.

benzinFiyat = 6.69
dizelFiyat = 5.86
toplamYakitUcreti = 0

ortalamaYakitTuketimi = float(input('100 km deki ortalama yakit tüketimi: '))
gidilecekYol = float(input('gidilecek yol kaç km: '))
yakitTipi = input('yakit tipiniz nedir: ')

toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

if (yakitTipi == "benzin"):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif (yakitTipi == "dizel"):
    toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
else:
    print('yanliş yakit tipi girdiniz.')

if (toplamYakitUcreti != 0):
    print(toplamYakitUcreti)
