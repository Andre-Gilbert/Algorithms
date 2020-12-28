'''
An implementation of finding the GCD of two numbers - O(log(a + b))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''


class GCD:
    def gcd(self, a: int, b: int) -> int:
        """Compute the greatest common divisor of a and b.
        
        Below method is more memory efficient because it does not 
        create additional stack frames for recursive functions calls.

        Args: 
            a: An integer.
            b: An integer.

        Returns:
            An integer representing the gcd of a and b.

            Example:
            >>> gcd(24, 40)
            8
            >>> gcd(3, 9)
            3
            >>> gcd(16, 4)
            4
        """

        return a if b == 0 else self.gcd(b, a % b)

    def gcd_iterative(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a


# Example usage
if __name__ == "__main__":
    find = GCD()
    print(f"Greatest Common Divisor of 12 & 18 = {find.gcd(12, 18)}")
    print(f"Greatest Common Divisor of 72 & 56 = {find.gcd_iterative(72, 56)}")