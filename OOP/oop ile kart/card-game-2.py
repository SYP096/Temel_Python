# Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart türünü temsil edecek. (sinek 5)
# Kart sınıfının tip ve deger isminde 2 instance özelliği olsun. (tip:sinek deger:5)
# Kart sınıfının kartıGetir() ismindeki instance metodu kart bilgilerini yazdırsın.
# Kart bilgilerini yazdırmak için __repr__ metodunu kullanın. (Araştırma...)

class Kart:
    def __init__(self, tip, deger):
        self.tip = tip
        self.deger = deger

    # def kartiGetir(self):
    #     return f"{self.tip} {self.deger}"

    def __repr__(self):         # 打印实例对象时， 返回一个字符串，告诉您这个对象的·类型和状态。必须是字符串！！
        return f"{self.tip} {self.deger}"


sinek5 = Kart("sinek", "5")
karoAs = Kart("karo", "A")

# print(sinek5.kartiGetir())
# print(karoAs.kartiGetir())

print(sinek5)
print(karoAs)
