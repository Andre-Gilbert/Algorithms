"""An implementation of a queue using a linked list."""
from typing import Generic, Iterator, TypeVar
from collections import deque

T = TypeVar('T')


class LinkedQueue(Generic[T]):
    """Class representing a queue.

    Attributes:
        _queue: The linked list queue.
    """

    def __init__(self) -> None:
        self._queue = deque()

    def size(self) -> int:
        """Returns the size of the queue."""
        return len(self._queue)

    def is_empty(self) -> bool:
        """Checks if the queue is empty."""
        return self.size() == 0

    def offer(self, elem: T) -> None:
        """Adds an element to the end of the queue."""
        self._queue.append(elem)

    def poll(self) -> T:
        """Removes the front element of the queue."""
        if self.is_empty(): raise RuntimeError('Queue is empty.')
        return self._queue.popleft()

    def peek(self) -> T:
        """Returns the front element of the queue."""
        if self.is_empty(): raise RuntimeError('Queue is empty.')
        return self._queue[0]

    def __iter__(self) -> Iterator:
        self._iter = iter(self._queue)
        return self

    def __next__(self) -> T:
        return next(self._iter)

    def __str__(self) -> str:
        return str(self._queue)

    def __bool__(self) -> bool:
        return bool(self._queue)

    def __contains__(self, elem: T) -> bool:
        return elem in self._queue


def main() -> None:
    queue = LinkedQueue()
    print(queue.is_empty())
    queue.offer(1)
    queue.offer(2)
    queue.offer(3)
    print(queue.is_empty())
    print(queue)
    print(queue.size())
    print(queue.peek())
    print(1 in queue)
    queue.poll()
    print(queue.peek())
    print(1 in queue)


if __name__ == '__main__':
    main()
