def sum(n, p):
    if n == 0:
        return 0
    elif n == 1 and p == 1:
        return 1
    elif n == 2 and p == 2:
        return 2
    else:
        return sum(n - p, p) + sum(n - 1, p)