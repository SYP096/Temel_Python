class Pet:
    cinsler = ["kedi", "köpek", "kuş"]
    count = 0

    def __init__(self, isim, cins):
        if cins not in Pet.cinsler:         # 在方法中使用类属性时   需要用到  类名.
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        # 别忘了raise是自己定义一个报错
        self.isim = isim
        self.cins = cins
        Pet.count += 1
        Pet.cinsler.append(isim)         # 在这里的更改也会直接更改列表
        print(Pet.count)

    def set_cins(self, cins):
        if cins not in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değildir.")
        self.cins = cins


boncuk = Pet("Boncuk", "kedi")
pasa = Pet("Paşa", "köpek")
mavis = Pet("Maviş", "kuş")

# mavis.set_cins("aslan")
pasa.count = 10            # 这个实例对象的更改，只针对此对象， 不影响类对象和其他实例对象
print(pasa.count)      # 10
pasa = Pet("Paşa", "köpek")
# 到13行时输出为 4， 因为26的操作不影响类属性，所以类属性pet.count还是3+1
Pet.count = 10                           # 这个直接更改了类属性
pasa = Pet("Paşa", "köpek")         # 28 行， 是类属性的值改为了10 ， 所以是 10+1=11
Pet.cinsler.append("balik")
# 列表和类属性不太一样， 列表是可变对象 所以任何改变都会直接映射在类和其他实例对象中
boncuk.cinsler.append("at")
print(boncuk.cinsler)
# pasa.cinsler.append("at")

print(Pet.cinsler)
print(boncuk.cinsler)
print(pasa.cinsler)
'''
虽然类属性和列表在 Python 中的行为有所不同，但是它们都具有共享性,
这意味着它们可以被所有实例对象和类共享，并且当一个实例对象修改它们时
其他实例对象和类本身也会看到这个更改（对于可变对象而言）。
-----也就是说，类属性的更改是共享的， 但是只是针对类属性的更改， 例如上面的Pet.count
-----但是， 实例属性中 count 的更改不影响 类 和 其他实例对象， 例如上面的pasa.count
===列表不太一样， 列表是完全共享的， 实例属性对其的所有更改都会直接映射到 类 和 其他实例对象中
/////////////实例方法是能用实例对象调用， 类对象无法调用实例方法
'''
