# "w": (Write) yazma modu.
#    ** Dosyayi konumda oluşturur.
#    ** Eğer konumda ayni dosya varsa dosyayi siler ve yeni oluşturur.
with open("newfile.txt", "w", encoding="UTF-8") as file:
    # 用 "w" 的时候、如果没有该文件、就会在控制台创建一个该空文件
    # 以后打开文件的时候你一定要用到 endcoding='utf-8' 因为不用的话土耳其语识别不了
    file.write("Çinar Turan\n")
    file.write("Sadik Turan\n")
    file.write("Sena Turan\n")
    file.write("用'w'的时候、如果没有该文件、就会在控制台创建一个该空文件\n")
    file.write("以后打开文件的时候你一定要用到 endcoding='utf-8' 因为不用的话土耳其语识别不了")
    print(file)

with open("newfile.txt", encoding='utf-8') as file:
    print(file.read())
