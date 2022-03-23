"""An implementation of merge sort - O(n * log(n))."""


class MergeSort:
    """Class that sorts arrays using merge sort."""

    def sort(self, array: list[int]) -> None:
        if len(array) <= 1: return
        self._merge_sort(array)

    def _merge_sort(self, array: list[int]) -> None:
        size = len(array)
        if size <= 1: return

        # Split array into two parts
        mid = size // 2
        left = array[:mid]
        right = array[mid:]

        # Recursively sort the arrays
        self._merge_sort(left)
        self._merge_sort(right)
        self._merge(array, left, right)

    def _merge(self, array: list[int], left: list[int], right: list[int]) -> None:
        """Merges two sorted arrays into a larger sorted array."""
        i = 0
        j = 0
        k = 0
        size_left = len(left)
        size_right = len(right)

        while i < size_left and j < size_right:
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < size_left:
            array[k] = left[i]
            i += 1
            k += 1

        while j < size_right:
            array[k] = right[j]
            j += 1
            k += 1


def main() -> None:
    sorter = MergeSort()
    array = [10, 4, 6, 4, 8, -13, 2, 3]
    sorter.sort(array)
    print(array)


if __name__ == '__main__':
    main()
