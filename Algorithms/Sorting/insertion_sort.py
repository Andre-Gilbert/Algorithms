'''
Insertion sort implementation - O(n^2)
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class InsertionSort:
    def sort(self, array: List[int]) -> None:
        if len(array) == None: return

        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j] < array[j - 1]:
                self.__swap(array, j - 1, j)
                j -= 1

    def __swap(self, array: List[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    insertion = InsertionSort()
    insertion.sort(array)
    print(array)