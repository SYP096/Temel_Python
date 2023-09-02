from functools import wraps
'''这个wraps可以保存原始函数的元数据 , 在这里就是保存了 函数add 的元数据 , 使其不会被替代为wrapper'''


def log_data(fn):
    @wraps(fn)        # 使原始函数add保留其元数据, 如果没有这个代码可以看到23，24 打印的是wrapper的数据
    def wrapper(*args, **kwargs):
        """wrapper hakkinda bilgilendir"""
        print(f"çağirdiğiniz metot ismi: {fn.__name__}")       # 特殊函数,打印函数名字
        print(f"metot bilgisi: {fn.__doc__}")           # 特殊函数 , 打印注释
        return fn(*args, **kwargs)
    return wrapper


@log_data
def add(x, y):
    """fonksiyona gönderilen 2 sayiyi toplar."""
    return x+y


aa = add(10, 20)
print(add(10, 20))
print(add.__name__)       # 如果在函数wrapper上一行修饰了@wraps(fn) , add就不会变 , 还会是原本的元数据
print(add.__doc__)          # 如果没有修饰 , add 就会被wrapper替代
