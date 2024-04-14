"""
On a 2D plane, we place n stones at some integer coordinate points.
Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column
as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi]represents the location
of the ith stone, return the largest possible number of stones that can be removed.
"""

from typing import List


class Solution:
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
