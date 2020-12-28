'''
Tests whether a number is a prime number or not - O(sqrt(n))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''

from math import sqrt


class IsPrime:
    def is_prime(self, n: int) -> bool:
        """Checks to see if a number is a prime.

        A number is prime if it has exactly two factors: 1 and itself.

        Args: 
            n: An integer.

        Returns:
            True if n is a prime number otherwise False.

            Example:
            >>> is_prime(2)
            True
            >>> is_prime(3)
            True
            >>> is_prime(4)
            False
        """

        if n < 2: return False
        if (n == 2 or n == 3): return True
        if (n % 2 == 0 or n % 3 == 0): return False

        limit = int(sqrt(n))

        for i in range(5, limit + 1):
            if (n % i == 0 or n % (i + 2) == 0):
                return False

        return True

    def is_prime_recursive(self, n: int, i: int = 2) -> bool:
        # Base cases
        if n <= 2: return True if n == 2 else False
        if n % i == 0: return False
        if i * i > n: return True

        # Recursive Case
        return self.is_prime_recursive(n, i + 1)


if __name__ == "__main__":
    find = IsPrime()
    print(f"1433 is a prime number: {find.is_prime(1433)}")
    print(f"1231 is a prime number: {find.is_prime_recursive(1231)}")
