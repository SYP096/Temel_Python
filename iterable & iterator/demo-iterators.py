import time
import sys


class Counter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


print(type(Counter(10, 20)))     # <class '__main__.Counter'>
# for i in Counter(10, 20):
#     print(i)

iterator = iter(Counter(20, 30))
print(type(iterator))     # <class '__main__.Counter'>

# for i in iterator:        # 可以用 for 遍历 迭代器对象
#     print(i)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break


liste = [i*2 for i in range(10000)]       # 列表生成式
print(sys.getsizeof(liste))      # 85176

iterator = iter(liste)     # 用 iter() 是列表传换成迭代器对象
print(sys.getsizeof(iterator))       # 48      可以看出迭代器对象占用内存更少, 甚至比生成器都要少很多

sss = [i**2 for i in range(100000000)]

list_start_time = time.time()
sum(sss)
list_stop = time.time() - list_start_time

a = iter(sss)
gen_start_time = time.time()
sum(a)
gen_stop = time.time() - gen_start_time

print(list_stop, gen_stop)
# 1.920884132385254 1.719550371170044可以看到迭代器对象用的时间更少
