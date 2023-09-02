# 1- Çarpim tablosu hazirlayiniz.
# 乘法口诀
for i in range(1, 10):
    for j in range(1, i+1):
        print('{} x {} = {}'.format(j, i, j*i), end='\t')
    print()
# 2- Girilen bir sayinin asal olup olmadiğini kontrol ediniz..
#    Asal Sayi 1 ve kendisi hariç tam böleni olmayan sayilara denir.
# 素数， 素数只能被 1 和 素数本身整除。

sayi = int(input('sayi: '))

asalmi = True

if (sayi == 1):
    asalmi = False

for i in range(2, sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('sayi asaldir.')
else:
    print('sayi asal değildir.')


# 用 f 表达的打印方法
for i in range(10):
    for j in range(1, i+1):
        print(f'{j} x {i} = {j*i}', end='\t')
    print()

'''print函数中自带一个end='\n'''
print(help(print))
# print(*args, sep=' ', end='\n', file=None, flush=False)
