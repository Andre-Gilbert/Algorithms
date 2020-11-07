'''
Implementation of an integer only array
@author André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class IntArray():
    __DEFAULT_CAP = 1 << 3

    def __init__(self, capacity=None) -> None:
        self.length = 0

        if capacity < 0: raise ValueError(f"Illegal Capacity: {capacity}")
        if capacity is None:
            self.capacity = __DEFAULT_CAP
            self.array = [] * __DEFAULT_CAP
        else:
            self.capacity = capacity
            self.array = [] * capacity

    def len(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.length == 0


array = IntArray()