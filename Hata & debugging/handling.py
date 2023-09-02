# 只要执行了except，就会结束整个循环
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except (ZeroDivisionError, ValueError) as e:      # 括号是必须要有的，括号里面可以有多个Error
        print('hata oluştu.')
        print(e)
    except Exception as e:             # 也可以直接写Exception as e
        print('bilinmeyen bir hata oluştu.')
        print(e)
    else:            # else 如果try没有报错就执行else， 报错执行except
        break
    finally:      # finally 是 不管报不报错都执行
        print('finally bloğu çalişti.')
