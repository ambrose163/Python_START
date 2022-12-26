from os import path, chdir, listdir
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import emoji


def parser(polynom):
    if not polynom:
        return {}
    polynom = polynom[:polynom.find("=")]
    map_polynom = map(str.strip, polynom.split("+"))
    dict_polynom = {}
    for data in map_polynom:
        if "x" in data:
            if "^" in data:
                dict_polynom[int(data[data.find("^") + 1:])] = int(data[:data.find("x")])
            else:
                dict_polynom[1] = int(data[:-1])
        else:
            dict_polynom[0] = int(data)
    return dict_polynom


def sum_polynom(poly1, poly2):
    res_polynom = parser(poly1)
    dict_polynom = parser(poly2)
    for key in dict_polynom:
        val = res_polynom.get(key)
        if val:
            res_polynom[key] += dict_polynom[key]
        else:
            res_polynom[key] = dict_polynom[key]
    return create_polynom(res_polynom)


def create_polynom(dict_polynom):
    new_polynom = ""  # создание полинома
    plus = False
    for key in sorted(dict_polynom)[::-1]:
        if plus:
            new_polynom += " + "
        else:
            plus = True

        if key > 1:
            new_polynom += f"{'' if dict_polynom[key] == 1 else dict_polynom[key]}x^{key}"
        elif key == 1:
            new_polynom += f"{'' if dict_polynom[key] == 1 else dict_polynom[key]}x"
        else:
            new_polynom += f"{dict_polynom[key]}"
    if not new_polynom:
        new_polynom += "0 = 0"
    else:
        new_polynom += " = 0"
    return new_polynom


async def view_sum_polynom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if path.isdir("polynom"):  # Проверка присутствия каталога
        chdir("polynom")
    else:
        await update.message.reply_text(f'Не сгенерировано ни одного многочлена {emoji.emojize(":frowning_face:")}')
        exit()

    res_polynom = ""
    for file_name in listdir():
        if "polynom_" in file_name:
            with open(file_name, 'r') as file:
                str_polynom = file.read()
                # print(f"{str_polynom} из файла {file_name}")
                res_polynom = sum_polynom(res_polynom, str_polynom)
    await update.message.reply_text(f'Сумма всех сгенерированных многочленов {res_polynom}')
    await update.message.reply_text(f'{emoji.emojize(":check_mark_button:")}')
    # print(f"Сумма многочленов из файлов: {res_polynom}")

    with open("sum_polynom.txt", 'w') as file:  # Запись в файл
        file.write(str_polynom)
        # print("Результат записан в файл sum_polynom.txt")