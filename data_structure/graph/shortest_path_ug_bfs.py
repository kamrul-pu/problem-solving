# Importing the necessary module
from collections import deque


# Function to find the shortest path using BFS
def shortest_path(g: list[list[int]], n: int, src: int) -> list[int]:
    # Initializing distance list with infinity for all nodes
    dist: list[int] = [float("inf")] * n
    # Creating a deque for BFS traversal
    q: deque = deque()
    # Adding the source node to the queue and setting its distance to 0
    q.append(src)
    dist[src] = 0

    # BFS traversal
    while q:
        # Pop the front node from the queue
        node: int = q.popleft()

        # Explore neighbors of the current node
        for it in g[node]:
            # Calculate the new distance
            nd: int = dist[node] + 1
            # Update the distance if it's shorter
            if nd < dist[it]:
                dist[it] = nd
                # Add the neighbor to the queue for further exploration
                q.append(it)

    # Return the list of shortest distances from the source node
    return dist


# Main block to test the function
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    g: list[list[int]] = [
        [1, 3],
        [0, 2, 3],
        [1, 6],
        [0, 4],
        [3, 5],
        [4, 6],
        [2, 5, 7, 8],
        [6, 8],
        [6, 7],
    ]
    # Find the shortest path from node 5
    ans: list[int] = shortest_path(g=g, n=len(g), src=0)
    # Print the result
    print(ans)
