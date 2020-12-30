'''
Use the sieve of eratosthenes to find all the prime numbers up to a certain limit. - O(n * log(log(n)))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''
from typing import List


class SieveOfEratosthenes:
    def sieve(self, num: int) -> List[int]:
        """Gets all primes up to, but NOT including limit (returned as a list of primes).

        Args: 
            num: An integer.

        Returns:
            A list of integers containing only prime numbers.

            Examples:
            >>> sieve(10)
            [2, 3, 5, 7]
            >>> sieve(20)
            [2, 3, 5, 7, 11, 13, 17, 19]
            >>> sieve(1)
            []
        """

        if num < 2: return []

        primes = [n for n in range(2, num + 1)]
        i = 2

        while i * i <= num:
            if i in primes:
                for j in range(i * 2, num + 1, i):
                    if j in primes:
                        primes.remove(j)

            i += 1

        return primes


# Example usage
if __name__ == '__main__':
    primes = SieveOfEratosthenes()
    print(primes.sieve(100))