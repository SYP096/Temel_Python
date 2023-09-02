'''这个类似于dict , 这个也是帮我们更好的理解以下的特殊函数'''
liste = [1, 2, 3]
print(len(liste))

s = "hello world"
print(len(s))


class Film:
    def __init__(self, baslik, yonetmen, sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure

    def __str__(self):
        return f"{self.baslik},  {self.yonetmen} tarafindan yönetildi."

    def __repr__(self):
        return f"{self.baslik},  {self.yonetmen} tarafindan yönetildi."

    def __len__(self):      # 调用的时候可以直接就像平常的内置函数一样
        return self.sure

    def __del__(self):        # 只要双下划线的方法一般都会自动执行
        print("film objesi silindi.")


f = Film("film adi", "yonetmen", 120)

print(str(liste))
print(str(f))
print(len(f))
