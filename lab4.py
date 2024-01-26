def binomial_coefficient(m, n):
    if m == 0 or m == n:
        return 1
    else:
        return binomial_coefficient(m, n-1) + binomial_coefficient(m-1, n-1)

m = 2
n = 4
result = binomial_coefficient(m, n)
print(result)
