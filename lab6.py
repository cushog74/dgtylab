def calculate_A(n, m):
    if n == 0:
        return m + 1
    elif n > 0 and m == 0:
        return calculate_A(n - 1, 1)
    else:
        return calculate_A(n - 1, calculate_A(n, m - 1))

n = 2
m = 3
result = calculate_A(n, m)
print(result)
