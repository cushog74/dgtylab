def Fact2(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return n * Fact2(n - 2)
    else:
        return n * Fact2(n - 2) * 1