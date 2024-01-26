sequence = []
num = int(input("Введите число: "))
while num != 0:
    sequence.append(num)
    num = int(input("Введите число: "))

negative_numbers = []
positive_numbers = []

for num in sequence:
    if num < 0:
        negative_numbers.append(num)
    else:
        positive_numbers.append(num)

print("Отрицательные числа:", negative_numbers)
print("Положительные числа:", positive_numbers)