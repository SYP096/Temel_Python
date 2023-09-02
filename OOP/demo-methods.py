# BankAccount isminde bir sinif tanimlayiniz.
# Üretilen her bir nesne owner isminde biz özelliğe sahip olmalidir. BankAccount("Sadik Turan")
# Üretilen her bir nesne balance isminde bir özelliğe sahip olup başlangiçta 0.0 değerinde olmalidir.
# Üretilen her bir nesne için deposit metodu oluşturun ve dişaridan yatirilacak miktar bilgisini alip balance
# üzerine ekleyin ve balance miktarini geriye döndürün.
# Üretilen her bir nesne için withdraw metodu oluşturun ve dişaridan çekilecek miktar bilgisini alip balance
# değerinden çikarip geriye döndürün.

# hesap = BankAccount("Sadik Turan")
# hesap.owner => Sadik Turan
# hesap.balance => 0.0
# hesap.deposit(1000) => 1000.0
# hesap.withdraw(500) => 500.0

class BankAccount:
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


hesap = BankAccount("Sadik Turan")

print(hesap.getBalance())
hesap.deposit(1000)
print(hesap.getBalance())
hesap.withdraw(500)
print(hesap.getBalance())
