def digits():
    with open('input.txt', 'r') as file:
        text = file.read()
    
    num_chars = len(text) - 1

    num_digits = sum(1 for char in text if char.isdigit())
    return num_chars, num_digits
result = digits()
print("Количество символов:", result[0])
print("Количество цифр:", result[1])
