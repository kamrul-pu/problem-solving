"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

from typing import List


class Solution:
    def __brute(self, intervals: List[List[int]]) -> List[List[int]]:
        n: int = len(intervals)
        intervals.sort()  # Sort intervals based on the starting point

        ans: List[List[int]] = []
        for i in range(n):
            start: int = intervals[i][0]
            end: int = intervals[i][1]

            # If the current interval overlaps with the last merged interval in ans,
            # merge them by updating the end of the last interval in ans
            if ans and end <= ans[-1][1]:
                continue

            # Iterate through remaining intervals to find all overlapping intervals
            for j in range(i + 1, n):
                if (
                    intervals[j][0] <= end
                ):  # Check if intervals[j] overlaps with the current interval
                    end = max(
                        end, intervals[j][1]
                    )  # Merge intervals by updating the end
                else:
                    break  # No more overlap, break the inner loop

            ans.append([start, end])  # Append the merged interval to ans

        return ans

    def __optimal(self, intervals: List[List[int]]) -> List[List[int]]:
        n: int = len(intervals)
        intervals.sort()  # Sort intervals based on the starting point

        ans: List[List[int]] = []
        for i in range(n):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])  # No overlap, append the interval directly
            else:
                ans[-1][1] = max(
                    ans[-1][1], intervals[i][1]
                )  # Merge by updating the end of the last interval in ans

        return ans

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # return self.__brute(intervals=intervals)  # Uncomment to use the brute-force approach
        return self.__optimal(
            intervals=intervals
        )  # Use the optimal approach by default


if __name__ == "__main__":
    intervals: List[List[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution: Solution = Solution()
    result: List[List[int]] = solution.merge(intervals=intervals)
    print(result)
