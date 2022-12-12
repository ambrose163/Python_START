# Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».


with open('file_task_1.txt', encoding='utf-8') as file: # открыт для чтения
       data = file.readline()

print(data)
data = [word for word in data.split() if 'абв' not in word]
print(' '.join(data))