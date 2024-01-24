def binom(n, m):
    if m == 0 or m == n:
        return 1
    else:
        return binom(n - 1, m) + binom(n - 1, m - 1)