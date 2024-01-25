def sum():
    def recursive_sum(numbers):
        if not numbers:
            return 0

        current_number = numbers.pop(0)
        if current_number < 0:
            return current_number + recursive_sum(numbers)
        else:
            return current_number + recursive_sum(numbers)

    numbers = []
    while True:
        try:
            number = float(input("Введите положительное вещественное число: "))
            if number >= 0:
                numbers.append(number)
            else:
                break
        except ValueError:
            print("Введено неверное значение. Пожалуйста, введите положительное вещественное число.")

    return recursive_sum(numbers)

print(sum())