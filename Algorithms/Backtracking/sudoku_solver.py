'''
A Sudoku solver implementation - O(n^m)
'''
import numpy as np
from typing import Tuple, List


class SudokuSolver:
    def solve(self, board: List[List[int]]) -> bool:
        """Solves the given sudoku board.

        Attempts to assign values to all unassigned locations in such a way 
        to meet the requirements (non-duplication across rows, columns, and boxes).
        
        Args:
            board: Partially filled grid.
            
        Returns:
            True if solved otherwise False.
        """
        position = self.__find_empty_position(board)
        if position == (-1, -1):
            return True
        else:
            row, column = position

        for num in range(1, 10):
            if self.__valid_position(board, num, position):
                board[row][column] = num

                if self.solve(board):
                    return True

                board[row][column] = 0  # Undo the bad choice (backtracking)

        return False

    def __valid_position(self, board: List[List[int]], num: int, position: Tuple[int, int]) -> bool:
        """Checks the grid to see if each row, column, and the 3x3 subgrids contain num.
        
        Args:
            board: Partially filled grid.

        Returns: 
            True if num is valid for the given position otherwise False.
        """
        for i in range(9):
            if board[position[0]][i] == num or board[i][position[1]] == num:
                return False

        # Check 3x3 subgrids
        x0 = (position[1] // 3) * 3
        y0 = (position[0] // 3) * 3

        for i in range(3):
            for j in range(3):
                if board[y0 + i][x0 + j] == num:
                    return False

        return True

    def __find_empty_position(self, board: List[List[int]]) -> Tuple[int, int]:
        """Finds an empty location.
        
        Args: 
            board: Partially filled grid.

        Returns:
            A tuple containing 2 integers representing an empty position in the board.
        """
        for row in range(9):
            for column in range(9):
                if board[row][column] == 0:
                    return row, column

        return -1, -1  # Row, column if board is completely filled


# Example usage
if __name__ == '__main__':
    sudoku = SudokuSolver()
    board: List[List[int]] = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
                                       [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
                                       [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
                                       [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
                                       [0, 0, 0, 0, 8, 0, 0, 7, 9]])
    print("Original Board:" + "\n")
    print(np.matrix(board))
    print("-" * 21)
    print("Solution:" + "\n")
    sudoku.solve(board)
    print(np.matrix(board))
