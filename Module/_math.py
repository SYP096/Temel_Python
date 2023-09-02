# Yöntem 1
# import math
# import math as islem

# value = dir(math)       这个是列举该模块中所有函数
# value = help(math)   这个是帮助了解该模块中的所有函数
# value = help(math.factorial)      这个是帮助了解该模块中的指定函数
# value = math.sqrt(49)     # sqrt 平方根
# value = math.factorial(5)    # 5！
# value = math.floor(5.9)     # 向下取整        floor 地板
# value = math.ceil(5.9)       # 向上取整        ceil 天花板

# value = islem.factorial(5)      # 根据第三行

# Yöntem 2
# from math import *


def sqrt(x):
    print('x :' + str(x))


from math import factorial, sqrt, ceil

value = factorial(5)
value = sqrt(9)        # 这个时候sqrt会指向23行，因为23行时距离这行最近的函数
value = ceil(9.8)

print(value)
