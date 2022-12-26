from logger import log
import model
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time


async def greetings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Вывод приветствия и меню.'''
    show_menu = ('/exit - Выход \n'
                 '/show - Загрузить из файла и вывести на экран \n'
                 '/add - Добавить новую запись\n(Пример: "/add Иван Иванов 89000000000 12.12.80 Завод)\n',)

    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}!\n'
                                    f'Вас приветствует телефонный справочник')
    time.sleep(3)
    await update.message.reply_text(show_menu[0])


async def show_book(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for my_dict in model.get_data():
        await update.message.reply_text(f'Имя: {my_dict["first_name"]}\n'
                                        f'Фамилия: {my_dict["last_name"]}\n'
                                        f'Телефон: {my_dict["phone_number"]}\n'
                                        f'Дата рождения: {my_dict["birthday"]}\n'
                                        f'Место работы: {my_dict["workplace"]}\n'
                                        f'Id: {my_dict["id"]}')
        await update.message.reply_text('************')


async def add_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    my_dict = {}
    tel_list = []
    my_dict['first_name'] = update.message.text.split()[1]
    my_dict['last_name'] = update.message.text.split()[2]
    my_dict['phone_number'] = update.message.text.split()[3]
    my_dict['birthday'] = update.message.text.split()[4]
    my_dict['workplace'] = update.message.text.split()[5]

    model.add_data(my_dict)


@log
def request_id() -> int:  # ввидите id input
    """
    Запрос id от пользователя
    :return id:
    """
    return int(input('Введите id: '))


@log
def editor(data: dict) -> dict:  # входит справочник пройти по нему
    """
    :param data: Выбранная запись
    :return отредактированная запись:
    """
    new_dict = {}
    data['first_name'] = input(f"Имя: {data['first_name']}. Введите новое имя: ")

    data['last_name'] = input(f"Фамилия: {data['last_name']} Введите новую фамилию: ")
    print("Телефон:", *data['phone_number'])
    tel_list = []
    while True:
        tel = input('Введите номер телефона (для выхода нажмите Enter) : ')
        if tel:
            tel_list.append(tel)
        else:
            break
    data['phone_number'] = tel_list
    data['birthday'] = input(f"Дата рождения: {data['birthday']} Введите новую дату: ")
    data['workplace'] = input(f"Место работы: {data['workplace']} Введите новое место работы: ")

    return data


@log
def request_last_name() -> str:  # input введите фамилию
    """
    Запрос фамилии от пользователя
    :return фамилия:
    """
    return input('Введите Фамилию: ')