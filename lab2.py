def square(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return square(n-2) + (4 * (n-2)) + 4

n = 5
result = square(n)
print(result)
