def recursive_sum(n, p, a):
    if n == 1:
        return 1
    elif n == p:
        return n
    else:
        return n + recursive_sum(n - a, p, a)

n = 5
p = 2
a = 1
result = recursive_sum(n, p, a)
print(f"Сумма чисел от {n} до 1 по формуле sum(n) = sum(n,2) + sum(n-1,2) равна: {result}")