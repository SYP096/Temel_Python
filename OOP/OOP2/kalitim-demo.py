# User
# Moderator


class User:
    active_users = 0

    @classmethod      # @这个是修饰符 , 还是挺有用的,可以直接用类名使用的类方法
    def display_active_users(cls):
        return f"şu anda aktif {cls.active_users} user var."

    def __init__(self, firstname, lastname):
        # 只要使用到这个类都会先到这个__init__()
        self.firstname = firstname
        self.lastname = lastname
        User.active_users += 1

    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Moderator(User):
    active_moderators = 0

    @classmethod
    def display_active_moderators(cls):
        return f"şu anda aktif {cls.active_moderators} moderator var."

    def __init__(self, firstname, lastname, community):
        super().__init__(firstname, lastname)
        self.community = community
        Moderator.active_moderators += 1

    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan bir post sildi."

    def update_post(self):
        return f"{self.fullname()} {self.community} grubunda bir post güncelledi."


print(User.display_active_users())      # 0
print(Moderator.display_active_moderators())        # 0

u1 = User("Ali", "Korkmaz")
m1 = Moderator("Yağmur", "Korkmaz", "yazilim")
m2 = Moderator("Canan", "Korkmaz", "kozmetik")

print(m1.remove_post())
print(m2.update_post())

print(User.display_active_users())          # 3
print(Moderator.display_active_moderators())         # 2

print(u1.fullname())
print(m1.fullname())

print(isinstance(u1,  User))                # True
print(isinstance(u1,  Moderator))       # False

print(isinstance(m1,  User))               # True
print(isinstance(m1,  Moderator))      # True
# isinstance(a, b) 判断 a 是否是 b 的实例对象、子类的实例对象同时也是父类的实例对象
