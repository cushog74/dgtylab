def print_numbers():
    numbers = input().split()
    for number in numbers:
        if int(number) < 0:
            print(number, end=' ')
    for number in numbers:
        if int(number) >= 0:
            print(number, end=' ')
    print()