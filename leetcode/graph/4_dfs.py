"""Depth first search."""

from typing import List


def dfs(
    node: int, adj_list: List[List[int]], visited: List[bool], ans: List[int]
) -> List[int]:
    """
    Perform Depth-First Search (DFS) traversal on a graph represented by an adjacency list.

    Args:
        node (int): Current node being visited.
        adj_list (List[List[int]]): Adjacency list representation of the graph.
        visited (List[bool]): List to keep track of visited nodes.
        ans (List[int]): List to store the order of visited nodes.

    Returns:
        List[int]: List containing the nodes visited during DFS traversal.
    """
    # Mark the current node as visited
    visited[node] = True
    # Print the current node (optional, for visualization)
    print(node, end="->")
    # Append the current node to the list of visited nodes
    ans.append(node)
    # Visit all neighbors of the current node
    for neighbor in adj_list[node]:
        # If the neighbor has not been visited, recursively call DFS on it
        if not visited[neighbor]:
            dfs(node=neighbor, adj_list=adj_list, visited=visited, ans=ans)


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
    # Print the adjacency list (optional, for visualization)
    print(adj_list)
    # Initialize a list to keep track of visited nodes
    visited: List[bool] = [False] * (n + 1)
    # Initialize a list to store the order of visited nodes
    ans: List[int] = []
    # Perform DFS traversal starting from node 1
    dfs(adj_list=adj_list, node=1, visited=visited, ans=ans)
    # Print the order of visited nodes
    print(ans)
