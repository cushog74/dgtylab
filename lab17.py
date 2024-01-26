def rearrange_digits(n):
    if n < 10:
        return n
    else:
        odd_digits = []
        even_digits = []
        while n > 0:
            digit = n % 10
            if digit % 2 == 0:
                even_digits.append(digit)
            else:
                odd_digits.append(digit)
            n = n // 10
        odd_digits.reverse()
        even_digits.reverse()
        result = int(''.join(map(str, odd_digits + even_digits)))
        return result

n = 254631
result = rearrange_digits(n)
print(result)
