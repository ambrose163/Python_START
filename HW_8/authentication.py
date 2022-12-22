from user_io import confirm_correctness, login_password_collection, name_sname_group_collection

SALT = 'non_auq_enis'
USERS_PATH = 'HW_8/auth.txt'

# def hash_password(password):
    # return hash(password + SALT) не работает, подобрать другую хэш-функцию

def get_users_dict():
    with open(USERS_PATH) as file:
        users_dict = {line.split()[0]: (line.split()[1], tuple(line.split()[2:])) for line in file.readlines()}
        return users_dict

def auth_user(login_password, users_dict):
    l_p = login_password[0] + login_password[1]
    return users_dict[l_p]

def add_user(): # добавление авторизованного пользователя
    print('Создание новой записи.')
    with open(USERS_PATH, 'a') as file:
        while True:
            l_p = login_password_collection()
            user_entity = l_p[0] + l_p[1] + ' '
            role = input('1. Учитель / 2. Ученик\n')
            if role == '1':
                user_entity += 't\n'
            elif role == '2':
                user_entity += 'p '
                user_tuple = name_sname_group_collection()
                if not user_tuple:
                    continue
                else:
                    for element in user_tuple[:-1]:
                        user_entity += f'{element} '
                    user_entity += f'{user_tuple[-1]}\n'
            else:
                print('Ошибка, начните сначала.')
                continue
            c_c = confirm_correctness()
            if c_c in 'lд':
                file.write(user_entity)
                print('Новый пользователь успешно создан.')
                break
            elif c_c in 'gп':
                print('Начните сначала и исправьте информацию.')
                continue
            else:
                print('Завершение работы.')
                exit()

if __name__ == '__main__': # режим системного администратора :) 
    add_user()