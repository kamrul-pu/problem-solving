"""Find the city with the smallest number of neighbors within a threshold distance."""


def find_city(n: int, m: int, edges: list[list[int]], distance_threshold: int) -> int:
    # Initialize a matrix to store distances between cities, initially set to infinity
    distance: list[list[int]] = [[float("inf") for col in range(n)] for row in range(n)]

    # Populate the distance matrix with given edge information
    for edge in edges:
        distance[edge[0]][edge[1]] = edge[2]
        distance[edge[1]][edge[0]] = edge[2]

    # Set the distance from a city to itself to 0
    for i in range(n):
        distance[i][i] = 0

    # Floyd-Warshall algorithm to find the shortest distances between all pairs of cities
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] == float("inf") or distance[k][j] == float("inf"):
                    continue

                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # Initialize variables to track the city with the smallest number of neighbors
    cnt_city: int = n
    city_no: int = -1

    # Iterate through each city
    for city in range(n):
        cnt: int = 0
        # Count the number of neighbors within the distance threshold for the current city
        for adj_city in range(n):
            if distance[city][adj_city] <= distance_threshold:
                cnt += 1

        # Update if the current city has fewer neighbors than the current minimum
        if cnt <= cnt_city:
            cnt_city = cnt
            city_no = city

    # Return the city with the smallest number of neighbors within the threshold
    return city_no


if __name__ == "__main__":
    n: int = 4
    m: int = 4
    edges: list[list[int]] = [(0, 1, 3), (1, 2, 1), (1, 3, 4), (2, 3, 1)]
    distance_threshold: int = 4
    city: int = find_city(n=n, m=m, edges=edges, distance_threshold=distance_threshold)
    print(city)
