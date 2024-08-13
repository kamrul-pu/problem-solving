"""BFS Traversal"""

from collections import deque
from typing import List
import numpy as np

# Define the number of nodes in the graph
n: int = 8

# Initialize the adjacency list with empty lists for each node
# Adding an extra empty list for 0-index which is not used in this case (1-based indexing)
adj_list: list[List[int]] = [
    [],
    [2, 6],
    [1, 3, 4],
    [2],
    [2, 5],
    [4, 7],
    [1, 7, 8],
    [6, 5],
    [6],
]

print(adj_list)


def bfs(adj_list: List[List[int]], n: int, root: int) -> List[int]:
    """
    Perform Breadth-First Search (BFS) traversal on a graph.

    :param adj_list: Adjacency list representing the graph
    :param n: Number of nodes in the graph (assuming 1-based indexing)
    :param root: The starting node for BFS traversal
    :return: A list of nodes in the order they were visited during BFS
    """

    # Initialize a list to keep track of visited nodes
    # Using numpy to create a boolean array of size n+1, initialized to False
    visited: List[bool] = np.zeros(n + 1, dtype=np.bool_)

    # List to store the BFS traversal order
    ans: List[int] = []

    # Initialize the queue for BFS using deque
    q = deque()

    # Start the BFS from the root node
    q.append(root)
    visited[root] = True  # Mark the root node as visited

    while q:
        # Dequeue a node from the front of the queue
        node: int = q.popleft()

        # Add the node to the result list
        ans.append(node)

        # Iterate through all adjacent nodes of the dequeued node
        for item in adj_list[node]:
            # If the adjacent node has not been visited, mark it as visited and enqueue it
            if not visited[item]:
                q.append(item)
                visited[item] = True

    return ans


# Call the BFS function starting from node 1
result: List[int] = bfs(adj_list=adj_list, n=n, root=1)
print(result)
