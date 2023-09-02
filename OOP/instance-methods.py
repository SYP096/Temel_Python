class Person:

    # yapici metotlar (constructor)
    def __init__(self, name, surname, year):

        # object attributes,  instance attributes
        self.name = name
        self.surname = surname
        self.year = year

    # instance methods
    def intro(self):               # 实例方法只有实例对象可以调用， 类对象不能调用实例方法
        return f"Benim adim {self.name} ve soyadim {self.surname}"

    def calculate_age(self):
        return f"{2023-self.year}"


# Object,  Instance
p1 = Person("Sadik", "Turan", 1983)      # pa 就是 self 就是可以直接调用实例对象
p2 = Person("Sena", "Turan", 1999)

print(p1.intro())                   # 实例对象调用 类对象 中的实例方法
print(p2.intro())

print(p1.calculate_age())
print(p2.calculate_age())
'''
实例方法只能用实例对象调用， 无法用类方法调用实例方法
'''
