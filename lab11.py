def sum_recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n + sum_recursive(n-2) + sum_recursive(n-1)

n = 11
result = sum_recursive(n)
print(result)
