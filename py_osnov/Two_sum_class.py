# Учитывая массив целых чисел nums и целое число target, верните индексы двух чисел так,
#  чтобы они составляли в суммеtarget .
# Вы можете предположить, что каждый вход будет 
# иметь ровно одно решение , и вы не можете использовать один и тот же элемент дважды.
# Вы можете вернуть ответ в любом порядке.
# Пример:
# Ввод: nums = [2,7,11,15], target = 9
#  Вывод: [0,1]
#  Объяснение: Поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].

class Solution:
    def twoSum(self, nums: list[int], target: int):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                     return [i, j]


lst = [-1,-2,-3,-4,-5]
b = -8
a = Solution()
print(a.twoSum(lst, b))
