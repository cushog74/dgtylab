def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return sum_recursive(n-1) + n


n = 5
sum_of_numbers = sum_recursive(n)
print("Сумма чисел от 1 до", n, ":", sum_of_numbers)
