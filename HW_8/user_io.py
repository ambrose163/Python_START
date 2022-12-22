from os import system
from random import choice

def glossary():
    glossary = ['Repititio est mater studiorum',
                'Qui scribit bis legit',
                'Pigritia est mater vitiorum',
                'Carpe diem',
                'Quod licet Jovi non licet bovi',
                'Suum quique',
                'Non est fumus absque igne',
                'Simile similibus curantur',
                'Cogito ergo sum',
                'Mens sana in corpore sano',
                'Alea jacta est',
    ]
    return choice(glossary)

def greet():
    system('cls')
    print(f'Добро пожаловать в программу Школьная база данных!\nАфоризм дня: {glossary()}.')
    input()
    
def main_menu():
    while True:
        system('cls')
        print('1. Войти, используя логин и пароль')
        print('2. Выход из программы')
        user_input = input()
        match user_input:
            case '1':
                return user_input
            case '2':
                print('Завершение работы.')
                exit()
            case _:
                print('Ошибка. Нажмите ENTER, затем повторите ввод.')
                input()

def login_password_collection():
    print('Введите логин: ')
    user_input_1 = input()
    print('Введите пароль: ')
    # user_input_2 = hash_password(input()) # переписать хэш-функцию
    user_input_2 = input()
    return (user_input_1, user_input_2)

def name_sname_group_collection():
    while True:
        print('Введите имя: ')
        user_input_1 = input()
        print('Введите фамилию: ')
        user_input_2 = input()
        print('Введите цифру и литеру класса без пробела: ')
        user_input_3 = input().upper()
        # match confirm_correctness().lower():
        #     case 'l' | 'д':
        #         return (user_input_1, user_input_2, user_input_3)
        #     case 'g' | 'п':
        #         continue
        #     case _:
        #         break
        return (user_input_1, user_input_2, user_input_3)

def confirm_correctness():
    user_input = input('Проверьте правильность введенных данных:\n- Д или L, затем ENTER, чтобы подтвердить.\n- П или G, затем ENTER, чтобы повторить и справить.\n- Нажмите любую иную клавишу, затем ENTER, для отмены.\n').lower()
    return user_input

def pupil_screen(actual_user):
    system('cls')
    print(f'Здравствуйте, уважаемый ученик {actual_user[1][0]} {actual_user[1][1]}! Просмотрите свои оценки по предметам:')

def show_grades(subj_list):
    for subject in subj_list:
        print(f'{subject[0]}: {subject[1]}')
    input()

def teacher_start_screen():
    system('cls')
    print(f'Здравствуйте, уважаемый преподаватель! Внесите оценки в журнал по своему предмету.')

if __name__ == '__main__':
    print(name_sname_group_collection())