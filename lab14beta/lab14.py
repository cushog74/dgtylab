import os

def digits():
    with open('input.txt', 'r') as file:
        text = file.read()
    
    def count_symbols(text, count=0):
        for char in text:
            if char.isalpha() or char.isspace() or char.isdigit():
                count += 1
            else:
                return count
        return count
    
    def count_digits(text, count=0):
        for char in text:
            if char.isdigit():
                count += 1
            else:
                return count
        return count
    
    symbols_count = count_symbols(text)
    digits_count = count_digits(text)
    
    print(f"Количество символов в тексте: {symbols_count}")
    print(f"Количество цифр в тексте: {digits_count}")

digits()