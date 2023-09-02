import time


def speed_test(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"{fn.__name__} metodu çalişiyor...")
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"geçen süre: {run_time}")
        return result
    return wrapper


@speed_test     # 这里也可以像文件decorator_args中的写法, 给修饰器一个参数
def sum_gen():
    return sum((x for x in range(10000000)))


@speed_test
def sum_list():
    return sum([x for x in range(10000000)])


print(sum_gen())
print(sum_list())
