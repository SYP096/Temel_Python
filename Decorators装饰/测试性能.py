import time
import sys
'''测量代码性能的时候用 time.perf_counter '''


def spped_test(count):
    def sed_test(func):
        def ana_test(*args, **kwargs):      # 此时虽然不用导入任何参数, 但是最好这样写 , 因为指不定什么时候会需要导入参数
            print(f"现在执行的是{func.__name__}")
            for _ in range(count):
                start_time = time.perf_counter()                         # perf_counter 的意思就是 性能计数器
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                loading_time = end_time - start_time
                print(f"运行时间为{loading_time * 1000} ms")
            return result
        return ana_test
    return sed_test


@spped_test(count=3)
def test_list():
    return sum([i for i in range(1000000)])


@spped_test(count=3)
def test_generator():
    return sum((i for i in range(1000000)))


@spped_test(count=3)
def test_iterator():
    aa = [i for i in range(1000000)]
    return sum(iter(aa))


print(test_list())
print(test_generator())
print(test_iterator())

print("------------------------以下是文件大小-------------------------")
liste = [i for i in range(1000000)]
print(sys.getsizeof(liste))              # 8448728
iterator = iter(liste)
print(sys.getsizeof(iterator))        # 48
generator = (i for i in range(1000000))
print(sys.getsizeof(generator))     # 200

'''
time.time() 和 time.perf_counter() 在 Python 中都是用于获取时间的函数 , 但它们的实现方式和返回值有所不同。

time.time() 函数返回自 Unix 纪元(1970 年 1 月 1 日 00:00:00 UTC)以来的秒数 , 是一个浮点数 , 通常用于测量时间间隔。
它的返回值精度是秒级别的 , 精度可能不足以用于测量很短的时间间隔。
------------------------------------------------------------------------------------------------------------------

time.perf_counter() 函数返回一个 CPU 计时器的值 , 通常是一个高精度的小数。
它适合于测量代码的性能 , 特别是在短时间内运行的代码。
在同一台计算机上运行 , 多次调用 perf_counter() 函数会返回不同的值 , 这可以用于测量时间间隔的精确性。


因此 , time.time() 和 time.perf_counter() 用途不同 , 需要根据具体的使用场景进行选择。
'''
