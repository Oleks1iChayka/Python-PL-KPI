# 10. Знайти різницю між найбільшим і найменшим елементом
lst = []
a =1
for i in range(30):
    lst.append(a)
    a +=1

min_lst = min(lst)
max_lst = max(lst)

riz = max_lst - min_lst
print(riz)