# open(dosya_adi,dosya_erişim_modu)
# dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "r": (Read) okuma. Dosya konumda yoksa hata verir.
# "w": (Write) yazma modu.
#    ** Dosyayı konumda oluşturur.
#    ** Dosya içeriğini siler ve yeniden ekleme yapar.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
#       file.seek()在'a'模式下用不了 、 在'r+'模式下能用
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.

# with open("msg.txt","a") as file:
#     file.write("dördüncü satır\n")
#     file.write("beşinci satır\n")

with open("msg.txt", "r+") as file:
    file.read()    # 从头读到尾
    file.write("yeni satir")
