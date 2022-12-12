# Реализуйте код игры.
# Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
# Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
# Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
# Он забирает также все конфеты оппонента.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?
# a) Добавьте игру против бота
# b) Подумайте, как наделить бота простейшим "интеллектом"


import random
from random import randint


player = input('Введите имя игрока: ')
bot = 'BOT'
candy = int(input('Введите кол-во конфет на столе candy = '))
m_max = int(input('Введите максимальное кол-во конфет, возможное за один ход m_max = '))
# print(k % (m_max + 1))
fortune = random.randint(0, 2)

if fortune:
    print(f'Первым ходит {player}')
else:
    print(f'Первым ходит {bot}')


def take_candy_amount(name):
    if name == player:
        move = int(input(f'{name}, введите кол-во конфет от 1 до {m_max}: '))
        while move < 1 or move > m_max:
            move = int(input(f'{name}, введите кол-во конфет от 1 до {m_max}: '))
    else:
        move = random.randint(1, m_max)
    return move


def player_output(name, candy, count, move):
    print(f'За этот ход {name} взял {move} конфет, всего у него {count}.\n'
          f'На столе осталось {candy} конфет.')


count1 = 0
count2 = 0

while candy > 11:
    if fortune:
        move = take_candy_amount(player)
        count1 += move
        candy -= move
        fortune = False
        player_output(player, candy, count1, move)
    else:
        move = take_candy_amount(bot)
        count2 += move
        candy -= move
        fortune = True
        player_output(bot, candy, count2, move)

if fortune:
    print(f'Выиграл {player}')
else:
    print(f'Выиграл {bot}')

# _________________________________________________________________________________________________________________


# import random
# from random import randint


# player1 = input('Введите имя игрока 1: ')
# player2 = input('Введите имя игрока 2: ')
# candy = int(input('Введите кол-во конфет на столе candy = '))
# m_max = int(input('Введите максимальное кол-во конфет, возможное за один ход m_max = '))
# print(candy % (m_max + 1))
# fortune = random.randint(0, 2)

# if fortune:
#    print(f'Первый ход у {player1}')
#else:
#    print(f'Первый ход у {player2}')


# def take_candy_amount(name):
#    move = int(input(f'{name}, введите кол-во конфет от 1 до {m_max}: '))
#    while move < 1 or move > m_max:
#        move = int(input(f'{name}, введите кол-во конфет от 1 до {m_max}: '))
#    return move


# def player_output(name, candy, count, move):
#    print(f'{name} взял {move} конфет, всего у него {count}.\n'
#          f'На столе осталось {candy} конфет.')


# count1 = 0
# count2 = 0

# while candy > 11:
#    if fortune:
#        move = take_candy_amount(player1)
#        count1 += move
#        candy -= move
#        fortune = False
#        player_output(player1, candy, count1, move)
#    else:
#        move = take_candy_amount(player2)
#        count2 += move
#        candy -= move
#        fortune = True
#        player_output(player2, candy, count2, move)

# if fortune:
#    print(f'{player1} - победитель')
# else:
#    print(f'{player2} - победитель')