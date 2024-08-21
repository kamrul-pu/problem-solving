from typing import List


class Solution:
    def __dfs(self, i: int, col: int, color: List[int], g: List[List[int]]) -> bool:
        """
        Perform DFS to color the graph and check for bipartiteness.

        :param i: The current node index to process.
        :param col: The color to assign to the current node.
        :param color: A list storing the color of each node (-1 means uncolored).
        :param g: The adjacency list representation of the graph.
        :return: True if the graph is bipartite starting from this node, False otherwise.
        """
        # Color the current node with the given color
        color[i] = col

        # Iterate through all the neighbors of the current node
        for neighbor in g[i]:
            # If the neighbor has not been colored, color it with the opposite color
            if color[neighbor] == -1:
                if not self.__dfs(neighbor, int(not col), color, g):
                    return False
            # If the neighbor is colored with the same color as the current node, return False
            elif color[neighbor] == col:
                return False

        # Return True if all neighbors are properly colored
        return True

    def is_bipartite(self, g: List[List[int]]) -> bool:
        """
        Check if the given graph is bipartite.

        :param g: The adjacency list representation of the graph.
        :return: True if the graph is bipartite, False otherwise.
        """
        n: int = len(g)  # Number of nodes in the graph
        color: List[int] = [-1] * n  # Initialize the color array with -1 (uncolored)

        # Process each node in the graph
        for node in range(n):
            # If the node is not colored, start a DFS from this node with color 0
            if color[node] == -1:
                if not self.__dfs(node, 0, color, g):
                    return False

        # If all nodes are properly colored and no conflicts were found, return True
        return True


if __name__ == "__main__":
    # Example graph:
    # 0 -- 1 -- 2 -- 3 -- 4
    #          |       |
    #          5       5
    g: List[List[int]] = [
        [1],  # Node 0 is connected to node 1
        [0, 2, 4],  # Node 1 is connected to nodes 0, 2, and 4
        [1, 3],  # Node 2 is connected to nodes 1 and 3
        [2, 5, 4],  # Node 3 is connected to nodes 2, 5, and 4
        [1, 3],  # Node 4 is connected to nodes 1 and 3
        [3],  # Node 5 is connected to node 3
    ]

    solution: Solution = Solution()
    print(solution.is_bipartite(g=g))  # Output: True
