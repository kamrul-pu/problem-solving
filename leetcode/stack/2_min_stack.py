"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

from typing import List


class MinStack:
    def __init__(self) -> None:
        # Initialize two stacks:
        # - 'st' for storing values pushed onto the stack
        # - 'mn_l' for keeping track of the minimum value at each point in 'st'
        self.st: List[int] = []
        self.mn_l: List[int] = []

    def push(self, val: int) -> None:
        # Push the value onto the main 'st'
        self.st.append(val)

        # Determine the minimum value encountered so far
        # If 'mn_l' is not empty, compare 'val' with the current minimum in 'mn_l'
        # Otherwise, use 'val' itself as the initial minimum
        val = min(val, self.mn_l[-1] if self.mn_l else val)

        # Push the current minimum 'val' onto 'mn_l'
        self.mn_l.append(val)

    def pop(self) -> int:
        # Pop the top value from 'mn_l' (which corresponds to the minimum value at this point)
        self.mn_l.pop()

        # Pop and return the top value from the main 'st'
        return self.st.pop()

    def top(self) -> int:
        # Return the top value from the main 'st' (without removing it)
        return self.st[-1]

    def getMin(self) -> int:
        # Return the top value from 'mn_l', which represents the current minimum value in 'st'
        return self.mn_l[-1]


if __name__ == "__main__":
    obj: MinStack = MinStack()
    obj.push(val=-2)
    obj.push(val=0)
    obj.push(val=-3)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
