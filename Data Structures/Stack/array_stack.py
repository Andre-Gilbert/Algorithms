'''
An array implementation of a stack
'''


class Stack:
    def __init__(self) -> None:
        """Creates the initial state of the stack."""
        self.__stack = []

    def push(self, elem: int) -> None:
        """Add an element to the top of the stack."""
        self.__stack.append(elem)

    def pop(self) -> int:
        """Removes the element on top of the stack."""
        return self.__stack.pop()

    def peek(self) -> int:
        """Returns the element at the top of the stack."""
        return self.__stack[-1]

    def is_empty(self) -> bool:
        """Returns whether the stack is empty."""
        return not self.__stack

    def size(self) -> int:
        """Returns the number of elements inside the stack."""
        return len(self.__stack)

    def __contains__(self, elem) -> bool:
        """Checks if an element is in the stack."""
        return elem in self.__stack

    def __str__(self) -> str:
        """Returns the string representation of the stack."""
        return str(self.__stack)


# Example usage
if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(f"Stack: {str(stack)}")
    print(f"2 in stack: {2 in stack}")
    print(f"Stack size: {stack.size()}")
    print(f"Current top: {stack.peek()}")
    stack.pop()
    print(f"Stack size: {stack.size()}")
    print(f"Empty stack: {stack.is_empty()}")
    print(f"Current top: {stack.peek()}")
    stack.pop()
    print(f"Empty stack: {stack.is_empty()}")
