def sum_array(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2 
        left_sum = sum_array(arr[:mid])
        right_sum = sum_array(arr[mid:])
        return left_sum + right_sum 
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_array(arr)
print("Сумма элементов массива:", result)