import os
# import datetime

result = dir(os)
result = os.name

# dizin değiştirme
# os.chdir('C:\\')                    # 切换路径
# os.chdir('..')                        # 回到上一个文件夹
# os.chdir('../..')                     # 回到上上一个文件夹

'''------------------------klasör oluşturma--------------------------'''
# os.mkdir("newdirectory")                             # 创建目录， 创建文件夹
# os.makedirs("newdirectory/yeniklasör")      # 在new文件夹中再创建一个新的文件夹yenilik
# os.rename("newdirectory","yeniklasör")      # 重命名， 将new文件夹的名字改为yenik
# os.rmdir("newdirectory")                            # 删除该文件
# os.removedirs("yeniklasör/yeniklasör")      # 删除该文件

'''------------------------listeleme------------------------'''
result = os.listdir()                         # 使本文件夹的文件夹或文件整合为列表并输出
print(result)                          # ['demo-module.zip', 'math.py', '_datetime.py', '_os.py', '_random.py']
result = os.listdir('E:\\my_project')                 # 使E:\\my_project文件夹中的文件夹或文件整合为列表并输出
print(result)
# for dosya in os.listdir():
#     if dosya.endswith('.py'):             # 只输出以 .py 结尾的文件
#         print(dosya)


# etkin dizin öğrenme                # 获取当前工作路径
# result = os.getcwd()


result = os.stat("Module")         # 获取该文件的相关信息
print(result)
# result = result.st_size                  # 查看该对象的尺寸
'''以下的三行， 每次只能操作一行'''
# result = datetime.datetime.fromtimestamp(result.st_ctime)            # 创建文件的时间          st_ctime
# result = datetime.datetime.fromtimestamp(result.st_atime)            # 最后使用时间             st_atime
# result = datetime.datetime.fromtimestamp(result.st_mtime)           # 最后一次改变的时间          st_mtime
# print(result)
'''-----------------------------------------------------------------------------'''
# os.system("notepad.exe")               # 打开记事本

# result = datetime.datetime.fromtimestamp(result.st_ctime)          # oluşturulma tarihi        st_ctime
# result = datetime.datetime.fromtimestamp(result.st_atime)         # son erişilme tarihi         st_atime
# result = datetime.datetime.fromtimestamp(result.st_mtime)       # değiştirilme tarihi          st_mtime
# path

# result = os.path.isfile("_os.py")         # 判断是否是文件
# print(result)
result = os.path.abspath("_os.py")     # 获取绝对路径
print(result)                 # E:\my_project\Udemy课件\_os.py
'''从绝对路径转变为文件路径时， 一定要记得把 '\\' 换成'/'   不换的话肯定报错， 而且还不能是单个'\' , 必须是'\\' '''
# result = os.path.dirname("E:/my_project/Udemy课件/Module/_os.py")           # 获取路径名称       注意必须是  /
result = os.path.dirname(os.path.abspath("_os.py").replace('\\', '/'))           # 这个相等于49， 54    记得 \\ 要换成 /
result = os.path.dirname(os.path.abspath("_os.py"))              # 也可以直接这样写， 必要时要加上replace
result = os.path.exists("E:/my_project/Udemy课件/Module/_os.py")         # 判断是否有该文件， 必须要把'\' 改为 '/'
result = os.path.exists(os.path.abspath("_os.py"))                 # 类似于以上步骤，但没必要这样写
# result = os.path.exists("")
result = os.path.isdir("E:/my_project/Udemy课件/Module")         # ’\‘   ->'/'     判断是否是文件夹(目录)
result = os.path.isfile("E:/my_project/Udemy课件/Module/_os.py")          # ’\‘   ->'/'     判断是否是文件
result = os.path.join("E:\\", "11111", "22222")         # 这个是连接文件和文件名， 但不代表创建文件
print(result)     # E:\11111\22222
result = os.path.split("e:\\deneme")                     # 分割文件名和目录， 输出为元组
print(result)   # ('e:\\', 'deneme'
result = os.path.splitext("_os.py")                         # 分离文件名和扩展名， 输出位元组
print(result)           # ("_os", ".py")
# result = result[0]
result = result[1]
result = os.path.getatime("function")          # 输出为秒 ，还是要用到datetime.datetime.fromtimestamp()
# 33 和 70行 只能输入文件夹参数、 py文件不行

print(result)

'''
可以看CSDN上的收藏夹
输出的时候是 \
但是在运用到函数的时候必须要把'\' 转换成'/ '      否则就会报错
记得用到replace的时候 , 必须是".replace('\\ ', '/')" , 必须是双斜杠， 否则也会报错
'''
