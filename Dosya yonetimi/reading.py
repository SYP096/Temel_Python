# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.
# "r": okuma modu => belirtilen konumda dosya olmalıdır.
import os
f = os.path.exists("msg.txt")
f = os.path.abspath("msg.txt")
print(f)
f = open("E:\\my_project\\Udemy课件\\msg.txt")
# 尽量用绝对路径、相对路径你容易找不到文件
print(f)
# print(help(f))
print(f.read())
