'''
Insertion sort implementation - O(n^2)
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class InsertionSort:
    def sort(self, array: List[int]) -> None:
        """Sort the given array using insertion sort. 

        The idea behind insertion sort is that at the array is already 
        sorted from [0, i] and you want to add the element at position i+1,
        so you 'insert' it at the appropriate location.

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

        for i in range(1, len(array)):
            j = i
            while j > 0 and array[j] < array[j - 1]:
                self.__swap(array, j - 1, j)
                j -= 1

    def __swap(self, array: List[int], i: int, j: int) -> None:
        """Swaps two items in the given array."""
        array[i], array[j] = array[j], array[i]


# Example usage
if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    insertion = InsertionSort()
    insertion.sort(array)
    print(array)