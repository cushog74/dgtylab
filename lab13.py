def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_sum = sum_array(arr[:mid])
        right_sum = sum_array(arr[mid:])
        return left_sum + right_sum