# 4. Замінити всі елементи, більші за 25, на -1

lst = []
lst25 = []
a =1
for i in range(30):
    lst.append(a)
    a +=1

for i in range(len(lst)):
    if i > 25:
        lst25[i] == -1
print(lst25)