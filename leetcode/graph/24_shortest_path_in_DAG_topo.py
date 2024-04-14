"""Shortest path using topo sort in DAG."""

from typing import List, Tuple


class Solution:
    def __dfs(
        self, node: int, visited: List[bool], st: List[int], g: List[Tuple[int]]
    ) -> None:
        """
        Depth-first search (DFS) to perform topological sorting.

        :param node: Current node being visited.
        :param visited: List to keep track of visited nodes.
        :param st: Stack to store the topological order.
        :param g: Adjacency list representing the graph.
        """
        visited[node] = True  # Mark the current node as visited

        # Visit neighbors of the current node
        for neighbor in g[node]:
            if not visited[neighbor[0]]:
                self.__dfs(node=neighbor[0], visited=visited, st=st, g=g)

        st.append(
            node
        )  # Add the current node to the stack after visiting all neighbors

    def __toposort(self, g: List[Tuple[int]]) -> List[int]:
        """
        Perform topological sorting using Depth-first search (DFS).

        :param g: Adjacency list representing the graph.
        :return: List representing the topological ordering of nodes.
        """
        n: int = len(g)
        visited: List[bool] = [False] * n  # List to keep track of visited nodes
        st: List[int] = []  # Stack to store the topological order

        # Start DFS for each unvisited node
        for node in range(n):
            if not visited[node]:
                self.__dfs(node=node, visited=visited, st=st, g=g)

        # Initialize distance array with infinity for all nodes
        distance: List[int] = [float("inf")] * n

        # Set distance of the source node to 0
        distance[st[-1]] = 0  # mark the distance of source node as zero

        # Update distances by relaxing edges
        while st:
            node: int = st.pop()
            # traverse all neighboring node
            for neighbor in g[node]:
                v: int = neighbor[0]
                wt: int = neighbor[1]
                # if the node weight + edge weight is smaller than current distance update it
                if distance[node] + wt < distance[v]:
                    distance[v] = distance[node] + wt

        return distance

    def shortest_path(self, g: List[Tuple[int]]) -> List[int]:
        """
        Find shortest path in a Directed Acyclic Graph (DAG).

        :param g: Adjacency list representing the graph.
        :return: List representing the shortest distance from source to each node.
        """
        return self.__toposort(g=g)


if __name__ == "__main__":
    # Example graph represented by adjacency list of tuples (destination, weight)
    g: List[Tuple[int]] = [
        [(1, 2)],
        [(3, 1)],
        [(3, 3)],
        [],
        [(0, 3), (2, 1)],
        [(4, 1)],
        [(4, 2), (5, 3)],
    ]

    # Instantiate the solution class
    solution: Solution = Solution()

    # Find shortest path in the graph
    distance: List[int] = solution.shortest_path(g=g)

    # Print the shortest distances from the source node
    print(distance)
