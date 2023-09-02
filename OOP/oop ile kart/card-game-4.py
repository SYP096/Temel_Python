# Destede kalan kart sayisi için kartSayisi() isminde bir metot.
# Destedeki kartlari kariştirmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar karti dağitmalidir. Destedeki kalan kart sayisina dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanilsin.
from random import shuffle
'''从random, 模块中导入shuffle函数 , 该函数是洗牌 , 可以彻底打乱一个对象的顺序'''


class Kart:
    def __init__(self, tip, deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):        # 打印实例对象时， 返回一个字符串，告诉您这个对象的·类型和状态。必须是字符串！！
        '''总之 , 类对象和实例对象都会直接运行这个函数'''
        return f"{self.tip} {self.deger}"


class Deste:
    tipler = ["karo", "sinek", "kupa", "maça"]
    degerler = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.kartlar = [Kart(tip, deger) for tip in Deste.tipler for deger in Deste.degerler]

    def kartSayisi(self):
        return len(self.kartlar)

    def kartlariKaristir(self):
        if (self.kartSayisi() < 52):
            raise ValueError("Deste bozulmadan kartlari kariştirabilirsiniz.")
        shuffle(self.kartlar)

    def kartDagit(self, adet):
        kartSayisi = self.kartSayisi()
        if kartSayisi == 0:
            raise ValueError("Bütün kartlar dağitildi.")
        adet = min([kartSayisi, adet])
        kartlar = self.kartlar[-adet:]
        self.kartlar = self.kartlar[:-adet]
        return kartlar

    def kartAt(self):
        return self.kartDagit(1)[0]


deste1 = Deste()

deste1.kartlariKaristir()

print(deste1.kartAt())

print(deste1.kartDagit(5))
print(deste1.kartlar)
print(deste1.kartSayisi())
print(deste1.kartDagit(3))
print(deste1.kartSayisi())

print(deste1.kartlar)
