# 8. Скласти новий список, де всі елементи піднесені до куба
lst_cube = []
lst = []
a =1
for i in range(30):
    lst.append(a)
    a +=1

for i in range(len(lst)):
    lst_cube.append(lst[i] ** 3)  

print(lst_cube)