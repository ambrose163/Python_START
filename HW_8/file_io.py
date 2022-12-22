import pandas as pd

# Пути чтения/записи
GRADES_FILE_PATH = 'HW_8/pupil_grades.csv'

COLUMN_NAMES = ['Имя','Фамилия','Класс','Предмет','Оценки']


def append_school_db(record):
    with open(GRADES_FILE_PATH, 'a') as file:
        for element in record[:-1]:
            file.write(f'{element},')
        file.write(f'{record[-1]}\n')

def get_grades(pupil_tuple):
    data = pd.read_csv(GRADES_FILE_PATH, names = COLUMN_NAMES)
    for i in range(len(data)):
        if data['Имя'][i] == pupil_tuple[0] and data['Фамилия'][i] == pupil_tuple[1] and data['Класс'][i] == pupil_tuple[2]:
            print(data['Предмет'][i] + ': ' + data['Оценки'][i])
    
if __name__ == '__main__':
    get_grades()                