"""Graph Represantation."""
import numpy as np


def display(matrix: list[list[int]], n) -> None:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(matrix[i][j], end=" ")
        print()


# store graph as a matrix
n, m = list(map(int, input("Enter the node and edge of the graph: ").split(" ")))


matrix = np.zeros((n + 1, n + 1), dtype=np.int8)


# store as a adjacency list
# Initialize an adjacency list with empty lists
adj_list = [[] for i in range(n + 1)]

for i in range(m):
    x, y = list(map(int, input().split(" ")))
    matrix[x][y] = 1
    matrix[y][x] = 1
    adj_list[x].append(y)
    adj_list[y].append(x)

display(matrix=matrix, n=n)

print(adj_list)
