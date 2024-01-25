def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_recursive(n - 1)

n = int(input(15))
print(f 1{n}{sum_recursive(n)}")