# 6. Вивести список у зворотному порядку
lst = []
lstr =[]
a =1
for i in range(30):
    lst.append(a)
    a +=1
for i in range(len(lst) - 1, -1, -1):
    lstr.append(lst[i])

print(lstr)