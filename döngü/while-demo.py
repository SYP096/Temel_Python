sayilar = [4, 6, 9, 10, 35, 57, 89, 125, 244]

# 1: sayilar listesini while ile ekrana yazdirin.

# for i in sayilar:
#     print(i)

# i = 0
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i += 1

# while sayilar:
#     print(sayilar.pop(0))

# print(sayilar)

# 2: Başlangiç ve bitiş değerlerini kullanicidan alip aradaki tüm tek sayilari
# ekrana yazdirin.

# baslangic = int(input('başlangiç: '))
# bitis = int(input('bitiş: '))

# i = baslangic

# while i < bitis:
#     i += 1
#     if (i%2==1):
#         print(i)


# 3: 1-100 arasindaki sayilari azalan şekilde yazdirin.

# i = 100

# while (i>0):
#     print(i)
#     i -= 1

# 4: Kullanicidan alacağiniz 5 sayiyi ekranda sirali bir şekilde yazdirin.

sayilar = []
i = 0
while (i < 5):
    sayi = int(input('sayi: '))
    sayilar.append(sayi)
    i += 1

sayilar.sort()
print(sayilar)
