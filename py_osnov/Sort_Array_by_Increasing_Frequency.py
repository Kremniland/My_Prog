'''
Дан массив целых чисел nums, отсортируйте массив в порядке возрастания в зависимости от
 частоты значений. Если несколько значений имеют одинаковую частоту, отсортируйте их в 
 порядке убывания .
Вернуть отсортированный массив.

Пример 1:

Ввод: nums = [1,1,2,2,2,3]
 Вывод: [3,1,1,2,2,2]
 Объяснение: «3» имеет частоту 1, «1» имеет частоту 2, а «2» имеет частоту 3.

Пример 2:

Ввод: nums = [2,3,1,3,2]
 Вывод: [1,3,3,2,2]
 Объяснение: «2» и «3» имеют частоту 2, поэтому они отсортированы по убыванию
'''
import collections

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = collections.Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))


nums = [1,1,2,2,2,3]
pt = Solution()
print(pt.frequencySort(nums))