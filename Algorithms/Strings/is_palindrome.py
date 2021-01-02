'''
Test to see whether the string is a palindrome - O(n)
@author: André Gilbert, andre.gilbert.77110@gmail.com
'''


class Palindrome:
    def is_palindrome(self, s: str) -> bool:
        """Determines whether a string is a palindrome or not.
        
        A string s is a palindrome when it reads the same forward as backward.

        Args:
            s: A String.
            
        Returns:
            True if the given string is a palindrome otherwise False.

            Examples:
            >>> is_palindrome("Hello")
            False
            >>> is_palindrome("Able was I ere I saw Elba")
            True
            >>> is_palindrome("racecar")
            True
            >>> is_palindrome("Mr. Owl ate my metal worm?")
            True
        """

        s = "".join([char for char in s.lower() if char.isalnum()])
        return s == s[::-1]


# Example usage
if __name__ == "__main__":
    palindrome = Palindrome()
    s = "a man a plan a canal panama"
    print(f'"a man a plan a canal panama" is a palindrome: {palindrome.is_palindrome(s)}')