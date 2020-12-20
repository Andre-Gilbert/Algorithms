'''
Bubble sort implementation - O(n^2)
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class BubbleSort:
    def sort(self, array: List[int]) -> None:
        if array == None: return

        sorted = False
        while True:
            sorted = True
            for i in range(1, len(array)):
                if array[i] < array[i - 1]:
                    self.__swap(array, i - 1, i)
                    sorted = False
            if sorted: break

    def __swap(self, array: List[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    bubble = BubbleSort()
    bubble.sort(array)
    print(array)