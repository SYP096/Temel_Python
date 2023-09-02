from termcolor import colored

# sonuc = dir(termcolor)
# sonuc = help(termcolor)
sonuc = colored("Merhaba", color="green", on_color="on_yellow")
sonuc = colored("Merhaba", color="green", on_color="on_yellow", attrs=["bold"])
'''color 指的是字体的颜色,  on_color 指的是背景颜色, attrs是属性,  bold就是加粗了 '''
print(sonuc)
