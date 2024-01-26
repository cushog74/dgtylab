def digits():
    # Открываем файл для чтения
    with open('input.txt', 'r') as file:
        # Читаем содержимое файла
        content = file.read()
        
        # Если достигнут конец файла, возвращаем 0
        if content == '.':
            return 0
        
        # Рекурсивно вызываем функцию для оставшейся части
        return 1 + digits()