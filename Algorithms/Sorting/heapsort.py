'''
Heapsort implementation O(n * log(n))
'''


class Heapsort:
    def sort(self, array: list) -> None:
        """Heap sort is a comparison based sorting technique based on Binary Heap data structure. 
        
        It is similar to selection sort where we first find 
        the maximum element and place the maximum element at the end. 
        We repeat the same process for the remaining elements.

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
        n = len(array)

        # Heapify, converts array into binary heap O(n), see:
        # http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
        for i in range(max(0, (n // 2) - 1), -1, -1):
            self.__sink(array, n, i)

        # Sorting
        for i in range(n - 1, 0, -1):
            self.__swap(array, 0, i)
            self.__sink(array, i, 0)

    def __sink(self, array: list, size: int, index: int) -> None:
        """Maintains the max-heap property for the entire tree."""
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            # Right child is larger than parent
            if right < size and array[right] > array[largest]:
                largest = right

            # Left child is larger than parent
            if left < size and array[left] > array[largest]:
                largest = left

            # Move down the tree following the largest node
            if largest != index:
                self.__swap(array, largest, index)
                index = largest
            else:
                break

    def __swap(self, array: list, i: int, j: int) -> None:
        """Swaps two items in the given array."""
        array[i], array[j] = array[j], array[i]


# Example usage
if __name__ == '__main__':
    heap = Heapsort()
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    heap.sort(array)
    print(array)
