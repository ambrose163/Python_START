# Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.


nums = [22, 39, 10, 8, 56, 12, 2, 291]


def sum_odd_index_elem(nums):
    sum_odd = 0
    for i in range(1, len(nums), 2):
        sum_odd += nums[i]
    return f'Сумма элементов списка, стоящих на нечетных позициях = {sum_odd}'


print(sum_odd_index_elem(nums))
print(sum_odd_index_elem(nums=[2, 3, 5, 9, 3]))


def sum_odd_index_elem_1(nums):
    sum_odd = 0
    for i in range(0, len(nums)):
        if i % 2 != 0:
            sum_odd += nums[i]
    return f'Сумма элементов списка, стоящих на нечетных позициях = {sum_odd}'


print(sum_odd_index_elem_1(nums))
print(sum_odd_index_elem_1(nums=[2, 3, 5, 9, 3]))