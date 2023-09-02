def dec_do_twice(count):
    def do_twice(func):
        def wrapper_do_twice(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
        return wrapper_do_twice
    return do_twice


@dec_do_twice(count=2)      # 也可以利用装饰器导入参数 , 返回do_twice . 此时修饰器指向do_twice
def hello():               # 回到修饰器(10) , 然后进入函数do_twicw并且返回wrapper_do_twice. 此时函数hello被替代为wrapper_do_twice
    print("hello")


@dec_do_twice(count=5)
def greet(name):
    print("hello " + name)


hello()
greet("ali")
