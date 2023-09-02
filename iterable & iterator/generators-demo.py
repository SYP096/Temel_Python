import time
import sys

# (1 - ∞) aralığındaki her sayının karesini getiren fonksiyon.
# Fibonacci serisini hem normal fonksiyon hem de generator fonksiyon ile oluşturun.
# Performans testlerini yapın.

# def sonsuz_sayi_uret():
#     sayi = 0
#     while True:
#         yield sayi
#         sayi += 1

# generator = sonsuz_sayi_uret()

# print(next(generator))
# print(next(generator))
# print(next(generator))

# for i in generator:
#     print(i)

'''用while循环创建斐波那契数列'''
# def fib_list(max):
#     sayilar = []

#     a, b = 0, 1
#     while len(sayilar) < max:
#         sayilar.append(a)
#         a, b = b, a+b
#     return sayilar

# # print(fib_list(10000))


def fib_gen(max):
    '''用生成器创建斐波那契数列'''
    a, b = 0, 1
    count = 0
    while count < max:
        yield a             # 必须用到 yield
        a, b = b, a+b
        count += 1


print(list(fib_gen(10)))     # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
for i in fib_gen(10):       # 只有在循环的时候yield才会像return一样遇到了就返回
    print(i)

liste = [i*2 for i in range(10000)]       # 列表生成式
print(sys.getsizeof(liste))      # 85176

gen = (i**2 for i in range(10000))     # 生成器生成式
print(sys.getsizeof(gen))       # 208      可以看出生成器更加的轻巧 , 占用内存更少

list_start_time = time.time()
sum([i**2 for i in range(50000000)])
list_stop = time.time() - list_start_time

gen_start_time = time.time()
sum((i**2 for i in range(50000000)))
gen_stop = time.time() - gen_start_time

print(list_stop, gen_stop)      # 4.357099533081055 3.0721724033355713 可以看到生成器用的时间更少
