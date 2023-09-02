# Destede kalan kart sayisi için kartSayisi() isminde bir metot.
# Destedeki kartlari kariştirmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar karti dağitmalidir.
# Destedeki kalan kart sayisina dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanilsin.

from random import shuffle


class Kart:
    def __init__(self, tip, deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):
        return f"{self.tip} {self.deger}"


class Deste:
    tipler = ["karo", "sinek", "kupa", "maça"]
    degerler = ["A", "2", "3", "4", "5",
                "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.kartlar = [Kart(tip, deger) for tip in Deste.tipler for deger
                        in Deste.degerler]

    def __iter__(self):        # 如果只有__iter__的话，就只是可迭代对象，而非迭代器
        return iter(self.kartlar)

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

for kart in deste1:
    print(kart)
