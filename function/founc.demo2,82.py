# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
'''


def karsilastirma(a, b):
    if (a > b):
        return "a b den büyük"
    elif (b > a):
        return "b a dan büyük"
    return "a b ye eşit"


sonuc = karsilastirma(a=10, b=20)
sonuc = karsilastirma(a=10, b=10)
print(sonuc)
'''
# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
# 搜索有几个相同元素，用 count ， 多做题，多练习


def same_alpha(args):
    print(args)
    dic = {alpha: args.count(alpha) for alpha in args}   # 很重要
    return dic


keybord = "qrqerqwerqerqwererwerqwerwqr24124"
print(same_alpha(keybord))
# Kendisine gönderilen list,  command,  position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
# [1, 2, 3],  ("add,  remove"),  ("beginning | end"),  value
# list_operation([1, 2, 3], "add", "end", "4") => [1, 2, 3, 4]
# list_operation([1, 2, 3], "remove", "beginning") => [2, 3]


def update_list(liste,  command,  position,  value=None):
    if (command == "remove" and position == "end"):
        liste.pop()
        return liste
    elif (command == "remove" and position == "beginning"):
        liste.pop(0)
        return liste
    elif (command == "add" and position == "end"):
        liste.append(value)
        return liste
    elif (command == "add" and position == "beginning"):
        liste.insert(0, value)
        return liste


sonuc = update_list([1, 2, 3],  "add",  "end",  4)
print(sonuc)
sonuc = update_list([1, 2, 3],  "add",  "beginning",  4)
print(sonuc)
sonuc = update_list([1, 2, 3],  "remove",  "beginning")
print(sonuc)
sonuc = update_list([1, 2, 3],  "remove",  "end")
print(sonuc)

# Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.


def contains_blue(*args):
    print(type(args))
    if "blue" in args:
        return True
    return False


sonuc = contains_blue("blue", "yellow", "red")
sonuc = contains_blue("green", "yellow", "red", "black")

print(sonuc)
