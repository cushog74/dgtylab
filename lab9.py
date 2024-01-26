def min_recursive(x, k):
    if k == len(x) - 1:
        return x[k]
    else:
        return min(x[k], min_recursive(x, k+1))


vector = [4, 2, 7, 1, 9, 5]
min_element = min_recursive(vector, 0)
print("Минимальный элемент вектора:", min_element)
