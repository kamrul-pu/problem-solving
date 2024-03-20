from collections import deque
import time

import threading


class Queue:
    def __init__(self) -> None:
        self.buffer = deque()

    def is_empty(self) -> bool:
        return len(self.buffer) == 0

    def size(self) -> int:
        return len(self.buffer)

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if not self.is_empty():
            return self.buffer.pop()
        return None


orders = ["pizza", "samosa", "pasta", "biryani", "burger"]

q = Queue()


def place_order(q: Queue, orders: list):
    print("placing order operations started")
    for order in orders:
        print("placing order for:", order)
        q.enqueue(order)
        time.sleep(0.5)


def server_order(q: Queue, orders: list):
    time.sleep(1)
    while not q.is_empty():
        print("Now Serving:", q.dequeue())
        time.sleep(2)


t1 = threading.Thread(
    target=place_order,
    args=(
        q,
        orders,
    ),
)
t2 = threading.Thread(
    target=server_order,
    args=(
        q,
        orders,
    ),
)

t1.start()
t2.start()

# join is optional here
t1.join()
t2.join()

# print(q)
