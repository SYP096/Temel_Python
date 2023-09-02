def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        # return func(*args, **kwargs)      # 加上这一行 , 每个函数会执行三次
    return wrapper_do_twice


@do_twice
def hello():
    print("hello")


@do_twice
def greet(msg):
    print("hello " + msg)


@do_twice
def return_greeting(name):
    print("greeting function")
    return f"hello,  {name}"       # 因为每次执行完都会返回到第3 4 行。 所以没有值会返回到第27行


hello()
greet("world")
return_greeting("ali")
print(return_greeting("ali"))     # 如果想要有值返回到在这里。只能在wrapper_do_twice中加上return
