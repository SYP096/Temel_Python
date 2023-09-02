sayilar = [1, 5, 7, 45, 25, 89]
harfler = ['a', 'v', 'h', 's']
isimler = ['ahmet', 'ismail', 'ada', 'sena', 'sadik']
# max、min中都有很重要的key= 是用来做对比的属性、或函数作为关键词
sonuc = min(sayilar)      # 1
sonuc = max(sayilar)      # 89

sonuc = min(harfler)        # a
sonuc = max(harfler)       # v

sonuc = min(isimler)        # 'ada'
sonuc = max(isimler)        # 'sena'
# 一下四行代码，每个元素执行函数len、并且组建成一个新的由数字组成的列表或迭代器
sonuc = min([len(isim) for isim in isimler])         # 3
sonuc = min(map(len, isimler))                          # 同 14
sonuc = max([len(isim) for isim in isimler])        # 6
sonuc = max(map(len, isimler))

# key=function 是在运行max、min时所要对比的关键，输出的还是原列表中的元素
sonuc = max(isimler,  key=lambda n:  len(n))       # 'ismail'
sonuc = min(isimler,  key=lambda n:  len(n))        # 'ada'

urunler = [
    {"title": "iphone x", "price": 5000},
    {"title": "iphone xr", "price": 6000},
    {"title": "iphone 11", "price": 7000}
]

sonuc = min(urunler,  key=lambda urun:  urun['price'])
sonuc = min(urunler,  key=lambda urun:  urun['price'])['title']
sonuc = max(urunler,  key=lambda urun:  urun['price'])['title']

max = 0

for urun in urunler:
    if urun["price"] > max:
        max = urun["price"]

print(max)

print(sonuc)
