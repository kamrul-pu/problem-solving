"""Find safe nodes in directed graph using dfs."""

from typing import List


class Solution:
    def __dfs(
        self,
        node: int,
        graph: List[List[int]],
        vis: List[bool],
        path_vis: List[bool],
        check: List[bool],
    ) -> bool:
        # Mark the current node as visited and add it to the current path.
        vis[node] = True
        path_vis[node] = True

        # Explore all neighbors of the current node.
        for neighbor in graph[node]:
            # If the neighbor has not been visited, recursively perform DFS.
            if not vis[neighbor]:
                if self.__dfs(neighbor, graph, vis, path_vis, check):
                    # If a cycle is detected in the DFS path, mark the current node as unsafe.
                    check[node] = False
                    return True
            # If the neighbor is in the current path, a cycle is detected.
            elif path_vis[neighbor]:
                check[node] = False
                return True

        # If no cycles are detected from this node, mark it as safe.
        check[node] = True
        # Remove the node from the current DFS path.
        path_vis[node] = False
        return False

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Finds all safe nodes in a directed graph.

        Args:
        - graph: Adjacency list representing the directed graph.

        Returns:
        - List[int]: A list of all safe nodes.
        """
        n: int = len(graph)
        # Lists to track visited nodes, nodes in the current path, and safe nodes.
        vis: List[bool] = [False] * n
        path_vis: List[bool] = [False] * n
        check: List[bool] = [False] * n

        # Perform DFS for each node that hasn't been visited yet.
        for node in range(n):
            if not vis[node]:
                self.__dfs(
                    node=node, graph=graph, vis=vis, path_vis=path_vis, check=check
                )

        # Collect all nodes that are marked as safe.
        safe_nodes: List[int] = []
        for i in range(n):
            if check[i]:
                safe_nodes.append(i)

        return safe_nodes


if __name__ == "__main__":
    # Example usage of the find_safe_nodes function with a directed graph represented as an adjacency list.
    g: List[List[int]] = [
        [1],  # Node 0 -> Node 1
        [2],  # Node 1 -> Node 2
        [3],  # Node 2 -> Node 3
        [4, 5],  # Node 3 -> Node 4, Node 5
        [6],  # Node 4 -> Node 6
        [6],  # Node 5 -> Node 6
        [7],  # Node 6 -> Node 7
        [],  # Node 7 -> No outgoing edges
        [1, 9],  # Node 8 -> Node 1, Node 9
        [10],  # Node 9 -> Node 10
        [8],  # Node 10 -> Node 8 (forming a cycle with Node 8)
        [9],  # Node 11 -> Node 9
        [10],  # Node 12 -> Node 10
    ]
    solution: Solution = Solution()
    safe_nodes: List[int] = solution.eventualSafeNodes(g)
    print(safe_nodes)  # Prints safe nodes in the graph
