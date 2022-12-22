import authentication as auth
import user_io as uio
import file_io as fio
import datetime as dt

actual_user = ('login','password')

# def add_pupil():
#     while True:
#         entity_structure = ['Фамилия: ','Имя: ','Телефон: ','Описание: ']
#         new_entity = []
#         for element in entity_structure:
#             new_entity.append(input(f'{element}'))
#         match uio.confirm_correctness():
#             case 'l' | 'д':
#                 return tuple(new_entity)
#             case 'g' | 'п':
#                 print('Отмена внесенных изменений...')
#                 continue
#             case _:
#                 print('Возврат в предыдущее меню...')
#                 input()
#                 break

def teacher_facility():
    uio.teacher_start_screen()
    while True:
        try:
            record = teacher_grades()
            match uio.confirm_correctness():
                case 'l' | 'д':
                    fio.append_school_db(record)
                    print('Запись успешно внесена в базу данных.')
                case 'g' | 'п':
                    print('Отмена внесенных изменений...')
                    continue
                case _:
                    print('Возврат в предыдущее меню...')
                    input()
                    break
        except IndexError:
            if input('Не удалось преобразовать данные к стандартному виду.\n1. Повторите ввод.\n2. Выйти.\n') == '1':
                continue
            else:
                break

def teacher_grades():
    teacher_string = input(f'Внесение оценок производится по следующему шаблону:\nИмя, фамилия ученика, цифра и литера класса, предмет, оценки по предмету.\n').split()
    name, surname, group, subject, grades = teacher_string[0], teacher_string[1], teacher_string[2], teacher_string[3], ' '.join(teacher_string[4:])
    return (name, surname, group, subject, grades)

def pupil_facility():
    uio.pupil_screen(actual_user)
    fio.get_grades(actual_user[1])
    input()

def enter(role_flag):
    if role_flag == 't':
        teacher_facility()
    else:
        pupil_facility()

def program():
    uio.greet()
    while True:
        match uio.main_menu():
            case '1':
                try:
                    users_dict = auth.get_users_dict()
                    global actual_user
                    actual_user = auth.auth_user(uio.login_password_collection(), users_dict)
                    # breakpoint()
                    enter(actual_user[0]) # добавить извлечение id и вход по нему
                except KeyError:
                    print('Пользователя с таким логином и паролем не существует.')
                    input()

if __name__ == '__main__':
    program()                