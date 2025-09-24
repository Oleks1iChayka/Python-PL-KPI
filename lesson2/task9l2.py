import random

a = [random.randint(-50, 50) for _ in range(12)]

print("Масив:", a)

s = a[1] + a[-2]
a[1] = s
a[-2] = s


print("Масив після заміни:", a)
