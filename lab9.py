def min(x, k):
    if k == 0:
        return x[0]
    else:
        return min(x[k:], 0)