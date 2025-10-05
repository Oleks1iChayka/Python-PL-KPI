# 2. Вивести числа, що діляться на 4
lst = []
lst4 = []
a =1
for i in range(30):
    lst.append(a)
    a +=1

for i in range(len(lst)):
    if i // 4:
        lst4.append(i)
print(lst4)