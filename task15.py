"""15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Дан целочисленный массив nums. Верните все тройки чисел [nums[i], nums[j], nums[k]], такие что:
i != j, i != k, and j != k,
и nums[i] + nums[j] + nums[k] == 0.

Обратите внимание, что набор решений не должен содержать повторяющихся троек.
"""


def threeSum(nums):
    nums.sort()  # Сортируем массив, чтобы числа в массиве шли по возрастанию
    res = []

    for i in range(len(nums) - 2):
        # Пропускаем одинаковые элементы, чтобы избежать дубликатов
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1  # Два указателя: один в начале, другой в конце

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                # поиск нужной комбинации
                res.append([nums[i], nums[left], nums[right]])

                # Пропускаем дубликаты для левого указателя
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Пропускаем дубликаты для правого указателя
                while left < right and nums[right] == nums[right - 1]:
                    right
                # Сдвигаем указатели
                left += 1
                right -= 1

            elif total < 0:
                left += 1  # Если сумма меньше 0, сдвигаем левый указатель вправо
            else:
                right -= 1  # Если сумма больше 0, сдвигаем правый указатель влево
    return res


# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(threeSum([-1,0,1,2,-1,-4]))

# Example 2:
# Input: nums = [0,1,1]
# Output: []
print(threeSum([0,1,1]))

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
print(threeSum([0,0,0]))

# !NB 	•	Для небольших строк подход с реверсом быстрее и проще.
# 	    •	Для больших строк или ограничений по памяти предпочтителен алгоритм с двумя указателями.