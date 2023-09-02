markalar = ["opel", "bmw", "mercedes"]

# index = 0
# for marka in markalar:
#     print(f"{index+1}-{markalar[index]}")
#     index += 1

# enumarate

obj1 = enumerate(markalar)

print(type(obj1))        # <class 'enumerate'>
print(list(obj1))          # [(0, 'opel'), (1, 'bmw'), (2, 'mercedes')]

for index, value in enumerate(markalar, 1):
    print(f"{index}-{value}")

# zip

liste1 = [1, 2, 3, 4, 5]
liste2 = ['a', 'b', 'c', 'd', 'e', 'f']
liste3 = [100, 200, 300, 400, 500]

print(list(zip(liste1, liste2, liste3)))
# [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)]

for item in zip(liste1, liste2):
    print(item)


for a, b, c in zip(liste1, liste2, liste3):
    print(a, b, c)
aa = zip(liste1,  liste2)
print(type(aa), '\t', aa)
print(list(aa))
