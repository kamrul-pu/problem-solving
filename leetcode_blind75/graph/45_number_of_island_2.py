"""
You have a 2D grid of N rows and M columns which are initially filled with water.
You are given Q queries each consisting of two integers X and Y and in each query operation,
you have to turn the water at position (X, Y) into a land. You are supposed to find the number
of islands in the grid after each query.

An island is a group of lands surrounded by water horizontally, vertically, or diagonally.
"""

from typing import List, Tuple


class DSU:
    def __init__(self, node: int) -> None:
        # Initialize DSU with parent array and size array
        self.parent: List[int] = [i for i in range(node)]  # Initialize parent array
        self.__size: List[int] = [1] * (node)  # Initialize size array

    def find_parent(self, node: int) -> int:
        # Find the parent of the set containing 'node' (with path compression)
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(node=self.parent[node])  # Path Compression
        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        # Union operation to merge two sets
        u_parent: int = self.find_parent(node=u)
        v_parent: int = self.find_parent(node=v)
        if u_parent == v_parent:
            return None
        if self.__size[u_parent] < self.__size[v_parent]:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]
        elif self.__size[u_parent] > self.__size[v_parent]:
            self.parent[v_parent] = u_parent
            self.__size[u_parent] += self.__size[v_parent]
        else:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]


class Solution:
    def __is_valid(self, row: int, col: int, n: int, m: int) -> bool:
        # Check if a given cell is within the grid boundaries
        return n > row >= 0 and m > col >= 0

    def num_of_island(self, n: int, m: int, operators: List[Tuple[int]]) -> List[int]:
        ds: DSU = DSU(
            node=n * m
        )  # Initialize disjoint set union (DSU) with number of nodes equal to number of cells in grid
        visited: List[List[bool]] = [
            [False] * m for _ in range(n)
        ]  # Initialize visited array to keep track of visited cells
        dr: List[int] = [
            -1,
            0,
            1,
            0,
        ]  # Define relative row directions for adjacent cells
        dc: List[int] = [
            0,
            1,
            0,
            -1,
        ]  # Define relative column directions for adjacent cells
        ans: List[int] = (
            []
        )  # Initialize list to store the number of islands after each query
        cnt: int = 0  # Initialize count of islands

        # Iterate through each query
        for operator in operators:
            row, col = operator  # Extract row and column from query
            if visited[row][
                col
            ]:  # If the cell has been visited, continue to the next query
                continue
            visited[row][col] = True  # Mark the cell as visited
            cnt += 1  # Increment count of islands
            node: int = row * m + col  # Calculate node number for current cell

            # Check adjacent cells to the current cell
            for ind in range(4):
                adj_row: int = row + dr[ind]  # Calculate adjacent row
                adj_col: int = col + dc[ind]  # Calculate adjacent column
                if (
                    self.__is_valid(adj_row, adj_col, n, m)
                    and visited[adj_row][adj_col]
                ):  # If adjacent cell is valid and already visited
                    adj_node: int = (
                        adj_row * m + adj_col
                    )  # Calculate node number for adjacent cell
                    if ds.find_parent(node=node) != ds.find_parent(
                        node=adj_node
                    ):  # If current cell and adjacent cell are not in the same set
                        ds.union(
                            u=node, v=adj_node
                        )  # Merge the sets of current cell and adjacent cell
                        cnt -= 1  # Decrement count of islands as they are now connected

            ans.append(cnt)  # Append count of islands after processing current query

        return ans  # Return the list containing number of islands after each query


if __name__ == "__main__":
    operators: List[Tuple[int]] = [
        (0, 0),
        (0, 0),
        (1, 1),
        (1, 0),
        (0, 1),
        (0, 3),
        (1, 3),
        (0, 4),
        (3, 2),
        (2, 2),
        (1, 2),
        (0, 2),
    ]
    n: int = 4  # Number of rows in the grid
    m: int = 5  # Number of columns in the grid
    solution: Solution = Solution()  # Initialize solution object
    print(
        solution.num_of_island(n=n, m=m, operators=operators)
    )  # Print the result of number_of_island function
