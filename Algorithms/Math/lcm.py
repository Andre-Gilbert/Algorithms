'''
An implementation of finding the LCM of two numbers - O(log(a + b))
'''


class LCM:
    def lcm(self, a: int, b: int) -> float:
        """Computes the least common multiple of a and b.
        
        Args: 
            a: An integer.
            b: An integer.

        Returns:
            A float representing the lcm of a and b.

            Examples:
            >>> lcm(12, 76)
            228
            >>> lcm(5, 2)
            10
            >>> lcm(12, 18)
            36
        """
        lcm = (a / self.__gcd(a, b)) * b

        return lcm if lcm > 0 else -lcm

    def __gcd(self, a: int, b: int) -> int:
        """Computes the greatest common divisor of a and b."""
        return a if b == 0 else self.__gcd(b, a % b)


# Example usage
if __name__ == "__main__":
    find = LCM()
    print(f"Least Common Multiple of 12 & 18 = {find.lcm(12, 18)}")
    print(f"Least Common Multiple of 3 & 10 = {find.lcm(3, 10)}")
