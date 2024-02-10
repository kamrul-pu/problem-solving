class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = [int(i) for i in range(-1000, 1001)]
        return ans[1000 + a + b]


if __name__ == "__main__":
    soltuion = Solution()
    a, b = 2, 3
    print(soltuion.getSum(a, b))
