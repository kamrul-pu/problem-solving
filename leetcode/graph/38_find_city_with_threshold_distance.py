"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti]
represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most
distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path
"""

from typing import List

INF: int = float("inf")


class Solution:
    def __floyd_warshal(self, matrix: List[List[int]], n: int) -> None:
        # Floyd-Warshall algorithm to compute the shortest paths between all pairs of vertices
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # If either of the paths is unreachable, continue to the next iteration
                    if matrix[i][k] == INF or matrix[k][j] == INF:
                        continue
                    # Update the shortest distance between vertices i and j via vertex k
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    def __get_city(self, distance: List[List[int]], n: int, threshold: int) -> int:
        cnt_city: int = n  # Initialize the count of reachable cities to total cities
        city_no: int = -1  # Initialize the city number with an invalid value
        # Iterate over each city
        for city in range(n):
            cnt: int = (
                0  # Initialize the count of reachable cities from the current city
            )
            # Check the distances to all adjacent cities
            for adj_city in range(n):
                # If the distance from the current city to the adjacent city is within the threshold
                if distance[city][adj_city] <= threshold:
                    cnt += 1  # Increment the count of reachable cities
            # If the count of reachable cities from the current city is less than or equal to the current minimum count
            if cnt <= cnt_city:
                cnt_city = cnt  # Update the minimum count of reachable cities
                city_no = city  # Update the city number
        return city_no  # Return the city number with the smallest number of reachable cities

    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Initialize the adjacency matrix with INF for unreachable cities
        distance: List[List[int]] = [
            [0 if col == row else INF for col in range(n)] for row in range(n)
        ]
        # Populate the adjacency matrix with edge weights
        for edge in edges:
            distance[edge[0]][edge[1]] = edge[2]
            distance[edge[1]][edge[0]] = edge[2]  # Since edges are bidirectional
        # Compute the shortest paths between all pairs of vertices
        self.__floyd_warshal(matrix=distance, n=n)
        # Return the city with the smallest number of reachable cities within the threshold
        return self.__get_city(distance=distance, n=n, threshold=distanceThreshold)


if __name__ == "__main__":
    # Test case
    n: int = 4
    edges: List[List[int]] = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold: int = 4
    solution: Solution = Solution()
    print(solution.findTheCity(n=n, edges=edges, distanceThreshold=distanceThreshold))
