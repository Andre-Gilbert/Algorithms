'''
Tests whether a number is a prime number or not - O(sqrt(n))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''

from math import sqrt, floor


class IsPrime:
    def is_prime_iterative(self, n: int) -> bool:
        if n < 2: return False
        if (n == 2 or n == 3): return True
        if (n % 2 == 0 or n % 3 == 0): return False

        limit = floor(sqrt(n))

        for i in range(5, limit + 1):
            if (n % i == 0 or n % (i + 2) == 0):
                return False

        return True

    def is_prime_recursive(self, n: int, i=2) -> bool:
        # Base cases
        if n <= 2: return True if n == 2 else False
        if n % i == 0: return False
        if i * i > n: return True

        # Recursive Cases
        return self.is_prime_recursive(n, i + 1)


if __name__ == "__main__":
    find = IsPrime()
    print(find.is_prime_iterative(5))
    print(find.is_prime_iterative(31))
    print(find.is_prime_iterative(1433))
    print("----")
    print(find.is_prime_recursive(5))
    print(find.is_prime_recursive(31))
    print(find.is_prime_recursive(1433))
