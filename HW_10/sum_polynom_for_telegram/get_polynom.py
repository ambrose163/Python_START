from random import randrange
from os import path, mkdir, chdir
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


def create_polynom(list_k):
    i = len(list_k) - 1
    new_polynom = ""  # создание полинома
    plus = False
    for num in list_k:
        if num:
            if plus:
                new_polynom += " + "
            else:
                plus = True

            if i > 1:
                new_polynom += f"{'' if num == 1 else num}x^{i}"
            elif i == 1:
                new_polynom += f"{'' if num == 1 else num}x"
            else:
                new_polynom += f"{num}"
        i -= 1
    if not new_polynom:
        new_polynom += "0 = 0"
    else:
        new_polynom += " = 0"
    return new_polynom


async def view_polynom(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    k = int(update.message.text.split()[1])
    # k = int(input("Введите натуральное число k "))
    polynom = [randrange(101) for i in range(k + 1)]
    str_polynom = create_polynom(polynom)
    await update.message.reply_text(f'Сгенерирован полином:\n'
                                    f'{str_polynom}')
    # print(str_polynom)  # Вывод в консоль

    if not path.isdir("polynom"):  # Запись в файл
        mkdir("polynom")
    chdir("polynom")
    i = 0
    while True:
        if not path.isfile(f"polynom_{i}.txt"):
            with open(f"polynom_{i}.txt", 'w') as file:
                file.write(str_polynom)
                print(f"Результат записан в файл polynom_{i}.txt")
            break
        else:
            i += 1
    chdir('../')