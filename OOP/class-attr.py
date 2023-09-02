class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1          # 想要调用class attributes 必须要用到  类名.

    def full_name(self):
        return f"{self.first} {self.last}"

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} uygulamadan çikiş yapti."


print(User.active_users)
userA = User("Sadik", "Turan", 37)
userB = User("Sena", "Turan", 20)
userC = User("Çinar", "Turan", 4)
print(User.active_users)
print(userC.logout())
print(User.active_users)

# print(userA.full_name())
# print(userB.full_name())
