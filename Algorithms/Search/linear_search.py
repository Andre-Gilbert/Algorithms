'''
Linear search implementation
@author André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class LinearSearch:
    def search(self, array: List[int], target: int) -> int:
        for i, element in enumerate(array):
            if element == target:
                return i
        return -1


if __name__ == '__main__':
    array = [10, 2, 24, 12, 34, 1, 3, 2, 1, 79]
    ls = LinearSearch()
    index_of_34 = ls.search(array, 34)
    print(index_of_34)
