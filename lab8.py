def is_power_of_two(n):
    if n == 1:  
        return True
    elif n % 2 != 0 or n == 0:  
        return False
    else:
        return is_power_of_two(n // 2) 


print(is_power_of_two(16))  
print(is_power_of_two(17))
print(is_power_of_two(0))
