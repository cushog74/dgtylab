def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    else:
        return x * power(x, n - 1)

x = 2.0
n = 3
result = power(x, n)
print(result)
