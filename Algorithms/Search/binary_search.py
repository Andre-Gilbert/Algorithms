'''
Binary search implementation - O(log(n))
'''


class BinarySearch:
    def binary_search(self, array: list, target: int) -> int:
        """Returns the index of the value that we are searching for.
        
        Be careful collection must be ascending sorted, otherwise result will be
        unpredictable.

        Args:
            array: An ascending sorted collection with comparable items.
            target: An integer value to search.

        Returns:
            An integer representing the index of the target otherwise -1.

            Examples:
            >>> binary_search([0, 5, 7, 10, 15], 0)
            0
            >>> binary_search([0, 5, 7, 10, 15], 15)
            4
            >>> binary_search([0, 5, 7, 10, 15], 5)
            1
        """
        if not array: return
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

    def binary_search_recursive(self, array: list, target: int, low: int, hi: int) -> int:
        """Returns the index of the value that we are searching for."""

        # Base case
        if low > hi: return -1

        mid = (low + hi) // 2
        if array[mid] == target:
            return mid

        # Recursive cases
        if array[mid] > target:
            return self.binary_search_recursive(array, target, low, mid - 1)
        else:
            return self.binary_search_recursive(array, target, mid + 1, hi)


# Example usage
if __name__ == '__main__':
    bs = BinarySearch()
    array = [-1, 1, 2, 4, 5, 20, 22, 34, 134, 379]
    print(f"Position of 22 in the array: {bs.binary_search(array, 22)}")
    print(f"Position of 34 in the array: {bs.binary_search_recursive(array, 34, 0, len(array))}")
