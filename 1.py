with open('Моя часть работы в %.txt', 'r',encoding='utf-8') as file:
    text = file.read()
words = text.split()
print("Количество слов в файле:", len(words))