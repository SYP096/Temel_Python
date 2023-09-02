class Person:
    def __init__(self,  name,  surname,  age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi türetildi.")

    def intro(self):
        print(self.name,  self.surname,  self.age)


class Student(Person):
    def __init__(self,  name,  surname,  age,  number):        # 子类的__init__函数中必须包含父类__init__中的所有形参
        super().__init__(name, surname, age)              # or   Person.__init__(self, name, surname, age)
        self.number = number
        print("student nesnesi türetildi.")

    def intro(self):
        print(self.name,  self.surname,  self.age,  self.number)

    def study(self):
        print(f"{self.number} numarali öğrenci ders çaliyor.")


class Teacher(Person):
    def __init__(self,  name,  surname,  age,  branch):
        Person.__init__(self, name, surname, age)          # or      super().__init__(name, surname, age)
        self.branch = branch
        print("teacher nesnesi türetildi.")

    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} eğitimi veriyor.")


p1 = Person("Ahmet", "Turan", 20)
p1.intro()       # person

s1 = Student("Ali", "Yilmaz", 25,  101)
s1.intro()        # student
s1.study()

t1 = Teacher("Can", "Yilmaz", 25,  "ingilizce")
t1.intro()
t1.teach()

'''
创建的子类实例对象可以直接用父类的方法、不过要在__init__()紧接着的下面那一行加上super() or 父类名称
创建的父类实例对象不可以直接用子类的方法
因为根据父类创建的实例对象还没有和子类们存在连接、不可能关联到子类、也还不存在子类
不过根据子类创建的实例对象、父类已经和子类有了关联、所以子类的实例对象可以使用父类的方法
Not: 在父类存在的所用形参、在其子类也必须存在'''
