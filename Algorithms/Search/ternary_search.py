'''
Ternary search implementation - O(log(high - low)).
'''
# Function which decreases then increases (U shape)
function = [16, 12, 10, 3, 6, 7, 9, 10, 11, 12, 13, 17]
f = lambda i: function[i]


class TernarySearch:
    def __init__(self) -> None:
        # Define a very small epsilon value to compare double values.
        self.EPS = 0.000000001

    def search(self, low: int, high: int) -> float:
        """Finds the minimum value.

        Args:
            low: First element of function.
            high: Last element of function.
        
        Returns:
            The minimum value as an integer.

            Examples:
            >>> function = [10, 1, 4]
            >>> search(0, len(function) - 1)
            1.0000
            >>> function = [16, 12, 10, 3, 6, 7, 9, 10, 11, 12, 13, 17]
            >>> search(0, len(function) - 1)
            3.0000
        """
        while low != high:
            if high - low == 1: return min(f(low), f(high))
            if high - low == 2: return min(f(low), min(f(low + 1), f(high)))

            mid1 = (2 * low + high) // 3
            mid2 = (low + 2 * high) // 3
            res1 = f(mid1)
            res2 = f(mid2)

            if abs(res1 - res2) < self.EPS:
                low = mid1
                high = mid2
            elif res1 > res2:
                low = mid1
            else:
                high = mid2

        return low


# Example usage
if __name__ == '__main__':
    print(f'Min value: {TernarySearch().search(0, len(function) - 1):.4f}\n')
