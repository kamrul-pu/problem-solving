""" Find peak Element in the sorted array."""


class Solution:
    def find_sqrt(self, number: int) -> int:
        sqrt = 1
        for i in range(number + 1):
            if i * i <= number:
                sqrt = i
            else:
                break
        return sqrt

    def find_sqrt_bs(self, number: int) -> int:
        ans: int = 1
        low: int = 1
        high: int = number
        while low <= high:
            mid: int = (low + high) // 2
            if mid * mid <= number:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans  # or return high


if __name__ == "__main__":
    solution = Solution()
    print(solution.find_sqrt(49))
    print(solution.find_sqrt_bs(36))
