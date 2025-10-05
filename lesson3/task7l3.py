# 7. Обчислити середнє арифметичне парних чисел
lst = []
lstp = []
a =1
suma = 0
kchysel = 0

for i in range(30):
    lst.append(a)
    a +=1

for i in range(len(lst)):
    if i // 2:
       suma += lstp[i]
       kchysel += 1
       
avgc = suma/kchysel
print(avgc)