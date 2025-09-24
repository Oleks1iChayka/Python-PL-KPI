import random

a = [random.randint(-50, 50) for _ in range(12)]


sum_v = sum(x for x in a if x < 0)

print("Масив:", a)
print("Сума від’ємних елементів =", sum_v)
