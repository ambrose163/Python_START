# Даны файлы, в каждом из которых находится запись многочлена.
# Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
# Входными данными для этой задачи являются выходные данные их предыдущей.


import re


def read_file(name):
    with open(name, 'r') as f:
        pol = re.split(' |\*',f.read())
    return pol


def negat_coefs(p):
    i = 0
    while p.count('-') != 0:
        if p[i] == '-':
            p[i] += p[i + 1]
            p.pop(i + 1)
            i = 0
        i += 1
    return p


p1 = negat_coefs(read_file('pol1.txt'))
p2 = negat_coefs(read_file('pol2.txt'))

print(p1)
print(p2)


def create_dict(p):
    dic = {}
    for i in range(len(p)):
        if p[i].count('x'):
            dic[p[i]] = int(p[i - 1])
        elif p[i] == '=':
            dic[''] = int(p[i - 1])
    return(dic)


dict_set = (create_dict(p1), create_dict(p2))
print(dict_set)

# dict_res = {}     """работает только при одинаковом кол-ве элементов"""
# for key, value in dict1.items():
#     dict_res[key] = value + dict2[key]
# print(dict_res)

dict_res = {}
for diction in dict_set:
    for key in diction:
        try:
            dict_res[key] += diction[key]
        except KeyError:
            dict_res[key] = diction[key]
print(dict_res)


str_res = []
for key, item in dict_res.items():
    if key == '':
        str_res.append(f'{item} = 0')
    else:
        str_res.append(f'{item}*{key}')
res = ' + '.join(str_res)
print(res)