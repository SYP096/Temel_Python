'''
raise 手动增加异常
python 中手动设置异常,  就用 raise
程序发生异常和程序运行错误是两码事儿,  程序运行错误是程序员需要想办法解决的
但有一些程序发生异常是程序正常运行的结果

运行try:  except:  时,   如果召唤了函数,  且在函数中报错了,  会返回到try:  except中,  并且执行except的执行体
因为同样是报错
'''
# print(10 / 0)

# x = 10

# if x > 5:
#     raise ValueError('x 5 den büyük olamaz.')


def colorize(text,  color):
    colors = ("blue", "red", "white", "black", "orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalidir.")    # 到了这里的时候，就是异常，会直接返回38，39行，就类似于return

    if type(color) is not str:
        raise TypeError("renk str tipinde olmalidir.")   # 类似于return, 且会把括号内的值带回去，作为 ex

    if color not in colors:
        raise ValueError("geçersiz bir renk ismi.")

    print(f"{text} {color} olarak yazdirildi.")

# try:
#     colorize("selam", "yellow")
# except Exception as ex:
#     print(ex)


try:
    colorize("selam", "red")
    colorize("selam", "yellow")
except (TypeError, ValueError) as ex:     # 这里也可以直接写Exception,   且ex的值还是上面 raise定义的
    print(ex)
