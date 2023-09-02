class NewDict(dict):        # 父级是字典dict       其实这些都是字典中拥有函数，只是写出来让我们更好的理解
    def __repr__(self):
        print('repr metondundan mesaj var.')
        return super().__repr__()

    def __missing__(self, key):
        print("olmayan key bilgisi istiyorsunuz.")

    def __getitem__(self, key):
        print("bir elemani çağiriyorsunuz.")
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print("listeye eleman ekliyorsunuz.")      # 或者更改
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("listede eleman arayamasiniz")
        return super().__contains__(item)


data = NewDict({"first": "Sadik", "last": "Turan"})     # 调用之后，父级dict的值就会是这个字典

print(data["first"])      # 调用的是第9行
data["age"]      # 如果该key不存在于父级字典中，就会执行第六行的__missing__
data["first"] = "Çinar"        # 调用的是第13行

print(data)      # 调用的是第2行

print("first" in data)     # 调用的是第17行
print(dir(dict))
