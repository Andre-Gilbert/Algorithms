'''
Heapsort implementation
@author André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class Heapsort():
    def __init__(self) -> None:
        pass

    def sort(self, array: List[int]) -> None:
        if array == None: return
        n = len(array)

        for i in range(max(0, (n // 2) - 1), -1, -1):
            self.__sink(array, n, i)

        for i in range(n - 1, -1, -1):
            self.__swap(array, 0, i)
            self.__sink(array, i, 0)

    def __sink(self, array: List[int], n: int, i: int) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if right < n and array[right] > array[largest]:
                largest = right

            if left < n and array[left] > array[largest]:
                largest = left

            if largest != i:
                self.__swap(array, largest, i)
                i = largest
            else:
                break

    def __swap(self, array: List[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    heap = Heapsort()
    heap.sort(array)
    print(array)
