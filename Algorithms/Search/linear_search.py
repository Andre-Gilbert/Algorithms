'''
Linear search implementation - O(n)
'''


class LinearSearch:
    def search(self, array: list, target: int) -> int:
        """Returns the index of the value that we are searching for.

        This method is more memory efficient because it does not 
        create additional stack frames for recursive functions calls.

        Args:
            array: A list of integer.
            target: An integer value to search.
            
        Returns:
            An integer representing the index of the target otherwise -1.
            
            Examples:
            >>> search([0, 5, 7, 10, 15], 6)
            -1
            >>> search([0, 5, 7, 10, 15], 15)
            4
            >>> search([0, 5, 7, 10, 15], 0)
            0
        """
        if not array: return

        for i, element in enumerate(array):
            if element == target:
                return i

        return -1

    def search_recursive(self, array: list, target: int, index: int = 0) -> int:
        """Returns the index of the value that we are searching for."""

        # Base case
        if index > len(array) - 1: return -1

        if array[index] == target:
            return index

        # Recursive case
        else:
            return self.search_recursive(array, target, index + 1)


# Example usage
if __name__ == '__main__':
    ls = LinearSearch()
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    print(f"Position of 34 in the array: {ls.search(array, 34)}")
    print(f"Position of 12 in the array: {ls.search_recursive(array, 12)}")
