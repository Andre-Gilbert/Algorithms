'''
Generate all the permutations of a list of elements - O(n!)
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List, Union


class Permutations:
    def generate_permutations(self, sequence: List[Union[str, int, float]]) -> None:
        """Generates all the permutations of a sequence of objects.
        
        Args: 
            sequence: A collection with items of type string, integer, float.

        Returns: 
            None.

            Examples:
            >>> generate_permutations([1, 2])
            [1, 2]
            [2, 1]
            >>> generate_permutations(["A", "B"])
            ["A", "B"]
            ["B", "A"]
            >>> generate_permutations(["A", 1.5])
            ["A", 1.5]
            [1.5, "A"]
        """

        if not sequence: return
        used = [False for i in range(len(sequence))]
        picked = [0 for i in range(len(sequence))]
        self.__permutations(0, used, picked, sequence)

    def __permutations(self, index: int, used: List[bool], picked: List[int], sequence: List[Union[str, int,
                                                                                                   float]]) -> None:
        """Recursive method to generate all the permutations of a sequence.
        
        Args:
            index: Current element we're considering.
            used: Elements we have currently selected in our permutation
            picked: Order of the indexes we have selected in our permutation.
            sequence: Collection we're generating permutations for.

        Returns:
            None.
        """

        if index == len(sequence):
            print(picked)  # Print valid permutation

        else:
            for i in range(len(sequence)):

                # Select an element which hasn't already been chosen
                if not used[i]:

                    # Select element i and track which element has been chosen
                    used[i] = True
                    picked[index] = sequence[i]
                    self.__permutations(index + 1, used, picked, sequence)

                    # Unselect element (backtracking)
                    used[i] = False


# Example usage
if __name__ == '__main__':
    permutation = Permutations()
    sequence = [1, 2, 3]
    print("All permutations of [1, 2, 3]:")
    permutation.generate_permutations(sequence)