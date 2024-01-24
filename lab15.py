def print_numbers(sequence):
    negative_numbers = [num for num in sequence if num < 0]
    positive_numbers = [num for num in sequence if num > 0]
    
    negative_numbers.sort(reverse=True)
    positive_numbers.sort()
    
    print('Отрицательные числа:', negative_numbers)
    print('Положительные числа:', positive_numbers)

sequence = [1, -2, 3, -4, 5, -6, 7, -8, 9, 10, 0]
print_numbers(sequence)
