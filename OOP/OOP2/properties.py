class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.description = description
        if price >= 0:
            self._price = price     # _price是私有变量，只能在模块内部使用。
        else:
            raise ValueError("fiyat için negatif değer atamasi yapilmaz")

    @property        # 属性，所有权。把方法转化成属性
    def price(self):
        return self._price

    @price.setter       # 表示原本是私有属性的_price可以被设置，可以被改变
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("fiyat için negatif değer atamasi yapilmaz")

    @property
    def short_description(self):
        return self.description[:10]

    # def set_price(self, value):
    #     if value >=0:
    #         self._price = value
    #     else:
    #         raise ValueError("fiyat için negatif değer atamasi yapilmaz")

    # def get_price(self):
    #     return self._price


p = Product("iphone 12",  9000,
            "iphone 12 en yeni üründür ancak fiyati çok pahali.")
print(p.price)
print(p.short_description)
'''私有属性只能在模块内部使用, 如果想在外部使用必须在类内部定以一个@property
如果没有@property就直接调用的话会报错'''

"""
设置属性值:
被 @property 装饰的方法是获取属性值的方法，被装饰方法的名字会被用做属性名.
被 @属性名.setter 装饰的方法是设置属性值的方法。
被 @属性名.deleter 装饰的方法是删除属性值的方法。
"""
