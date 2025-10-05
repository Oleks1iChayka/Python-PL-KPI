# 4. Написати програму для обчислення суми квадратів чисел від 1 до (n)
n = int(input("Введіть n: "))
sum_squares = sum(i**2 for i in range(1, n+1))
print("Сума квадратів від 1 до", n, "=", sum_squares)
