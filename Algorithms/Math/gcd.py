'''
An implementation of finding the GCD of two numbers - O(log(a + b))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''


class GCD:
    def gcd(self, a: int, b: int) -> int:
        """Compute the greatest common divisor of a and b"""
        return a if b == 0 else self.gcd(b, a % b)


if __name__ == "__main__":
    find = GCD()
    print(find.gcd(12, 18))
    print(find.gcd(5, 0))
    print(find.gcd(72, 56))