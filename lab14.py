def digits():
    with open("input.txt", "r") as file:
        text = file.read()
    text = text.replace('.', '')
    return len(text)