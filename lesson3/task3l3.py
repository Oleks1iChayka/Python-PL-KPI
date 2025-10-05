# 3. Порахувати кількість чисел, менших за 15
lst = []
lstm15 = []
a =1
for i in range(30):
    lst.append(a)
    a +=1

for i in range(len(lst)):
    if i < 15:
        lstm15.append(i)
print(lstm15)