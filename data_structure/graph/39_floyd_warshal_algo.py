"""Floyd Warshall Algorithm. Multi-source shortest path."""


def floyd_warshall_algo(matrix: list[list[int]]) -> list[list[int]]:
    n: int = len(matrix)

    # Initialize matrix: replace -1 with a large value, set diagonal elements to 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 1e9  # A large value representing infinity
            if i == j:
                matrix[i][j] = 0

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    # Detect negative cycles
    for i in range(n):
        if matrix[i][i] < 0:
            print("There is a negative cycle in the matrix")

    # Replace large values with -1 (representing unreachable paths)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1e9:
                matrix[i][j] = -1

    return matrix


if __name__ == "__main__":
    matrix: list[list[int]] = [
        [0, 1, 43],
        [1, 0, 6],
        [-1, -1, 0],
    ]

    # Print the original matrix
    print("Original Matrix:")
    for row in matrix:
        print(row)

    # Apply Floyd-Warshall algorithm
    matrix: list[list[int]] = floyd_warshall_algo(matrix=matrix)

    # Print the result after applying the algorithm
    print("\nResult Matrix:")
    for row in matrix:
        print(row)
