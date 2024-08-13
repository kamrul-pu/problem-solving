"""DFS Traversal"""

from typing import List
import numpy as np

# Define the number of nodes in the graph
n: int = 8

# Define the adjacency list representing the graph
adj_list: List[List[int]] = [
    [],  # 0 (not used in this case, since we are using 1-based indexing)
    [2, 3],  # 1 is connected to 2 and 3
    [1, 5, 6],  # 2 is connected to 1, 5, and 6
    [1, 4, 7],  # 3 is connected to 1, 4, and 7
    [3, 8],  # 4 is connected to 3 and 8
    [2],  # 5 is connected to 2
    [2],  # 6 is connected to 2
    [3, 8],  # 7 is connected to 3 and 8
    [4, 7],  # 8 is connected to 4 and 7
]

print(adj_list)


def dfs(
    node: int, adj_list: List[List[int]], visited: List[int], ans: List[int]
) -> None:
    """
    Perform Depth-First Search (DFS) traversal on a graph.

    :param node: The current node being visited
    :param adj_list: Adjacency list representing the graph
    :param visited: List to track visited nodes (1 means visited, 0 means not visited)
    :param ans: List to store the DFS traversal order
    """
    # Mark the current node as visited
    visited[node] = 1

    # Add the current node to the result list
    ans.append(node)

    # Recur for all adjacent nodes of the current node
    for neighbor in adj_list[node]:
        # If the adjacent node has not been visited, perform DFS on it
        if not visited[neighbor]:
            dfs(neighbor, adj_list, visited, ans)


# Initialize the visited list with zeros (False)
visited = np.zeros(
    n + 1, dtype=np.int_
)  # Using int_ to accommodate 1s for visited nodes

# List to store the DFS traversal order
ans: List[int] = []

# Define the starting node for DFS
starting_node: int = 1

# Mark the starting node as visited
visited[starting_node] = 1

# Perform DFS traversal starting from the defined starting node
dfs(starting_node, adj_list, visited, ans)

# Print the result of DFS traversal
print(ans)
