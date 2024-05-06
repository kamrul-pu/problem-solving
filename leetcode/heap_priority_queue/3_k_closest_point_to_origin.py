"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""

import math
import heapq
from typing import List


class Solution:
    def __f(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Helper function to find the k closest points using a min-heap of fixed size k
        distances = (
            []
        )  # Min-heap to keep track of the closest points based on squared distances

        for point in points:
            # Calculate squared distance from the origin (0, 0)
            d_x_squared = point[0] ** 2
            d_y_squared = point[1] ** 2
            distance: int = d_x_squared + d_y_squared

            # Push tuple (-squared_distance, point) into the min-heap
            heapq.heappush(distances, (-distance, point))

            # If the size of distances exceeds k, remove the farthest point
            if len(distances) > k:
                heapq.heappop(distances)

        # Extract the closest k points from the heap
        return [point for _, point in distances]

    def __brute(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Helper function to find the k closest points using a min-heap (brute-force approach)
        ans = []  # List to store the closest k points
        distances = []  # Min-heap to keep track of all distances

        for point in points:
            # Calculate Euclidean distance from the origin (0, 0)
            distance = math.sqrt((0 - point[0]) ** 2 + (0 - point[1]) ** 2)

            # Push tuple (distance, point) into the min-heap
            heapq.heappush(distances, (distance, point))

        # Extract the closest k points from the heap
        while k > 0:
            _, point = heapq.heappop(distances)
            ans.append(point)
            k -= 1

        return ans

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Main method to return the k closest points to the origin (0, 0)

        # Call the optimized helper function __f to find the k closest points
        return self.__f(points=points, k=k)

        # Alternatively, use the brute-force helper function __brute to find the k closest points
        # return self.__brute(points=points, k=k)


# Example usage:
if __name__ == "__main__":
    points: List[List[int]] = [[3, 3], [5, -1], [-2, 4]]  # Example input points
    k: int = 2  # Number of closest points to find

    solution: Solution = Solution()  # Create an instance of the Solution class
    result: List[List[int]] = solution.kClosest(
        points=points, k=k
    )  # Find the k closest points
    print(result)  # Print the result (k closest points to the origin)
