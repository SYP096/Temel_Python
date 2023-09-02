class User:
    active_users = 0

    @classmethod             # 创建类方法的时候必须要加上@classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanici var."    # cls 可以直接使用类

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(', ')           # split 之后可以直接用来赋值
        return cls(first, last, age)
# 会去到14行, 就类似于 User("Ali", "Korkmaz", 20)   调用类，也就是使用类 看37

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan çikiş yapti."


print(User.display_active_users())
# userA = User("Sadik", "Turan", 37)
# userB = User("Sena", "Turan", 20)
# userC = User("Sena", "Turan", 20)
ali = User.from_string("Ali, Korkmaz, 20")
print(User.active_users)
print(ali.first)

# {"key":"value"}
# dict.fromkeys()
'''cls参数可以用于引用类本身,并在类方法中使用。在Python中,cls参数是一个约定俗成的参数名
它表示类本身。类方法可以通过cls参数来访问类级别的属性和方法, 而不是实例级别的属性和方法
'''
