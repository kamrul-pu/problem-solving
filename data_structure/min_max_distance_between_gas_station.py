"""
Minimum maximum distance between gas station.
"""

import heapq


class Solution:
    def __init__(self, arr: list[int]) -> None:
        self.arr: list[int] = arr
        self.n = len(self.arr)

    def minimize_max_distance(self, k: int) -> float:
        how_many: list[int] = [0] * (self.n - 1)
        for gas_station in range(1, k + 1):
            max_section: int = -1
            max_ind: int = -1
            for i in range(0, self.n - 1, 1):
                diff: int = self.arr[i + 1] - self.arr[i]
                section_length: int = diff / (how_many[i] + 1)

                if section_length > max_section:
                    max_section = section_length
                    max_ind = i

            how_many[max_ind] += 1

        max_ans: float = -1
        for i in range(0, self.n - 1, 1):
            diff: int = self.arr[i + 1] - arr[i]
            section_length: float = diff / (how_many[i] + 1)
            max_ans = max(max_ans, section_length)

        return max_ans

    def minimize_max_distance_better(self, k: int) -> float:
        how_many = [0] * (self.n - 1)
        pq = []
        # insert the first n-1 elements into pq
        # with respective distance values:
        for i in range(self.n - 1):
            heapq.heappush(pq, ((-1) * (self.arr[i + 1]), i))

        # pick and place the k gas station
        for gas_station in range(1, k + 1):
            # find the maximum section
            # and insert the gas station
            tp = heapq.heappop(pq)
            sec_ind = tp[1]

            # insert the current gas station
            how_many[sec_ind] += 1
            initial_diff = self.arr[sec_ind + 1] - self.arr[sec_ind]
            new_section_length = initial_diff / (how_many[sec_ind] + 1)
            heapq.heappush(pq, (new_section_length * (-1), sec_ind))

        return pq[0][0] * (-1)

    def numberOfGasStationsRequired(self, dist: int):
        cnt: int = 0
        for i in range(1, self.n):
            numberInBetween = (self.arr[i] - self.arr[i - 1]) / dist
            if (self.arr[i] - self.arr[i - 1]) == (dist * numberInBetween):
                numberInBetween -= 1
            cnt += numberInBetween
        return cnt

    def minimize_max_distance_optimal(self, k: int):
        low = 0
        high = 0

        # Find the maximum distance:
        for i in range(self.n - 1):
            high = max(high, self.arr[i + 1] - self.arr[i])

        # Apply Binary search:
        diff = 1e-6
        while high - low > diff:
            mid = (low + high) / 2.0
            cnt = self.numberOfGasStationsRequired(mid)
            if cnt > k:
                low = mid
            else:
                high = mid

        return high

    def print_arr(self) -> None:
        print(self.arr, sep=" ")


if __name__ == "__main__":
    # arr = [1, 13, 17, 23]
    arr = [1, 2, 3, 4, 5]
    solution = Solution(arr)
    solution.print_arr()
    print(solution.minimize_max_distance(5))
    print(solution.minimize_max_distance_better(5))
    print(type(1e-6))
    print(solution.minimize_max_distance_optimal(5))
