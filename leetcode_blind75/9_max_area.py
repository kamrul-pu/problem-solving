class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Brute force solution O(n^2)
        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res

    def max_area(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


if __name__ == "__main__":
    soltuion = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 1]
    print(soltuion.maxArea(height))
    print(soltuion.max_area(height))
