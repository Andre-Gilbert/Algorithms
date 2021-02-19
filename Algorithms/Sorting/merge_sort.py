'''
Merge sort implementation - O(n * log(n))
'''


class MergeSort:
    def sort(self, array: list) -> list:
        """Sort the given array using merge sort. 
        
        Divide array into two sub-arrays of equal number of elements.
        Conquer means sort the two sub-arrays recursively using the merge sort.
        
        Args: 
            array: An unordered collection with comparable items.

        Returns: 
            None.

            Examples:
            >>> sort([0, 5, 2, 3, 2])
            >>> print(array)
            [0, 2, 2, 3, 5]
        """
        n = len(array)
        if n <= 1: return array

        # Split array into two parts and recursively sort them
        left = self.sort(array[:n // 2])
        right = self.sort(array[n // 2:])

        # Combine the two arrays into one larger array
        return self.__merge(left, right)

    def __merge(self, left: list, right: list) -> list:
        """Merge two sorted arrays into a larger sorted array."""
        left_length = len(left)
        right_length = len(right)
        size = left_length + right_length
        index1 = 0
        index2 = 0
        array = [0] * size

        for i in range(0, size):
            if index1 == left_length:
                array[i] = right[index2]
                index2 += 1
            elif index2 == right_length:
                array[i] = left[index1]
                index1 += 1
            else:
                if left[index1] < right[index2]:
                    array[i] = left[index1]
                    index1 += 1
                else:
                    array[i] = right[index2]
                    index2 += 1

        return array


# Example usage
if __name__ == '__main__':
    merge = MergeSort()
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    array = merge.sort(array)
    print(array)
