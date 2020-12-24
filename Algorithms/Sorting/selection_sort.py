'''
Selection sort implementation - O(n^2)
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''

from typing import List


class SelectionSort:
    def sort(self, array: List[int]) -> None:
        """Find the index beyond i with a lower value than i and swap them."""
        if not array: return
        n = len(array)

        for i in range(n):
            key = i
            for j in range(i + 1, n):
                if array[j] < array[key]:
                    key = j

            self.__swap(array, i, key)

    def __swap(self, array: List[int], i: int, j: int) -> None:
        array[j], array[i] = array[i], array[j]


# Example usage
if __name__ == "__main__":
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    selection = SelectionSort()
    selection.sort(array)
    print(array)