"""Bread first search BFS in a graph."""

from typing import List, Deque
from collections import deque


def bfs(adj_list: List[List[int]], n: int, source: int) -> List[int]:
    """
    Perform Breadth-First Search (BFS) traversal on a graph represented by an adjacency list.

    Args:
        adj_list (List[List[int]]): Adjacency list representation of the graph.
        n (int): Number of nodes in the graph.
        source (int): Source node from which BFS traversal starts.

    Returns:
        List[int]: List containing the nodes visited during BFS traversal.
    """
    # Initialize a list to keep track of visited nodes
    visited: List[bool] = [False] * (n + 1)
    # Initialize a list to store the order of visited nodes
    ans: List[int] = []
    # Initialize a deque for BFS traversal
    q: Deque = deque()

    # Start BFS traversal from the source node
    q.append(source)
    visited[source] = True

    while q:
        # Pop the first node from the queue
        node: int = q.popleft()
        # Append the node to the list of visited nodes
        ans.append(node)
        # Visit all neighbors of the current node
        for neighbor in adj_list[node]:
            # If the neighbor has not been visited, add it to the queue and mark it as visited
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True

    # Return the list of visited nodes
    return ans


if __name__ == "__main__":
    # Define the number of nodes in the graph
    n: int = 8
    # Define the adjacency list representation of the graph
    adj_list: List[List[int]] = [[], [], [], [], [], [], [], [], []]
    adj_list[1] = [2, 6]
    adj_list[2] = [1, 3, 4]
    adj_list[3] = [2]
    adj_list[4] = [2, 5]
    adj_list[5] = [4, 7]
    adj_list[6] = [1, 7, 8]
    adj_list[7] = [6, 5]
    adj_list[8] = [6]
    # Print the adjacency list
    print(adj_list)
    # Perform BFS traversal starting from node 1
    result: List[int] = bfs(adj_list=adj_list, n=n, source=1)
    # Print the order of visited nodes
    print(result)
