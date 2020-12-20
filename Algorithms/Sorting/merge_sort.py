'''
Merge sort implementation - O(n * log(n))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class MergeSort:
    def sort(self, array: List[int]) -> List[int]:
        """Merge sort is the algorithm which follows divide and conquer approach. 
        
        If array Contains 0 or 1 elements then it is already sorted, otherwise, 
        Divide array into two sub-array of equal number of elements.
        Conquer means sort the two sub-arrays recursively using the merge sort.
        Combine the sub-arrays to form a single final sorted array maintaining the ordering of the array.
        The main idea behind merge sort is that, the short list takes less time to be sorted.
        """
        n = len(array)
        if n <= 1: return array

        # Split array into two parts and recursively sort them
        left = self.sort(array[:n // 2])
        right = self.sort(array[n // 2:])

        # Combine the two arrays into one larger array
        return self.__merge(left, right)

    def __merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge two sorted arrays into a larger sorted array."""
        left_length = len(left)
        right_length = len(right)
        n = left_length + right_length
        idx1 = 0
        idx2 = 0
        array = [0] * n

        for i in range(0, n):
            if idx1 == left_length:
                array[i] = right[idx2]
                idx2 += 1
            elif idx2 == right_length:
                array[i] = left[idx1]
                idx1 += 1
            else:
                if left[idx1] < right[idx2]:
                    array[i] = left[idx1]
                    idx1 += 1
                else:
                    array[i] = right[idx2]
                    idx2 += 1
        return array


if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    merge = MergeSort()
    array = merge.sort(array)
    print(array)
