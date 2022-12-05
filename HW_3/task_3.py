# Задайте список из вещественных чисел, округленных до сотых.
# Найдите разницу между максимальным и минимальным значением дробной части элементов.


nums = [1.1, 1.2, 3.1, 5.1, 10.01]


def max_decimals(nums):
    maxim = nums[0] % 1
    for i in range(1, len(nums)):
        if nums[i] % 1 > maxim:
            maxim = nums[i] % 1
    return round(maxim, 3)


def min_decimals(nums):
    minim = nums[0] % 1
    for i in range(1, len(nums)):
        if nums[i] % 1 < minim:
            minim = nums[i] % 1
    return round(minim, 3)


diff = max_decimals(nums) - min_decimals(nums)
print(diff)