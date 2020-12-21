'''
Test to see whether two numbers are relatively prime - O(log (a + b))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''


class RelativelyPrime:
    def are_coprime(self, a: int, b: int) -> bool:
        """Two numbers are relatively prime if greatest common factor is 1."""
        return self.__gcf(a, b) == 1

    def __gcf(self, a: int, b: int) -> int:
        """Find the greatest common factor between two numbers."""
        return a if b == 0 else self.__gcf(b, a % b)


# Example usage
if __name__ == "__main__":
    check = RelativelyPrime()
    print(check.are_coprime(12, 6))
    print(check.are_coprime(3, 7))
