#Вивести всі числа від 1 до 200, кратні 8.
a = 0
lst = []
for i in range(1, 200, 8):
    a+=8
    lst.append(a)

print(lst)
