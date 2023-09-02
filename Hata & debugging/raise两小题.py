'''这个文件是自己做的raise-demo'''
# 1- Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajlari verin.
# 5！= 5*4*3*2*1
deneme_lis = [0, 5, 6, 'a', 3, 0, -4, '10a', 8, -3]


def fac(num):
    num = int(num)
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError('faktoriyel icin sayilar negatif olmaz')
    n = 1
    for i in range(1, num + 1):
        n *= i
    return n


for x in deneme_lis:
    try:
        num = (fac(x))
    except ValueError as e:
        print(e)
    else:
        print(num)
print('\n---------------------------第二题----------------------------\n')
# 2- Girilen parola içinde türkçe karakter hatası veriniz.
'''我这个解法,  是带这密码是否正确,  且只有三次机会'''
turkalpha = "İşçöüğı"
password = "123456789"


def palorajudge(palora):
    for i in palora:
        if i in turkalpha:
            raise ValueError("you cannot enter turrk alphabe as password")
    if palora == password:
        print("Your password is True")
    elif palora != password:
        print("Your password is False")


for i in range(3):
    palora = input("pleace enter your password:")
    try:
        x = palorajudge(palora)

    except ValueError as e:
        print(e)
