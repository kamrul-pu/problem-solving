from collections import deque


class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()
        return None

    def front(self):
        if not self.is_empty():
            return self.buffer[-1]

    def is_empty(self) -> bool:
        return len(self.buffer) == 0

    def size(self) -> int:
        return len(self.buffer)


def produce_binary(n: int):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("  ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == "__main__":
    produce_binary(10)
