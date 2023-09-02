import random

# result = dir(random)
# result = help(random)

result = random.random()         # 0.0 - 1.0
result = random.random() * 100
result = int(random.uniform(10, 100))
print(result)
result = random.randint(1, 100)     # 1-100 随机 整数      含头含尾

greeting = 'hello there'
names = ['ali', 'yağmur', 'deniz', 'cenk', 'ahmet', 'efe']
# result = names[random.randint(0,len(names)-1)]      # 这个对应15行， 随机选取列表中的一个元素

result = random.choice(names)    # 随机选取元素
print(result)
result = random.choice(greeting)     # 当然也可以随机选取字符串
print(result)

liste = list(range(10))
random.shuffle(liste)           # shuffle  洗牌， 打乱该对象  也可以用tuple()
result = liste
print(result)
liste = range(100)
result = random.sample(liste, 3)          # 随机选取三个样品，且返回列表
print(result)
result = random.sample(names, 2)

print(result)
