'''Вивести всі числа в діапазоні від 1 до (n), які є квадратами натуральних
чисел'''
a = 1
n = int(input("num: "))
lst = []

for i in range(n):
    lst.append(a*a)
    a+= 1
print(lst)
