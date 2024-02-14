"""Deep copy a graph"""

from typing import Optional

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # If the original graph is empty, return None
        if node is None:
            return node

        # Initialize a queue for breadth-first traversal and a dictionary to store clones
        q: deque = deque([node])
        clones = {node.val: Node(node.val, neighbors=[])}

        # Traverse the original graph using breadth-first search
        while q:
            # Take out the current node from the queue
            cur: Node = q.popleft()
            # Find the clone corresponding to the current node
            cur_clone = clones[cur.val]

            # Iterate through the neighbors of the current node
            for neighbor in cur.neighbors:
                # If the neighbor has not been cloned yet, create its clone and enqueue it
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone of the current node
                cur_clone.neighbors.append(clones[neighbor.val])

        # Return the clone of the starting node of the original graph
        return clones[node.val]


if __name__ == "__main__":
    # Create a sample graph
    node1: Node = Node(val=1, neighbors=[])
    node2: Node = Node(val=2, neighbors=[])
    node3: Node = Node(val=3, neighbors=[])
    node4: Node = Node(val=4, neighbors=[])
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    # Create an instance of the solution class and clone the graph
    solution: Solution = Solution()
    print(solution.cloneGraph(node=node1))
