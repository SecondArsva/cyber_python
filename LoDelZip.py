# ---
names = ["John", "David", "Eli"]
ages = [70, 30, 20]
shuffle = list(zip(names, ages))
print(shuffle)
# ---
names = ["John", "David", "Eli"]
ages = [70, 30]
shuffle = list(zip(names, ages))
print(shuffle)
# ---
for names, ages in zip(names, ages):
        print(f"{names} tiene {ages} años")
# ---
keys = ["nombre", "edad", "ciudad"]
values = ["Big Boss", 288, "Outher Heaven"]
dic = dict(zip(keys, values))
print(dic)
# ---
pairs = [("a", 1), ("b", 2), ("c", 3)]
chars, nums = zip(*pairs) # zip con "*" desempaqueta
print(chars)
print(nums)
# ---
a = [1, 2, 3]
b = [4, 5, 6]
new = [x + y for x, y in zip(a, b)]
print(new)
# ---
names = ["Aaa", "Eee", "Iii"]
ages = [1, 2, 3]
colours = ["white", "pink", "Brown"]
for name, age, color in zip(names, ages, colours):
        print(f"{name}, {age} años de color {color}")
# ---
z = zip([1, 2], [3, 4])
print(z)
