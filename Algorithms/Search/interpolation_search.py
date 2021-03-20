'''
An implementation of interpolation search - O(log(log(n))) if data is uniform O(n)
'''


class InterpolationSearch:
    def search(self, array: list, value: int) -> int:
        """A fast alternative to a binary search when the elements are uniformly distributed.

        Args:
            array: An ordered list containing uniformly distributed values.
            value: The value we're looking for in 'array'.

        Returns:
            The index of the value.
        """
        low, high = 0, len(array) - 1

        while array[low] <= value and array[high] >= value:
            mid = low + ((value - array[low]) * (high - low) // (array[high] - array[low]))

            if array[mid] == value:
                return mid
            if array[mid] < value:
                low += mid + 1
            else:
                high -= mid - 1

        return -1


# Example usage
if __name__ == '__main__':
    array = [10, 20, 25, 35, 50, 70, 85, 100, 110, 120, 125]
    print(f'Index of 25: {InterpolationSearch().search(array, 25)}')
    print(f'Index of 111: {InterpolationSearch().search(array, 111)}')
