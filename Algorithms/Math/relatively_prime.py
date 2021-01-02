'''
Test to see whether two numbers are relatively prime - O(log (a + b))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''


class RelativelyPrime:
    def are_coprime(self, a: int, b: int) -> bool:
        """Checks whether two number are coprime.
        
        Two numbers are relatively prime if greatest common factor is 1.
        
        Args:
            a: An integer.
            b: An integer.
            
        Returns:
            True if two numbers are relatively prime otherwise False.
            
            Examples:
            >>> are_coprime(12, 18)
            False
            >>> are_coprime(9, 3)
            False
            >>> are_coprime(3, 7)
            True
        """

        return self.__gcf(a, b) == 1

    def __gcf(self, a: int, b: int) -> int:
        """Find the greatest common factor between two numbers."""
        return a if b == 0 else self.__gcf(b, a % b)


# Example usage
if __name__ == "__main__":
    check = RelativelyPrime()
    print(f"12 & 6 are relatively prime: {check.are_coprime(12, 6)}")
    print(f"10 & 3 are relatively prime: {check.are_coprime(10, 3)}")
