'''
Quick sort implementation - O(n * log(n))
'''


class QuickSort:
    def sort(self, array: list) -> None:
        """Sorts the given array using quick sort.
        
        Args:
            array: An unordered collection with comparable items.

        Returns: 
            None.

            Examples:
            >>> sort([0, 5, 2, 3, 2])
            >>> print(array)
            [0, 2, 2, 3, 5]
        """
        if not array: return array
        self.__quick_sort(array, 0, len(array) - 1)

    def __quick_sort(self, array: list, low: int, high: int) -> None:
        """Sort interval [low, high] inplace recursively."""
        if low < high:
            pivot = self.__partition(array, low, high)
            self.__quick_sort(array, low, pivot - 1)
            self.__quick_sort(array, pivot + 1, high)

    def __partition(self, array: list, low: int, high: int) -> int:
        """Performs Hoare partition algorithm for quicksort"""
        index, pivot = low - 1, array[high]

        for j in range(low, high):
            if array[j] <= pivot:
                index += 1
                self.__swap(array, index, j)

        self.__swap(array, index + 1, high)
        return index + 1

    def __swap(self, array: list, i: int, j: int) -> None:
        """Swaps two items in the given array."""
        array[i], array[j] = array[j], array[i]


# Example usage
if __name__ == "__main__":
    quick = QuickSort()
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    quick.sort(array)
    print(array)