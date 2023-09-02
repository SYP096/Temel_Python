liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz. 要就报错就用1，不要求报错就用2
for i in liste:
    try:
        sonuc = int(i)        # 只有数字类型才能使用int()，否则就会报错
        print(sonuc)
    except ValueError:
        continue
'''
for i in liste:       # 不要求报错就用这个吧
    if i.isdigit():
        print(i)
'''
print([i for i in liste if i.isdigit()])                      # 或者就用列表生成式
print(list(filter(lambda i: i.isdigit(), liste)))       # 直接用filtre筛选也行
# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın.
'''
while True:
    mesaj = input("请输入一个数字:  ")
    if mesaj == 'q':
        break
    else:
        try:
            mesaj = float(mesaj)
            print(f"Your entered number is {mesaj}")
        except ValueError:
            print("Input Error")
            continue
'''
# 3: Dictionary ve key bilgilerini parametre olarak alan get(d,  key)
# fonksiyonu hazırlayınız.
urun = {"urunAdi": "samsung s10"}

# d["fiyat"] => KeyError

# get(d,  "fiyat") => None
# get(d,  "urunAdi") => samsung S10


def get(d,  key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(urun,  'fiyat'))
print(get(urun,  'urunAdi'))
