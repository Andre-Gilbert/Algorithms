'''
Binary search implementation
@author André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class BinarySearch:
    def binary_search_iterative(self, array: List[int], target: int) -> int:
        if len(array) == 0: return
        low = 0
        hi = len(array) - 1

        while low <= hi:
            mid = (hi + low) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                low = mid + 1
            else:
                hi = mid - 1
        return -1

    def binary_search_recursive(self, array: List[int], target: int, low: int, hi: int) -> int:
        if low > hi: return -1

        mid = (low + hi) // 2
        if array[mid] == target:
            return mid

        if array[mid] > target:
            return self.binary_search_recursive(array, target, low, mid - 1)
        else:
            return self.binary_search_recursive(array, target, mid + 1, hi)


if __name__ == '__main__':
    array = [-1, 1, 2, 4, 5, 20, 22, 34, 134, 379]
    bs = BinarySearch()
    index_of_34 = bs.binary_search_iterative(array, 34)
    print(index_of_34)
    print("---")
    index_of_2 = bs.binary_search_recursive(array, 2, 0, len(array))
    print(index_of_2)
