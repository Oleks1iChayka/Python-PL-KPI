# 7. Знайти суму всіх від’ємних елементів масиву.
import random

a = []

for i in range(12):
    a.append(random.randint(-50, 50))


sum_v = sum(x for x in a if x < 0)

print("Масив:", a)
print("Сума від’ємних елементів =", sum_v)
