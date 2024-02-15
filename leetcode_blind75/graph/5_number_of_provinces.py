"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
and isConnected[i][j] = 0 otherwise.
"""

from typing import List


class Solution:
    def __dfs(self, node: int, adj_list: List[List[int]], visited: List[bool]) -> None:
        """
        Depth-first search (DFS) traversal function.

        Args:
            node (int): Current node being visited.
            adj_list (List[List[int]]): Adjacency list representation of the graph.
            visited (List[bool]): List to keep track of visited nodes.

        Returns:
            None
        """
        # Mark the current node as visited
        visited[node] = True
        # Visit all neighbors of the current node
        for neighbor in adj_list[node]:
            # If the neighbor has not been visited, recursively call DFS on it
            if not visited[neighbor]:
                self.__dfs(neighbor, adj_list, visited)

    def __matrix_to_adj_list(self, matrix: List[List[int]], n: int) -> List[List[int]]:
        """
        Convert adjacency matrix to adjacency list.

        Args:
            matrix (List[List[int]]): Adjacency matrix representation of the graph.
            n (int): Number of nodes in the graph.

        Returns:
            List[List[int]]: Adjacency list representation of the graph.
        """
        # Initialize an empty adjacency list
        adj_list: List[List[int]] = [[] for _ in range(n)]
        # Iterate through each cell in the matrix
        for i in range(n):
            for j in range(n):
                # If there is an edge between nodes i and j, add j to the adjacency list of node i
                if matrix[i][j] == 1:
                    adj_list[i].append(j)
        return adj_list

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Find the number of provinces.

        Args:
            isConnected (List[List[int]]): Adjacency matrix representation of the graph.

        Returns:
            int: The number of provinces.
        """
        # Get the number of nodes
        n: int = len(isConnected)
        # Convert the adjacency matrix to adjacency list
        adj_list: List[List[int]] = self.__matrix_to_adj_list(matrix=isConnected, n=n)
        # Initialize a list to keep track of visited nodes
        visited: List[bool] = [False] * (n + 1)
        # Initialize a counter for the number of provinces
        cnt: int = 0
        # Iterate through each node
        for i in range(n):
            # If the node has not been visited, start a DFS from that node
            if not visited[i]:
                self.__dfs(node=i, adj_list=adj_list, visited=visited)
                # Increment the counter for the number of provinces
                cnt += 1
        # Return the total number of provinces
        return cnt


if __name__ == "__main__":
    # Example usage
    isConnected: List[List[int]] = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    solution: Solution = Solution()
    print(solution.findCircleNum(isConnected=isConnected))
