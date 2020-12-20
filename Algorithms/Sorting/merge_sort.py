'''
Merge sort implementation
@author André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class MergeSort:
    def sort(self, array: List[int]) -> List[int]:
        n = len(array)
        if n <= 1: return array

        left = self.sort(array[:n // 2])
        right = self.sort(array[n // 2:])
        return self.__merge(left, right)

    def __merge(self, left: List[int], right: List[int]) -> List[int]:
        n1 = len(left)
        n2 = len(right)
        n = n1 + n2
        i1 = 0
        i2 = 0
        array = [0] * n

        for i in range(0, n):
            if i1 == n1:
                array[i] = right[i2]
                i2 += 1
            elif i2 == n2:
                array[i] = left[i1]
                i1 += 1
            else:
                if left[i1] < right[i2]:
                    array[i] = left[i1]
                    i1 += 1
                else:
                    array[i] = right[i2]
                    i2 += 1
        return array


if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    merge = MergeSort()
    array = merge.sort(array)
    print(array)
