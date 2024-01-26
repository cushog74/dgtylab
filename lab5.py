def multiply(a, b):
    if a == 1:
        return b
    else:
        return multiply(a-1, b) + b

a = 3
b = 4
result = multiply(a, b)
print(result)
