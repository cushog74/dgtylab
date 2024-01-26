def sum():
    number = float(input("Введите число: "))
    if number < 0:
        return 0
    else:
        return number + sum()

result = sum()
print("Сумма положительных чисел:", result)