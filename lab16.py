
def find_root(a, b, eps):
    if b - a < eps:
        return (a + b) / 2
    else:
        mid = (a + b) / 2
        if f(mid) * f(mid + eps) < 0:
            return find_root(a, mid, eps)
        else:
            return find_root(mid, b, eps)
        
a=1
b=14
eps=19
print(find_root(a, b, eps))