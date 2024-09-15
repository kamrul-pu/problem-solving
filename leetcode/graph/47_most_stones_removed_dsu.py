"""
On a 2D plane, we place n stones at some integer coordinate points.
Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column
as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi]represents the location
of the ith stone, return the largest possible number of stones that can be removed.
"""

from typing import List, Dict, Tuple


class DSU:
    def __init__(self, node: int) -> None:
        self.parent: List[int] = [i for i in range(node)]  # Parent array
        self.__size: List[int] = [1] * node  # Size array

    def find(self, node: int) -> int:
        if self.parent[node] == node:
            return node
        # Path Compression
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u: int, v: int) -> None:
        u_parent = self.find(u)
        v_parent = self.find(v)
        if u_parent == v_parent:
            return
        # Union by size
        if self.__size[u_parent] < self.__size[v_parent]:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]
        elif self.__size[u_parent] > self.__size[v_parent]:
            self.parent[v_parent] = u_parent
            self.__size[u_parent] += self.__size[v_parent]
        else:
            self.parent[u_parent] = v_parent
            self.__size[v_parent] += self.__size[u_parent]

    def get_size(self, node: int) -> int:
        return self.__size[self.find(node)]


class Solution:
    def maxRemove(self, adj: List[List[int]], n: int) -> int:
        """
        Calculate the maximum number of stones that can be removed such that
        no two stones share the same row or column after removal.

        :param adj: A list of stones represented by their (row, column) positions.
        :param n: The total number of stones.
        :return: The maximum number of stones that can be removed.
        """
        mx_row = 0
        mx_col = 0
        # Find the maximum index for rows and columns
        for r, c in adj:
            mx_row = max(mx_row, r)
            mx_col = max(mx_col, c)

        # Initialize DSU with enough space to accommodate all row and column indices
        ds = DSU(mx_row + mx_col + 2)

        stone_nodes: Dict[int, int] = {}  # To track the involved rows and columns
        for stone in adj:
            r, c = stone
            node_row = r
            node_col = c + mx_row + 1  # Offset columns to ensure unique indices
            ds.union(node_row, node_col)
            stone_nodes[node_row] = 1
            stone_nodes[node_col] = 1

        # Count the number of unique components
        cnt = 0
        for k in stone_nodes:
            if ds.find(k) == k:
                cnt += 1

        # The number of stones that can be removed is total stones minus the number of unique components
        return n - cnt

    def removeStones(self, stones: List[List[int]]) -> int:
        graphR = {}
        graphC = {}
        for stone in stones:
            if stone[0] not in graphR:
                graphR[stone[0]] = [stone[1]]

            else:
                graphR[stone[0]].append(stone[1])

            if stone[1] not in graphC:
                graphC[stone[1]] = [stone[0]]
            else:
                graphC[stone[1]].append(stone[0])
        print(graphR, graphC)

        def bfs(node, visited):
            # visited[node] = 1
            # if node not in graph:
            #     return 0
            q = [node]
            # rows = []
            removedStones = 0  # len(graph[node])
            while q:
                # print(q)
                currRow = q.pop()
                if currRow in visited:
                    continue
                # rows.append(currRow)
                removedStones += len(graphR[currRow])
                visited[currRow] = 1
                for col in graphR[currRow]:
                    # if col not in graphC:
                    #     continue
                    for row in graphC[col]:
                        if row not in visited:
                            q.append(row)
            return removedStones

        ans = 0
        visited = {}
        # covered = {}
        for key in graphR.keys():
            if key not in visited:
                removedStones = bfs(key, visited) - 1
                ans += removedStones

        return ans


if __name__ == "__main__":
    stones: List[List[int]] = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    stones = [[0, 0]]
    stones = [[0, 1], [1, 0]]
    solution: Solution = Solution()
    print(solution.removeStones(stones=stones))
