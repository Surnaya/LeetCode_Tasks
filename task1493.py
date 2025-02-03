"""1493. Longest Subarray of 1's After Deleting One Element
Medium

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Дан бинарный массив nums. Необходимо удалить один элемент из него.

Верните размер самой длинного непустого подмассива, содержащего только единицы, в полученном массиве.
Верните 0, если такого подмассива не существует.
"""


def longest_subarray(nums):
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        # Увеличиваем счетчик, если встретили ноль
        if nums[right] == 0:
            zero_count += 1

        # Сдвигаем левый указатель, если нулей больше одного
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Вычисляем текущую длину окна и обновляем максимум
        max_length = max(max_length, right - left)

    return max_length


# Example 1:
# Input: nums = [1, 1, 0, 1]
# Output: 3
print(longest_subarray([1, 1, 0, 1]))

# Example 2:
# Input: nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
# Output: 5
print(longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))

# Example 3:
# Input: nums = [1, 1, 1]
# Output: 2
print(longest_subarray([1, 1, 1]))
