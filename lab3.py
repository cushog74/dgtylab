def Fact2(n):
    if n <= 0:
        return 1
    else:
        return n * Fact2(n - 2) if n > 1 else 1

n = 6
result = Fact2(n)
print(result)
