"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship
with packages on the conveyor belt (in the order given by weights). We may not load more
weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the
conveyor belt being shipped within days days.
"""

from typing import List


class Solution:
    def __f(self, weights: List[int], capacity: int) -> int:
        """
        Helper function to determine the number of days required to ship
        all packages with a given capacity.

        Args:
        - weights: List of integers representing the weights of packages.
        - capacity: Integer, the current capacity being tested.

        Returns:
        - int: The number of days required to ship all packages with the given capacity.
        """
        n: int = len(weights)
        days: int = 1  # Start with 1 day
        load: int = 0  # Current load on the ship
        for i in range(n):
            if load + weights[i] > capacity:
                days += 1  # Increment days since we exceed capacity
                load = weights[i]  # Start a new load with current package
            else:
                load += weights[i]  # Add current package to the current load
        return days

    def __brute(self, weights: List[int], days: int) -> int:
        """
        Brute-force approach to find the minimum weight capacity of the ship
        that allows all packages to be shipped within `days` days.

        Args:
        - weights: List of integers representing the weights of packages.
        - days: Integer, the maximum number of days allowed for shipping.

        Returns:
        - int: The minimum weight capacity found.
        """
        n: int = len(weights)
        max_weight: int = weights[0]  # Initialize max weight with the first package
        total_weight: int = weights[0]  # Initialize total weight with the first package
        for i in range(1, n):
            total_weight += weights[i]
            max_weight = max(max_weight, weights[i])

        # Iterate through possible capacities from max_weight to total_weight
        for capacity in range(max_weight, total_weight + 1):
            required_days: int = self.__f(weights, capacity)
            if required_days <= days:
                return capacity  # Return the first valid capacity found

    def __optimal(self, weights: List[int], days: int) -> int:
        """
        Optimized binary search approach to find the minimum weight capacity
        of the ship that allows all packages to be shipped within `days` days.

        Args:
        - weights: List of integers representing the weights of packages.
        - days: Integer, the maximum number of days allowed for shipping.

        Returns:
        - int: The minimum weight capacity found.
        """
        n: int = len(weights)
        max_weight: int = weights[0]  # Initialize max weight with the first package
        total_weight: int = weights[0]  # Initialize total weight with the first package
        for i in range(1, n):
            total_weight += weights[i]
            max_weight = max(max_weight, weights[i])

        lo, hi = max_weight, total_weight
        ans: int = total_weight
        while lo <= hi:
            mid: int = (lo + hi) // 2
            required_days: int = self.__f(weights, mid)
            if required_days <= days:
                ans = min(ans, mid)  # Update answer if current mid capacity is valid
                hi = mid - 1  # Search for potentially smaller capacities
            else:
                lo = mid + 1  # Search for larger capacities

        return ans

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Main function to find the least weight capacity of the ship that will
        result in all packages being shipped within `days` days.

        Args:
        - weights: List of integers representing the weights of packages.
        - days: Integer, the maximum number of days allowed for shipping.

        Returns:
        - int: The minimum weight capacity found.
        """
        # Uncomment to use the brute-force approach
        # return self.__brute(weights, days)

        # Use the optimal binary search approach
        return self.__optimal(weights, days)


if __name__ == "__main__":
    weights: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days: int = 5
    solution: Solution = Solution()
    print(solution.shipWithinDays(weights=weights, days=days))
