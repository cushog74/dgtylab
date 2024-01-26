def find_root(f, a, b, eps):
    c = (a + b) / 2 
    if abs(f(c)) < eps: 
        return c
    elif f(a) * f(c) < 0: 
        return find_root(f, a, c, eps)  
    else:
        return find_root(f, c, b, eps) 

def f(x):
    return x**2 - 4  
a = 1  
b = 3  
eps = 0.0001  
root = find_root(f, a, b, eps) 
print("Корень уравнения f(x) = 0:", root)
