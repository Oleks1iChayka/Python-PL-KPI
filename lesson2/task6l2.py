# 6. Створити масив із 12 елементів. Заповнити випадковими числами від -50 до 50.
import random
a = []

for i in range(12):
    a.append(random.randint(-50, 50))

print("Масив:", a)
