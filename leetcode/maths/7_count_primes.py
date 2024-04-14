"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""


class Solution:
    def __prime(self, num: int) -> bool:
        if num <= 2:
            return num == 2
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False

        return True

    def countPrimes(self, n: int) -> int:
        cnt: int = 0
        for i in range(2, n):
            if self.__prime(num=i):
                cnt += 1
        return cnt


if __name__ == "__main__":
    n: int = 2
    solution: Solution = Solution()
    print(solution.countPrimes(n=n))
