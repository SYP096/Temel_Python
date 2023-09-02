import random
# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yaziniz.
# 答案


def tekrar(kelime, adet):
    print(kelime * adet)


tekrar('大傻逼\n', 18)

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yaziniz.
# 答案


def hesap(*lines):          # 把实参传输到这里的时候, 就会自动形成元组, 然后传递到函数内的函数体
    print(type(lines), '\n', lines)
    alan = lines[0] * lines[1]
    cevre = 2 * (lines[0] + lines[1])
    return f"alan: {alan}, cevre: {cevre}"


print(hesap(3, 4))

# 3- Yazi tura uygulamasini fonksiyon kullanarak yapiniz.(Random modülü) yazi tura 就是指硬币的正反面


# 答案


def yaziTura(times):
    yazisayi = 0
    turasayi = 0
    for _ in range(times):          # 也可以用 while times >0:      times -= 1
        num = random.random()
        if num > 0.5:
            print('Yazi')
            yazisayi += 1
        elif num < 0.5:
            print('Tura')
            turasayi += 1
    print(f'yazisayi: {yazisayi}, turasayi: {turasayi}')


yaziTura(10)


# 4- Kendisine gönderilen 2 sayi arasindaki tüm asal sayilari bulan fonksiyonu yaziniz.
# 判断两个数字之间有哪些素数


def asalSayi(a, b):
    for i in range(a, b+1):
        if i > 1:
            for j in range(2, i):       # 这个除数的范围必须是 2 到 (被除数-1)
                if i % j == 0:
                    break
            else:                       # else 要在for后面, 只有for循环顺利的完全结束了, 才会执行else
                print(i, end='\t')               # 但如果,  遇到了可以整除的数字,  就会执行break,  else 则不会执行,  因为break之后没有判定True 或 Flase


asalSayi(10, 100)
print()
# 5- Kendisine gönderilen bir sayinin tam bölenlerini bir liste şeklinde döndüren fonksiyonu yaziniz.
'''tam bölenleri 也就是整除数'''


def number(sayi):
    sayilar = []
    for i in range(2, sayi):
        if sayi % i == 0:
            sayilar.append(i)
        else:
            continue
    return sayilar


num_lis = number(66)
print(num_lis)
