'''
Bubble sort implementation - O(n^2)
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class BubbleSort:
    def sort(self, array: List[int]) -> None:
        """Sort the given array using bubble sort.

        The function looks for adjacent indexes which
        are out of place and interchange their elements
        until the entire array is sorted.

        Args:
            array: An unordered collection with comparable items.

        Returns: 
            None.

            Examples:
            >>> sort([0, 5, 2, 3, 2])
            >>> print(array)
            [0, 2, 2, 3, 5]
        """

        if not array: return

        sorted = False
        while True:
            sorted = True
            for i in range(1, len(array)):
                if array[i] < array[i - 1]:
                    self.__swap(array, i - 1, i)
                    sorted = False
            if sorted: break

    def __swap(self, array: List[int], i: int, j: int) -> None:
        """Swaps two items in the given array."""

        array[i], array[j] = array[j], array[i]


# Example usage
if __name__ == '__main__':
    bubble = BubbleSort()
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    bubble.sort(array)
    print(array)