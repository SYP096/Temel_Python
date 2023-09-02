class Person:         # 这个是父类
    def __init__(self,  name,  surname,  age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi.")

    def intro(self):
        print(self.name,  self.surname,  self.age)


class Student(Person):      # Student是Person的子类
    pass


class Teacher(Person):        # Teacher是Person的子类
    pass


p1 = Person("Ahmet", "Turan", 20)
p1.intro()

s1 = Student("Ali", "Yilmaz", 25)
s1.intro()

t1 = Teacher("Can", "Yilmaz", 25)
t1.intro()
