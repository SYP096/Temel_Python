def Not_gir():
    Adi_soyadi = input("sizin ad soyadiniz girin: ")
    Not1 = input("1. Notunuz girin: ")
    Not2 = input("2. Notunuz girin: ")
    Not3 = input("3. Notunuz girin: ")
    with open("Notlar.txt", 'a', encoding='utf-8') as file:
        # 这个'a'模式就是追加数据的、追加到原始文本最后面、如果该路径没有该文件、会创建一个新的空文件然后添加数据
        file.write(Adi_soyadi + ': ' + Not1 + ', ' + Not2 + ', ' + Not3 + '\n')


def Ortalama_oku():
    with open("Notlar.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(hesaplama(satir))
# 这个是老师的写法、但是这样写的话文本最后最多只能留一行空行


'''
def Ortalama_oku():
    with open("Notlar.txt", 'r', encoding='utf-8') as file1:
        for satir in file1.readlines()[:-1]:
            print(hesaplama(satir))
# 11-14是自己写的、和老师写的不太一样、这个只能在文本后面有多个空行时使用
'''


def Not_kayit():
    liste = []
    with open("Notlar.txt", 'r', encoding='utf-8') as file1:
        for i in file1:
            liste.append(hesaplama(i))

        with open("Sonuclar.txt", 'w', encoding='utf-8') as file2:
            for i in liste:
                file2.write(i + '\n')
    with open("Sonuclar.txt", 'r', encoding='utf-8') as file:
        print(file.read())


def hesaplama(satir):
    satir = satir[:-1]    # 本来每一行后面都有一个'\n'、但是这样写的话就不会带上'\n'
    liste = satir.split(':')

    StudentName = liste[0].title()
    notlar = liste[1].split(',')
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    Ortalama = (not1 + not2 + not3)/3

    if Ortalama >= 95 and Ortalama <= 100:
        harf = 'AA'
    elif 90 <= Ortalama <= 94:
        harf = 'BA'
    elif 85 <= Ortalama <= 89:
        harf = 'BB'
    elif 80 <= Ortalama <= 84:
        harf = 'CB'
    elif 75 <= Ortalama <= 79:
        harf = 'CC'
    elif 70 <= Ortalama <= 74:
        harf = 'DC'
    elif 65 <= Ortalama <= 69:
        harf = 'DD'
    elif 60 <= Ortalama <= 64:
        harf = 'FD'
    else:
        harf = 'FF'

    return StudentName + ': ' + harf


while True:
    chioes = input("1-Not gir\n2-Ortamala oku\n3-Not kayit\n4-islem kapat\n")

    if chioes == '1':
        Not_gir()
    elif chioes == '2':
        Ortalama_oku()
    elif chioes == '3':
        Not_kayit()
    else:
        break
