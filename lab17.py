def rearrange_digits(n):
    even_digits = n % 10
    n = n // 10
    odd_digits = n % 10
    n = n // 10
    result = even_digits * 100 + odd_digits
    return result

n = 254631
print(rearrange_digits(n))