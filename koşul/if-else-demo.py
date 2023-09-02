# 1- Girilen bir sayinin 50-100 arasinda olup olmadiğini kontrol ediniz.

# sayi = int(input('sayi: '))
# if  (sayi > 50) and (sayi<=100):
#     print(f"{sayi}, 50 ile 100 arasindadir.")
# else:
#     print(f"{sayi}, 50 ile 100 arasinda değildir.")


# 2- Girilen bir sayinin pozitif tek sayi olup olmadiğini kontrol ediniz.

# sayi = int(input('sayi: '))
# if (sayi > 0):
#     if (sayi % 2 == 1):
#         print('girilen sayi pozitif tek sayidir.')
#     else:
#         print('sayi pozitif ancak tek değil.')
# else:
#     print('girilen sayi negatif.')


# 3- Username ve parola bilgileri ile giriş kontrolü yapiniz.
# _username = "sadikturan"
# _password = "1234"

# girilenUsername = input('username: ')
# girilenPassword = input('parola: ')

# if (girilenUsername.strip() == _username) and
# (girilenPassword.strip() == _password):
#     print('girilen username ve parola doğru')
# else:
#     print('girilen bilgiler yanliş')


# 4- Girilen 3 sayiyi büyüklük olarak karşilaştiriniz.

# x = int(input('x: '))
# y = int(input('y: '))
# z = int(input('z: '))

# if (x>y) and (x>z):
#     print("x en büyük sayi: ")
# elif (y>x) and (y>z):
#     print("y en büyük sayi: ")
# elif (z>x) and (z>y):
#     print("z en büyük sayi: ")


# 5- Kullanicidan 2 vize (%60) ve final (%40) notunu alip
# ortalama hesaplayiniz.
#    a-) Eğer ortalama 50 ve üstündeyse geçti değilse kaldi yazdirin.
#    b-) Ortamalama 50 olsa bile final notu en az 50 olmalidir.
#    c-) Finalden 70 alindiğinda ortalamanin önemi olmasin.

# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final: '))

# ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)
# sonuc = ortalama>=50
# sonuc = (ortalama >= 50) and (final>=50)
# sonuc = (ortalama >= 50) or (final>=70)

# durum 1
# if(ortalama>=50):
#     print(f"öğrencini not ortalamasi: {ortalama} ve sinifi geçti")
# else:
#     print(f"öğrencini not ortalamasi: {ortalama} ve kaldi.")

# durum 2
# if (ortalama>=50):
#     if(final>=50):
#         print(f'öğrencinin not ortalamasi: {ortalama} ve öğrenci geçti.')
#     else:
#         print(f'öğrencinin not ortalamasi: {ortalama} ve öğrenci kaldi.
# Finalden en az 50 almalidir.')
# else:
#     print(f'öğrencinin not ortalamasi: {ortalama} ve öğrenci kaldi.')

# durum 3
# if(ortalama>=50):
#     print(f'öğrencinin not ortalamasi: {ortalama} ve öğrenci geçti.')
# else:
#     if (final>=70):
#         print(f'öğrencinin not ortalamasi: {ortalama} ve öğrenci başarili
# çünkü finalden 70 üstü aldi.')
#     else:
#         print(f'öğrencinin not ortalamasi: {ortalama} ve öğrenci kaldi.')

# 6- Kişinin ad, kilo ve boy bilgilerini alip kilo indekslerini hesaplayiniz.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağidaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayif
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input('adiniz: ')
kg = float(input('kilonuz(kilogram): '))
hg = float(input('boyunuz(metre): '))

kiloIndeks = kg / (hg ** 2)

if (kiloIndeks >= 0) and (kiloIndeks <= 18.4):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen zayif.")
elif (kiloIndeks > 18.4) and (kiloIndeks <= 24.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen normal.")
elif (kiloIndeks > 24.9) and (kiloIndeks <= 29.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen kilolu.")
elif (kiloIndeks >= 29.9) and (kiloIndeks <= 34.9):
    print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo değerlendirmen obez.")
else:
    print('bilgileriniz yanliş.')
