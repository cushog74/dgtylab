def f(n):
    if n > 100:
        return n - 10
    else:
        return f(f(n + 11))

print("f(106) =", f(106))
print("f(99) =", f(99))
print("f(85) =", f(85))
