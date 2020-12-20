'''
An implementation of finding the LCM of two numbers - O(log(a + b))
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''


class LCM:
    def lcm(self, a: int, b: int) -> float:
        """Compute the lowest common multiple of a and b."""
        lcm = (a / self.__gcd(a, b)) * b
        return lcm if lcm > 0 else -lcm

    def __gcd(self, a: int, b: int) -> int:
        """Compute the greatest common divisor of a and b."""
        return a if b == 0 else self.__gcd(b, a % b)


# Example usage
if __name__ == "__main__":
    find = LCM()
    print(find.lcm(12, 18))
    print(find.lcm(5, 2))
    print(find.lcm(72, 56))