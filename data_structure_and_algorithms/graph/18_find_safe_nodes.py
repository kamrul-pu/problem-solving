"""Find safe nodes in directed graph using dfs."""

from typing import List


def dfs_check(
    node: int,
    g: List[List[int]],
    vis: List[int],
    path_vis: List[bool],
    check: List[bool],
) -> bool:
    # Mark the current node as visited
    vis[node] = True
    path_vis[node] = True
    check[node] = False

    # Explore neighbors of the current node
    for item in g[node]:
        if not vis[item]:
            # Recursive call for unvisited neighbors
            if dfs_check(node=item, g=g, vis=vis, path_vis=path_vis, check=check):
                check[node] = False
                return True
        elif path_vis[item]:
            # If the neighbor is part of the current path, a cycle is detected
            check[node] = False
            return True

    # Backtrack: Mark the current node as not part of the current path
    check[node] = True
    path_vis[node] = False
    return False  # No cycle found


def find_safe_nodes(v: int, g: List[List[int]]) -> List[int]:
    # Initialize lists to track visited nodes, path, and check safe nodes
    vis: List[bool] = [False] * (v)
    path_vis: List[bool] = [False] * (v)
    check: List[bool] = [False] * v
    safe_nodes: List[int] = []

    # Iterate through all nodes for connected components
    for i in range(0, v):
        if not vis[i]:
            # Start DFS for each unvisited node
            dfs_check(node=i, g=g, vis=vis, path_vis=path_vis, check=check)

    # Collect safe nodes after DFS traversal
    for i in range(v):
        if check[i] == True:
            safe_nodes.append(i)

    # Return the List of safe nodes
    return safe_nodes


if __name__ == "__main__":
    # Example usage of the find_safe_nodes function with a directed graph represented as an adjacency List
    g: List[List[int]] = [
        [1],
        [2],
        [3],
        [4, 5],
        [6],
        [6],
        [7],
        [],
        [1, 9],
        [10],
        [8],
        [9],
    ]
    safe_nodes: List[int] = find_safe_nodes(v=12, g=g)
    print(safe_nodes)
