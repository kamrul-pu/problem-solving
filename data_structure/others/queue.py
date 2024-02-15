from collections import deque


class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()

    def is_empty(self) -> bool:
        return len(self.buffer) == 0

    def size(self) -> int:
        return len(self.buffer)


pq = Queue()

pq.enqueue(
    {
        "company": "Wall Mart",
        "timestamp": "15 apr, 11.01 AM",
        "price": 131.10,
    }
)
pq.enqueue(
    {
        "company": "Wall Mart",
        "timestamp": "15 apr, 11.02 AM",
        "price": 132,
    }
)
pq.enqueue(
    {
        "company": "Wall Mart",
        "timestamp": "15 apr, 11.03 AM",
        "price": 135,
    }
)
print(pq.size())

print(pq.buffer)

print(pq.dequeue())
