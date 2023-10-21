from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        return None

    def is_empty(self) -> bool:
        return len(self.container) == 0

    def size(self) -> int:
        return len(self.container)


s = Stack()
s.push(5)
print(s.peek())

s.pop()
print(s.peek())

print(s.is_empty())

org_str: str = "We will conquere COVID-19"

for word in org_str:
    s.push(word)

while s.size() != 0:
    print(s.pop(), end="")
print()
