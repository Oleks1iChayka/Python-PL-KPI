# 9. Порахувати кількість входжень числа 10
lst = []
a =1
for i in range(30):
    lst.append(a)
    a +=1

c10 = 0

for i in range(len(lst)):
    if lst[i] == 10:
        c10 += 1

print(c10)