def selamlama(fn):
    def wrapper(ad):
        print("hoş geldiniz.")
        fn(ad)
        print("görüşmek üzere.")
    return wrapper        # 使新函数wrapper返回原始函数 。函数是可以被当作值或者对象的 , 所以可以被当做值返回原始函数


@selamlama   # 修饰器就是将函数(gunaydin)作为参数传到修饰器函数(selamlama) , 并返回其内部函数(wrapper)。固定搭配return
def gunaydin(ad):
    print("günaydin benim adim " + ad)


@selamlama
def iyigunler(ad):
    print("iyi günler benim adim " + ad)


gunaydin("ahmet")
iyigunler("yağmur")

'''
当你在使用Python语言编写函数时 , 经常会需要给函数添加一些额外的功能或者逻辑 ,
比如对函数的输入和输出进行验证、记录函数的调用日志等等。
Decorator(装饰器)是Python中用于装饰函数的一种特殊语法。它可以让你在不修改函数代码的前提下 , 给函数添加新的功能。

简单来说 , Decorator是一个Python函数或者类 , 它可以接受一个函数作为参数 , 然后返回一个新的函数。
这个新的函数通常会在原来的函数执行前或者执行后 , 添加一些额外的逻辑。'''
