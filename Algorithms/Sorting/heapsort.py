'''
Heapsort implementation O(n * log(n))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class Heapsort:
    def sort(self, array: List[int]) -> None:
        """Heap sort is a comparison based sorting technique based on Binary Heap data structure. 
        
        It is similar to selection sort where we first find the maximum element and place the maximum element at the end. 
        We repeat the same process for the remaining elements.
        """
        if not array: return
        n = len(array)

        # Heapify, converts array into binary heap O(n), see:
        # http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
        for i in range(max(0, (n // 2) - 1), -1, -1):
            self.__sink(array, n, i)

        # Sorting
        for i in range(n - 1, -1, -1):
            self.__swap(array, 0, i)
            self.__sink(array, i, 0)

    def __sink(self, array: List[int], n: int, i: int) -> None:
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            # Right child is larger than parent
            if right < n and array[right] > array[largest]:
                largest = right

            # Left child is larger than parent
            if left < n and array[left] > array[largest]:
                largest = left

            # Move down the tree following the largest node
            if largest != i:
                self.__swap(array, largest, i)
                i = largest
            else:
                break

    def __swap(self, array: List[int], i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]


# Example usage
if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    heap = Heapsort()
    heap.sort(array)
    print(array)
