def sum_of_array(arr):
    def recursive_sum(start, end):
        if start >= end:
            return arr[start]

        mid = (start + end) // 2
        left_sum = recursive_sum(start, mid)
        right_sum = recursive_sum(mid + 1, end)

        return left_sum + right_sum

    return recursive_sum(0, len(arr) - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_array(arr))