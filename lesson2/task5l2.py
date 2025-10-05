# 5. Знайти кількість парних цифр у заданому числі.
num = int(input("Введіть число: "))
even_digits = sum(1 for d in str(abs(num)) if int(d) % 2 == 0)
print("Кількість парних цифр =", even_digits)
