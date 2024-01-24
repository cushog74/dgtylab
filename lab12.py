def sum():
    numbers = input().split()
    if numbers[-1] == '.':
        numbers.pop()
    return sum_helper(numbers)

def sum_helper(numbers):
    if not numbers:
        return 0
    else:
        return float(numbers[0]) + sum_helper(numbers[1:])